import React, { useState } from 'react';
import { analisarTexto } from '../services/api';
import Carregando from './Carregando';
import ExibirResultado from './ExibirResultado';

const Analisador = () => {
  const [texto, setTexto] = useState('');
  const [usarExterno, setUsarExterno] = useState(false);
  const [resultado, setResultado] = useState(null);
  const [carregando, setCarregando] = useState(false);
  const [erro, setErro] = useState('');

  const handleEnviar = async (e) => {
    e.preventDefault();
    if (!texto.trim()) {
      setErro('Por favor, digite algum texto para analisar');
      return;
    }

    setCarregando(true);
    setErro('');
    setResultado(null);

    try {
      const resultadoAnalise = await analisarTexto(texto, usarExterno);
      setResultado(resultadoAnalise.resultado);
    } catch (err) {
      setErro(err.message);
    } finally {
      setCarregando(false);
    }
  };

  return (
    <div className="analisador">
      <h1>MVP de Análise de Sentimentos</h1>
      
      <form onSubmit={handleEnviar} className="formulario-analise">
        <div className="grupo-formulario">
          <label htmlFor="entrada-texto">Digite o texto para análise:</label>
          <textarea
            id="entrada-texto"
            value={texto}
            onChange={(e) => setTexto(e.target.value)}
            placeholder="Digite seu texto aqui..."
            rows={4}
            disabled={carregando}
          />
        </div>

        <div className="grupo-formulario">
          <label className="rotulo-checkbox">
            <input
              type="checkbox"
              checked={usarExterno}
              onChange={(e) => setUsarExterno(e.target.checked)}
              disabled={carregando}
            />
            Usar API externa (Hugging Face)
          </label>
        </div>

        <button 
          type="submit" 
          disabled={carregando || !texto.trim()}
          className="botao-analisar"
        >
          {carregando ? 'Analisando...' : 'Analisar Sentimento'}
        </button>
      </form>

      {erro && (
        <div className="erro">
          <strong>Erro:</strong> {erro}
        </div>
      )}

      {carregando && <Carregando />}

      {resultado && !carregando && <ExibirResultado resultado={resultado} />}

      <style jsx>{`
        .analisador {
          max-width: 600px;
          margin: 0 auto;
          padding: 2rem;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        h1 {
          text-align: center;
          color: #333;
          margin-bottom: 2rem;
        }
        .formulario-analise {
          background: white;
          padding: 2rem;
          border-radius: 8px;
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .grupo-formulario {
          margin-bottom: 1.5rem;
        }
        label {
          display: block;
          margin-bottom: 0.5rem;
          font-weight: 600;
          color: #333;
        }
        textarea {
          width: 100%;
          padding: 0.75rem;
          border: 1px solid #ddd;
          border-radius: 4px;
          font-size: 1rem;
          resize: vertical;
        }
        .rotulo-checkbox {
          display: flex;
          align-items: center;
          font-weight: normal;
        }
        input[type="checkbox"] {
          margin-right: 0.5rem;
        }
        .botao-analisar {
          width: 100%;
          padding: 1rem;
          background: #007bff;
          color: white;
          border: none;
          border-radius: 4px;
          font-size: 1rem;
          cursor: pointer;
          transition: background 0.2s;
        }
        .botao-analisar:hover:not(:disabled) {
          background: #0056b3;
        }
        .botao-analisar:disabled {
          background: #6c757d;
          cursor: not-allowed;
        }
        .erro {
          background: #f8d7da;
          color: #721c24;
          padding: 1rem;
          border-radius: 4px;
          margin-top: 1rem;
          border: 1px solid #f5c6cb;
        }
      `}</style>
    </div>
  );
};

export default Analisador;