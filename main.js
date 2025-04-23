const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


class main {
    
    startProject() {
        rl.question('\nAntes de começarmos, nos informe qual sua área: \n1 para vendedor \n2 para cliente \n9 para sair\n', (answer) => {
            if (answer === '1') {
                this.sellerFlow();
            } else if (answer === '2') {
                this.customerFlow();
            } else if (answer === '9') {
                rl.close();
            } else {
                console.log('Área inválida, por favor tente novamente \n');
                return this.startProject();
            }
        });
    }

    sellerFlow() {
        console.log('\nÓtimo, bem vindo vendedor!');
        console.log('Selecione o que deseja fazer');
        rl.question('1 para consultar estoque \n2 para adicionar items ao estoque \n9 para retornar ao menu principal\n', (answer) => {
            if (answer === '1') {
                console.log('Enviar mensagem para consultar estoque \n');
            } else if (answer === '2') {
                console.log('Enviar mensagem para adicionar itens ao estoque \n'); 
            } else if (answer === '9') {
                this.startProject();
            } else {
                console.log('Opção inválida, por favor tente novamente \n');
                return this.sellerFlow();
            }
        });
    }

    customerFlow() {
        console.log('\nÓtimo, bem vindo comprador!');
        console.log('Selecione o que deseja fazer');
        rl.question('1 para consultar estoque \n2 para adicionar items ao carrinho \n3 para realizar um pedido \n4 para consultar últimos pedidos \n9 para retornar ao menu principal\n', (answer) => {
            if (answer === '1') {
                console.log('Enviar mensagem para consultar estoque \n');
            } else if (answer === '2') {
                console.log('Enviar mensagem para adicionar items ao carrinho \n');
            } else if (answer === '3') {
                console.log('Enviar mensagem para realizar um pedido \n');
            } else if (answer === '4') {
                console.log('Enviar mensagem para consultar últimos pedidos \n'); 
            } else if (answer === '9') {
                this.startProject();
            } else {
                console.log('Opção inválida, por favor tente novamente \n');
                return this.customerFlow();
            }
        });
    }
}

const MAIN = new main
MAIN.startProject();
