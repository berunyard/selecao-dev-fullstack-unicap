import React from 'react';

const Carregando = () => {
  return (
    <div className="carregando">
      <div className="spinner"></div>
      <p>Analisando sentimento...</p>
      <style jsx>{`
        .carregando {
          display: flex;
          flex-direction: column;
          align-items: center;
          padding: 2rem;
        }
        .spinner {
          width: 40px;
          height: 40px;
          border: 4px solid #f3f3f3;
          border-top: 4px solid #007bff;
          border-radius: 50%;
          animation: spin 1s linear infinite;
        }
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        p {
          margin-top: 1rem;
          color: #666;
        }
      `}</style>
    </div>
  );
};

export default Carregando;