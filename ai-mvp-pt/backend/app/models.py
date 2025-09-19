from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from enum import Enum
from datetime import datetime
import uuid

class TipoTarefa(str, Enum):
    SENTIMENTO = "sentimento"
    ENTIDADES = "entidades"
    OCR = "ocr"
    LEGENDA = "legenda"
    PERSONALIZADO = "personalizado"

class RequisicaoAnalise(BaseModel):
    tarefa: TipoTarefa
    texto_entrada: Optional[str] = None
    usar_externo: bool = False
    opcoes: Optional[Dict[str, Any]] = None

class ResultadoSentimento(BaseModel):
    rotulo: str
    pontuacao: float

class RespostaAnalise(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    tarefa: TipoTarefa
    motor: str
    resultado: Dict[str, Any]
    tempo_ms: int
    recebido_em: datetime = Field(default_factory=datetime.utcnow)