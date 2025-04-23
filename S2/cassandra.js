const cassandra = require('cassandra-driver');

// Criação do cliente
const client = new cassandra.Client({
  contactPoints: ['127.0.0.1'], // IP do seu Cassandra
  localDataCenter: 'datacenter1', // nome do seu data center (padrão: datacenter1)
  keyspace: 'meu_keyspace' // seu keyspace (como se fosse um banco de dados)
});

// Função principal
async function executar() {
  try {
    // Conectar
    await client.connect();
    console.log('Conectado ao Cassandra!');

    // Criar tabela (se não existir)
    const criarTabela = `
      CREATE TABLE IF NOT EXISTS usuarios (
        id UUID PRIMARY KEY,
        nome text,
        idade int
      );
    `;
    await client.execute(criarTabela);

    // Inserir um usuário
    const query = 'INSERT INTO usuarios (id, nome, idade) VALUES (uuid(), ?, ?)';
    const params = ['Ana', 28];
    await client.execute(query, params, { prepare: true });

    console.log('Usuário inserido com sucesso!');
  } catch (err) {
    console.error('Erro:', err);
  } finally {
    await client.shutdown();
  }
}

executar();
