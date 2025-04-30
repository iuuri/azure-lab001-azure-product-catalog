import streamlit as st 
from azure.storage.blob import BlobServiceClient
import os 
import pymysql
import uuid 
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Variáveis de ambiente
blobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
blobContainerName = os.getenv('BLOB_CONTAINER_NAME')
blobAccountName = os.getenv('BLOB_ACCOUNT_NAME')

SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USER = os.getenv('SQL_USER')    
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

st.title("Cadastro de Produto")

# Formulário de cadastro
product_name = st.text_input("Nome do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_description = st.text_area("Descrição do Produto")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

# Função para upload da imagem no Azure Blob Storage
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = str(uuid.uuid4()) + "_" + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f'https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}'
    return image_url

# Função para inserir produto no banco de dados
def insert_product(product_name, product_price, product_description, image_url):
    try:
        connection = pymysql.connect(
            host=SQL_SERVER,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )
        cursor = connection.cursor()
        sql = "INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (product_name, product_price, product_description, image_url))
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir produto: {e}")
        return False

# Ação ao clicar no botão
if st.button('Salvar Produto'):
    if not all([product_name, product_description, product_image]):
        st.warning("Por favor, preencha todos os campos e envie uma imagem.")
    else:
        image_url = upload_blob(product_image)
        success = insert_product(product_name, product_price, product_description, image_url)
        if success:
            st.success('✅ Produto cadastrado com sucesso!')
            st.image(image_url, caption="Imagem do Produto", use_column_width=True)

# Botão de exemplo para listar produtos (sem implementação real)
if st.button('Listar Produtos'):
    st.info("Funcionalidade de listagem ainda não implementada.")
