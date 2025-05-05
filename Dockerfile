# Escolher uma imagem base com Python
FROM python:3.10-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Instalar as dependências da aplicação
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copiar o restante dos arquivos da aplicação para dentro do container
COPY . .

# Expôr a porta que a aplicação FastAPI vai rodar
EXPOSE 8000

# Definir o comando para rodar a aplicação FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]