# Projeto de banco de dados (FEI 1º semestre - 2025) 🚀

Nosso projeto é divido em 3 pilares, S1, S2 e S3. O S1 é responsável por gerar dados, e enviando esses dados para S2 por meio de uma mensageria, que no caso escolhida foi Apache Kafka. Já o S2 é responsável por receber as mensagens enviadas por S1 e armazena-las em seus respectivos bancos (relacionais e não-relacionais). E para finalizar o S3 é responsável por observar todas as mensagens enviadas pelo mensageria e registrar essas mensagens no ElasticSearch.

## Configuração inicial 🛠️
Instale todas as dependências do projeto, para isso acesse a pasta do projeto pelo terminal ou pelo command prompt e rode os seguintes comandos:

```
pip install 'elasticsearch<9' #Framework para o uso do ElasticSearch no S3
```
```
pip install 'confluent-kafka' #Framework para o uso do Apache Kafka, usado em todos os módulos 
```
```
pip install 'kafka-python' #Framework para o uso do Apache Kafka, usado em todos os módulos
```
```
pip install 'psycopg2-binary' #Framework para o uso do Cockroach atraves 
```
```
pip install 'pymongo' #Framework para o uso do MongoDB
```
```
pip install 'redis' #Framework para o uso do RedisDB
```

Após a instação de todos os packages temos que configurar o docker, para isso baixe o docker em sua máquina através [dessa URL](https://www.docker.com/products/docker-desktop/), retorne a pasta do projeto e rode o seguinte comando:
```
docker-compose up -d #Esse comando serve para configurar todo o ambiente local em sua máquina
```

## Entendendo o projeto
Agora com o projeto configurado e pronto para ser executado, vamos entender como o projeto é construído. Todos os módulos foram criados em MVC (Model, View, Controller). A view é responsável por toda a intereção com o cliente, seja ele uma pessoa ou outro serviço. A controller é responsável por todas as regras de negócio e lógica dos módulos, podendo ser uma simples classe (Como em S1) ou então ser dividia em várias Controllers (Como o caso de S2). E a model é responsável por gerenciar os dados dos módulos.<br>

Todo o projeto é testado através do terminal (Pode ser usado o banco de dados caso tenha acesso). Para que seja possível a interação com S2 e S3 é necessário inicial via terminal suas views, então para isso abra 3 janelas do terminal, uma dentro do S1, outra dentro de S2 e outra dentro de S3. Como o exemplo:

<img width="2055" alt="Screenshot 2025-05-23 at 19 58 31" src="https://github.com/user-attachments/assets/9dd5d1ab-cbdc-4b0e-9b64-18b0bc4a0451" />

E agora para iniciar as views rode primeiro em S3 o comando python view.py, depois o mesmo comando em S2 e depois o mesmo comando em S1. E pronto, o seu projeto estará rodando.
