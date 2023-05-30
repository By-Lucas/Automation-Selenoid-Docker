# Use a imagem oficial do Python como base
FROM python:3.8.0

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libxss1 \
    libappindicator1 \
    libindicator7 \
    libnss3 \
    lsb-release \
    xdg-utils

# Instale o Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Copie os arquivos de requisitos e instale-os
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instale o wait-for-it
RUN apt-get update && apt-get install -y wait-for-it

# Copie o restante do código do aplicativo
COPY . .

# Expanda a variável de ambiente PYTHONUNBUFFERED para que as saídas sejam exibidas corretamente no log do Docker
ENV PYTHONUNBUFFERED=1

# Comando para iniciar seu script
CMD ["python", "main.py"]
