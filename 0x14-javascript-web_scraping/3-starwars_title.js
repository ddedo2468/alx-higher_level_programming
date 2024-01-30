#!/usr/bin/node

const request = require('request');

const epNum = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${epNum}`;

request(URL, function(err, res, body) {

  if (err) throw err;

  if (res.statusCode === 200) {
    const resJson = JSON.parse(body);
    console.log(resJson.title)
  }
})
