#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response && response.statusCode === 200) {
      // Write the response body to the specified file
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error('Error writing to file:', err);
        } else {
          console.log('File saved successfully:', filePath);
        }
      });
    } else {
      console.error('Error: Unexpected status code:', response ? response.statusCode : 'Unknown');
    }
  }
});
