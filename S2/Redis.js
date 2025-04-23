// index.js (com CommonJS e função async)
const { createClient } = require('redis');
const express = require('express');

async function main() {
  const client = createClient({
    username: 'default',
    password: 'jzXQ3bYSEd12khkblAXBxIvhRgflqXTn',
    socket: {
      host: 'redis-11658.crce196.sa-east-1-2.ec2.redns.redis-cloud.com',
      port: 11658
    }
  });

  client.on('error', err => console.log('Redis Client Error', err));

  await client.connect();

  await client.set('foo', 'bar');
  const result = await client.get('foo');
  console.log(result);  // >>> bar
}

main();  // Chama a função assíncrona
