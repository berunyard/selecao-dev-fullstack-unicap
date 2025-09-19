from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.config import config
from app.models import RequisicaoAnalise, RespostaAnalise
from app.services.ai_service import servico_ia
from app.utils.logger import logger
import time

app = FastAPI(
    title=config.NOME_PROJETO,
    version=config.VERSAO,
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ORIGENS_PERMITIDAS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/healthz")
async def verificar_saude():
    return {"status": "ok"}

@app.post("/api/v1/analisar", response_model=RespostaAnalise)
async def analisar_texto(requisicao: RequisicaoAnalise):
    inicio = time.time()
    
    try:
        logger.info(f"Requisição de análise recebida: {requisicao.tarefa}, externo: {requisicao.usar_externo}")
        
        # Processar a requisição
        resultado = servico_ia.analisar({
            "tarefa": requisicao.tarefa,
            "texto_entrada": requisicao.texto_entrada,
            "usar_externo": requisicao.usar_externo,
            "opcoes": requisicao.opcoes or {}
        })
        
        tempo_ms = int((time.time() - inicio) * 1000)
        
        resposta = RespostaAnalise(
            tarefa=requisicao.tarefa,
            motor=resultado["motor"],
            resultado=resultado["resultado"],
            tempo_ms=tempo_ms
        )
        
        logger.info(f"Análise concluída em {tempo_ms}ms")
        return resposta
        
    except ValueError as e:
        logger.error(f"Erro de validação: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Erro de processamento: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro processando requisição: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)