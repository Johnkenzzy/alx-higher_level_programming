#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || w <= 0 || !h || h <= 0) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
