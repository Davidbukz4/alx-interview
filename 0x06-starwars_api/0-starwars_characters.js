#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, resp, body) => {
  if (error) console.log(error);
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (error, resp, body) => {
      if (error) console.log(error);
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
