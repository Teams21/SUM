FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt-get -y update && apt-get install -y \
    python3-dev \
    apt-utils \
    build-essential \
    && rm -rf /var/lib.apt/lists* \
    && pip3 install -r build/docker-requirements.txt

CMD streamlit run --server.address 0.0.0.0 app/app.py
