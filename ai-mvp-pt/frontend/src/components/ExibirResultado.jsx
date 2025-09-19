import React from 'react';

const ExibirResultado = ({ resultado }) => {
  const obterCorSentimento = (rotulo) => {
    switch (rotulo?.toUpperCase()) {
      case 'POSITIVO':
        return '#28a745';
      case 'NEGATIVO':
        return '#dc3545';
      case 'NEUTRO':
        return '#ffc107';
      default:
        return '#6c757d';
    }
  };

  const formatarPontuacao = (pontuacao) => {
    return (pontuacao * 100).toFixed(1);
  };

  return (
    <div className="resultado">
      <h3>Resultado da Análise</h3>
      <div className="cartao-sentimento">
        <div 
          className="badge-sentimento"
          style={{ backgroundColor: obterCorSentimento(resultado.rotulo) }}
        >
          {resultado.rotulo}
        </div>
        <div className="pontuacao">
          Confiança: {formatarPontuacao(resultado.pontuacao)}%
        </div>
      </div>
      <style jsx>{`
        .resultado {
          margin-top: 2rem;
          padding: 1.5rem;
          border: 1px solid #ddd;
          border-radius: 8px;
          background: #f8f9fa;
        }
        h3 {
          margin: 0 0 1rem 0;
          color: #333;
        }
        .cartao-sentimento {
          display: flex;
          align-items: center;
          gap: 1rem;
        }
        .badge-sentimento {
          padding: 0.5rem 1rem;
          color: white;
          border-radius: 20px;
          font-weight: bold;
          text-transform: uppercase;
          font-size: 0.9rem;
        }
        .pontuacao {
          color: #666;
          font-size: 0.9rem;
        }
      `}</style>
    </div>
  );
};

export default ExibirResultado;