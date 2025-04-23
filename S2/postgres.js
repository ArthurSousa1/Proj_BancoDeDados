const { Client } = require('pg');

// Configurações de conexão
const client = new Client({
  user: 'seu_usuario',
  host: 'localhost',
  database: 'seu_banco',
  password: 'sua_senha',
  port: 5432, // porta padrão do PostgreSQL
});

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
