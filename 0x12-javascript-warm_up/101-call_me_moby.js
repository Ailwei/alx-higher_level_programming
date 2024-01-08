#!/usr/bin/node

function callMeXTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = { callMeXTimes };
