#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code ' + response.statusCode);
  } else {
    try {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;
      charactersUrls.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            try {
              const characterData = JSON.parse(body);
              console.log(characterData.name);
            } catch (error) {
              console.error('Error parsing character data:', error);
            }
          }
        });
      });
    } catch (error) {
      console.error('Error parsing movie data:', error);
    }
  }
});
