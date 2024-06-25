docker run -dp 0.0.0.0:8501:8501 -v $PWD/data:/app/app/data s22678suml/projekt:1.1-slim
Start-Process "http://localhost:8501"