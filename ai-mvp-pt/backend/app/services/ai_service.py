import requests
import time
from typing import Dict, Any
from app.config import config
from app.services.local_ai import servico_ai_local

class ServicoIA:
    def __init__(self):
        self.cabecalhos = {
            "Authorization": f"Bearer {config.CHAVE_API_HF}",
            "Content-Type": "application/json"
        }
    
    def analisar_sentimento_externo(self, texto: str) -> Dict[str, Any]:
        """Analisar sentimento usando API Hugging Face"""
        if not config.CHAVE_API_HF:
            raise Exception("Chave da API Hugging Face não configurada")
        
        inicio = time.time()
        
        try:
            resposta = requests.post(
                f"{config.URL_API_HF}/{config.MODELO_EXTERNO}",
                headers=self.cabecalhos,
                json={"inputs": texto}
            )
            
            if resposta.status_code != 200:
                raise Exception(f"Erro na API: {resposta.status_code} - {resposta.text}")
            
            resultado = resposta.json()[0]
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
            raise Exception(f"Erro na API externa: {e}")
    
    def analisar(self, dados_requisicao: Dict[str, Any]) -> Dict[str, Any]:
        """Método principal de análise que direciona para o serviço apropriado"""
        tarefa = dados_requisicao.get('tarefa')
        texto_entrada = dados_requisicao.get('texto_entrada')
        usar_externo = dados_requisicao.get('usar_externo', False)
        
        if not texto_entrada:
            raise ValueError("Texto de entrada é necessário para análise de sentimentos")
        
        if tarefa == 'sentimento':
            if usar_externo:
                resultado = self.analisar_sentimento_externo(texto_entrada)
                motor = f"externo:hf-{config.MODELO_EXTERNO}"
            else:
                resultado = servico_ai_local.analisar_sentimento(texto_entrada)
                motor = f"local:{config.MODELO_LOCAL}"
            
            return {
                "resultado": {"rotulo": resultado["rotulo"], "pontuacao": resultado["pontuacao"]},
                "tempo_ms": resultado["tempo_ms"],
                "motor": motor
            }
        
        else:
            raise ValueError(f"Tarefa {tarefa} não implementada")

servico_ia = ServicoIA()