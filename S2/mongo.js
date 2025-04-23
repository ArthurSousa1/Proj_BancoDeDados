const mongoose = require('mongoose');

// Conectando ao MongoDB
mongoose.connect('mongodb+srv://sousaarthur840:sXFWGkNwWCcpknkq@estoque.djdf0fe.mongodb.net/?retryWrites=true&w=majority&appName=Estoque', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Conectado ao MongoDB!'))
.catch(err => console.error('Erro ao conectar ao MongoDB:', err));

// Definindo um schema
const usuarioSchema = new mongoose.Schema({
  nome: String,
  idade: Number
});

// Criando um modelo
const Usuario = mongoose.model('Usuario', usuarioSchema);

// Criando e salvando um novo usuário
const novoUsuario = new Usuario({ nome: 'Ana', idade: 28 });

novoUsuario.save()
  .then(doc => {
    console.log('Usuário salvo:', doc);
    mongoose.disconnect(); // fecha a conexão
  })
  .catch(err => console.error('Erro ao salvar usuário:', err));
