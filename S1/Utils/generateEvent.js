const {faker} = require('@faker-js/faker');

const tipos = ['entrada', 'saida'];

const generateEvent = () => ({
    produtoId: faker.string.uuid(),
    tipoMovimentacao: faker.helpers.arrayElement(tipos),
    quantidade: faker.number.int({min: 1, max: 100}),
    local: faker.location.city(),
    timestamp: new Date().toISOString()
});

module.exports = generateEvent;