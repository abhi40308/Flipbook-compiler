# Flipbook-compiler
Compiler for building flipbook, written in python.   

Note: This repo contains my attempt to build a compiler using python, for a language called `flip` used to create flipbooks (see below for language description). Currently only `lexer`, `parser` and `AST` are implemented. The code generator is yet to be implemented using `llvmlite` (LLVM-Python binding), yet the code is usable to create a flipbook.

## npm packages
[rply](https://pypi.org/project/rply/)  
[llvmlite](https://pypi.org/project/llvmlite/0.4.0/)  
[fpdf](https://pypi.org/project/fpdf/)  
[PyPDF2](https://pypi.org/project/PyPDF2/)

## Sample `flip` language
`print ( total (10) position(0,0) scale (5,1,10) move (10,5,1,10) image1.png dimensions (50,50) )`  
`print ( total (10) position(0,0) scale (5,1,10) move (10,5,1,10) images.jpeg dimensions (50,50) )`  
  
  
##### Keywords:  

`total(x)` = total number of pages which contains image   
`position(x,y)` = initial position coordinates of image from top-left  
`scale(num,i,j)` = increase the dimensions(height, width) of image by `num` user units, for every page in `range(i,j)`  
`move(x,y,i,j)` = move the image by `x` user units on x-axis, `y` user units on y-axis on every page in `range(i,j)`  
`imagefile` = lexer supports `jpg|png|gif|bmp|jpeg` image formats  
`dimensions(h,w)`= initial dimensions of image in user units



## Sample run

* Define your input in `input.flip` file, written in `flip` language.
* Run `main.py`
  
##### Output: 
![demo](demo.gif)
