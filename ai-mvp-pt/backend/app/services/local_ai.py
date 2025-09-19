import time
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import Dict, Any

class ServicoAILocal:
    def __init__(self):
        self.pipeline_sentimento = None
        self.modelo_carregado = False
        
    def carregar_modelo(self):
        """Carregamento lazy do modelo de análise de sentimentos"""
        if not self.modelo_carregado:
            try:
                self.pipeline_sentimento = pipeline(
                    "sentiment-analysis",
                    model="pysentimento/roberta-base-pt",
                    tokenizer="pysentimento/roberta-base-pt"
                )
                self.modelo_carregado = True
                print("Modelo local de análise de sentimentos carregado com sucesso")
            except Exception as e:
                print(f"Erro ao carregar modelo local: {e}")
                raise
    
    def analisar_sentimento(self, texto: str) -> Dict[str, Any]:
        """Analisar sentimento usando modelo local"""
        if not self.modelo_carregado:
            self.carregar_modelo()
        
        inicio = time.time()
        
        try:
            resultado = self.pipeline_sentimento(texto)[0]
            tempo_ms = int((time.time() - inicio) * 1000)
            
            # Traduzir rótulos para português
            rotulo_traduzido = {
                "pos": "POSITIVO",
                "neg": "NEGATIVO",
                "neu": "NEUTRO"
            }.get(resultado['label'], resultado['label'])
            
            return {
                "rotulo": rotulo_traduzido,
                "pontuacao": resultado['score'],
                "tempo_ms": tempo_ms
            }
        except Exception as e:
            raise Exception(f"Erro durante análise de sentimento: {e}")

servico_ai_local = ServicoAILocal()