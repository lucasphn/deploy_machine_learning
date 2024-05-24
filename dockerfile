# Use a imagem oficial do Python 3.12.2
FROM python:3.12.2

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Expõe a porta 8501 para acesso externo
EXPOSE 8501

# Comando para executar o Streamlit quando o contêiner for iniciado
CMD ["streamlit", "run", "app.py"]
