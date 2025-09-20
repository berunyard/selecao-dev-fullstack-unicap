# MVP - Análise de Sentimentos em Português

Este é um MVP (Minimum Viable Product) para análise de sentimentos em textos em português, utilizando FastAPI no backend e React no frontend.

## Visão Geral

### Arquitetura

O sistema segue uma arquitetura moderna com separação clara de responsabilidades:

- **Frontend**: React com Vite, responsável pela interface do usuário
- **Backend**: FastAPI com Python, responsável pelo processamento e integração com IA
- **IA**: Modelos especializados em português com fallback inteligente

### Decisão Local vs Externa

**Processamento Local**:
- Vantagem: Não depende de internet ou APIs externas
- Vantagem: Maior privacidade dos dados
- Vantagem: Custo zero após implantação
- Desvantagem: Requer mais recursos computacionais

**Processamento Externo (Hugging Face)**:
- Vantagem: Modelos mais poderosos e atualizados
- Vantagem: Menor consumo de recursos localmente
- Desvantagem: Requer conexão com internet
- Desvantagem: Possíveis custos com API em grande escala

**Decisão**: Implementamos ambos os modos com fallback automático, priorizando a disponibilidade do serviço.

## Como Executar  

### Pré-requisitos  
- Python 3.10+  
- Node.js 16+  

### Backend  
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend  
```bash
cd frontend
npm install
npm run dev
```

---
## Exemplos de Requisição  

### Via cURL  
**Requisição:**  
```bash
curl -X POST "http://localhost:8000/api/v1/analisar"   -H "Content-Type: application/json"   -d '{
    "tarefa": "sentimento",
    "texto_entrada": "Adorei este produto! Funciona perfeitamente.",
    "usar_externo": false,
    "opcoes": {"idioma": "pt"}
  }'
```  

**Resposta:**  
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "tarefa": "sentimento",
  "motor": "local:pysentimento/roberta-base-pt",
  "resultado": {
    "rotulo": "POSITIVO",
    "pontuacao": 0.9567
  },
  "tempo_ms": 120,
  "recebido_em": "2024-01-15T12:34:56Z"
}
```  

### Via HTTPie  
```bash
http POST http://localhost:8000/api/v1/analisar   tarefa="sentimento"   texto_entrada="Que serviço péssimo, nunca mais compro aqui."   usar_externo:=false   opcoes:='{"idioma": "pt"}'
```  

### Via Postman  
- **Método**: POST  
- **URL**: `http://localhost:8000/api/v1/analisar`  
- **Headers**: `Content-Type: application/json`  
- **Body (raw JSON):**  
```json
{
  "tarefa": "sentimento",
  "texto_entrada": "O produto é razoável, mas poderia ser melhor.",
  "usar_externo": true,
  "opcoes": {"idioma": "pt"}
}
```  

---

## Endpoints da API  

### Analisar texto  
```bash
curl -X POST "http://localhost:8000/api/v1/analisar"   -H "Content-Type: application/json"   -d '{
    "tarefa": "sentimento",
    "texto_entrada": "Adorei este produto!",
    "usar_externo": false,
    "opcoes": {"idioma": "pt"}
  }'
```

### Health check  
```bash
curl http://localhost:8000/api/v1/healthz
```

---

## Tecnologias  
- **Backend:** FastAPI, Pydantic, Transformers, Hugging Face  
- **Frontend:** React, Vite, Axios  
- **IA:** Modelos especializados em português com fallback  

---

## Exemplos  
| Texto                 | Sentimento | Confiança |
|------------------------|------------|-----------|
| "Adorei este produto!" | POSITIVO   | 95.6%     |
| "Que serviço péssimo"  | NEGATIVO   | 92.3%     |
| "Chegou no prazo"      | NEUTRO     | 78.9%     |

---

## URLs  
- Frontend: [http://localhost:3000](http://localhost:3000)  
- Backend: [http://localhost:8000](http://localhost:8000)  
- Docs API: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)  
