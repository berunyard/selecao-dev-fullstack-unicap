import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    NOME_PROJETO: str = "MVP IA - Análise de Sentimentos"
    VERSAO: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # API Hugging Face
    CHAVE_API_HF: str = os.getenv("CHAVE_API_HF", "")
    URL_API_HF: str = "https://api-inference.huggingface.com/models"
    
    # Configurações de modelo
    MODELO_LOCAL: str = "pysentimento/roberta-base-pt"
    MODELO_EXTERNO: str = "pysentimento/roberta-base-pt"
    
    # CORS
    ORIGENS_PERMITIDAS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

config = Config()