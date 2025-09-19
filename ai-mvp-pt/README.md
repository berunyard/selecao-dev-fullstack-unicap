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
- pip (gerenciador de pacotes Python)
- npm (gerenciador de pacotes Node)

### Backend

1. Navegue até a pasta do backend:
