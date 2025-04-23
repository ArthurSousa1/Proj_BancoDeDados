const { Client } = require('pg');

// Configurações de conexão
const client = new Client("postgresql://arthur-sousa:P9ClrcZsNNk0t_D2Ff38dg@projeto-banco-de-dados-14602.7tt.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full");

// Conectando ao banco
client.connect()
  .then(() => {
    console.log('Conectado ao PostgreSQL!');

    // Criando tabela (se não existir)
    return client.query(`
      CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100),
        idade INT
      );
    `);
  })
  .then(() => {
    // Inserindo um usuário
    return client.query(
      'INSERT INTO usuarios (nome, idade) VALUES ($1, $2) RETURNING *',
      ['Ana', 28]
    );
  })
  .then(res => {
    console.log('Usuário inserido:', res.rows[0]);
  })
  .catch(err => console.error('Erro:', err))
  .finally(() => client.end());
