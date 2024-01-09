#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (this.isValidNumber(w) && this.isValidNumber(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  isValidNumber (value) {
    return typeof value === 'number' && Number.isInteger(value);
  }

  print () {
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
