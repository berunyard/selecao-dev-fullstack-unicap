import axios from 'axios';

const URL_BASE_API = 'http://localhost:8000';

const api = axios.create({
  baseURL: URL_BASE_API,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const analisarTexto = async (texto, usarExterno = false) => {
  try {
    const resposta = await api.post('/api/v1/analisar', {
      tarefa: 'sentimento',
      texto_entrada: texto,
      usar_externo: usarExterno,
      opcoes: { idioma: 'pt' }
    });
    return resposta.data;
  } catch (erro) {
    throw new Error(erro.response?.data?.detail || 'Falha na análise');
  }
};

export const verificarSaude = async () => {
  try {
    const resposta = await api.get('/api/v1/healthz');
    return resposta.data;
  } catch (erro) {
    throw new Error('Backend não está disponível');
  }
};