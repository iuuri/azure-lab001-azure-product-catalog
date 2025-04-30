# Azure Product Catalog 📦☁️

Este é um projeto criado como parte de um laboratório prático do Bootcamp de Azure oferecido pela DIO. A aplicação permite o cadastro de produtos via uma interface web feita com Streamlit, armazenando as imagens no Azure Blob Storage e os dados em um banco de dados MySQL.

## 🚀 Funcionalidades

- Interface web com Streamlit
- Upload de imagens para Azure Blob Storage
- Cadastro de dados em banco relacional
- Uso de variáveis de ambiente com `.env`

## 🛠 Tecnologias Utilizadas

- Python
- Streamlit
- Azure Blob Storage
- MySQL (pymysql)
- dotenv

## 🧪 Como rodar o projeto localmente

1. Clone o repositório:
git clone https://github.com/seu-usuario/azure-product-catalog.git
cd azure-product-catalog

2.Crie um arquivo .env com base no .env.example e preencha com suas credenciais.

3.Instale as dependências:
pip install -r requirements.txt

4.Rode a aplicação:
streamlit run main.py

