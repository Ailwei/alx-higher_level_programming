#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code:', response.statusCode);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;
    const promises = charactersUrls.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        });
      });
    });

    Promise.all(promises)
      .then(characters => {
        characters.forEach(character => console.log(character));
      })
      .catch(error => {
        console.error('Error:', error);
      });
  } catch (error) {
    console.error('Error parsing movie data:', error);
  }
});
