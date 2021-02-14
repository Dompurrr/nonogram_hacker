# nonogram_hacker
Python app, that visually solves nonograms/griddlers.
#Input and output
All input data should be in the same folder with main.py program, in file, named "input.txt"
and output data will be be in comand line and will be duplicated in the same folder, in file, named "output.txt"
## Input structure
first line - size of field (n m), where n - quantity of lines, m - quantity of columns
next n lines - numbers on the left side (for rows)
next m lines - numbers on top (for columns)
numbers for row/column are separated by space
New row/column - new line in input file
### Example
```
9 9
2 2
4 4
9
9
9
7
5
3
1
4
6
7
7
7
7
7
6
4
```
This input will correspond nonogram, that looks like that:
<p align="center"><img src="https://upload.wikimedia.org/wikipedia/ru/8/87/Step1.png" width="30%" height="20%"></p>
