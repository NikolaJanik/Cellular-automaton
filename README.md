# Game of life

General rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproductio

Requirements:
 - python
 - numpy
 - pygame

To start the game type:
  python gameOfLife.py

When the application's window appears, you can choose starting conditions
using left click of your mouse to activate cells (remeber about basic rules).
Start the game with 'space' on the keyboard. You can also stop the game with
'space' and activate chosen cells. You are able to activate cells when
the game is running.
