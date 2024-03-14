#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
      
      if (w <= 0 || h <= 0) { 
        new Rectangle()
        // [this.width, this.height] = [w, h]; 
      } else{
        this.width = w
        this.height = h
      }
    }
  
    print () {
      // console.log("Xfgjl;fghjk");
      for (let i = 0; i < this.height; i++) {
        let shape = ""
        for (let j = 0; j < this.width; j++) {
          shape += "X";
        }
        console.log(shape)
      }

      console.log()
    }
  };