# Project `tetris-optimizer`

The project is a program that takes a list of <a href="https://en.wikipedia.org/wiki/Tetromino" target=blank>tetrominoes</a> from a text file and assembles them to create the smallest possible square.

The program also additionally implements the **--color** flag, when used, the tetrominoes are painted in the colors of the classic game <a href="https://en.wikipedia.org/wiki/Tetris" target=blank>Tetris</a>.

## Description

The program:

* Compiles successfully
* Collects all the tetrominoes to form the least square
* Defines each tetrominoe in the solution by printing them in capital letters (first `A`, second `B`, and so on)
* Has the ability to color tetrominoes using the **--color** flag
* Expects at least one tetrominoe in a text file
* In case of incorrect tetromino format or incorrect file format, prints `ERROR`
* The project is written in **Python**

## Usage

```
$ cat sample.txt
...#
...#
...#
...#

....
....
....
####

.###
...#
....
....

....
..##
.##.
....
```
```
$ python3 main.py sample.txt
A B B B B
A C C C .
A . . C .
A D D . .
D D . . .
```
```
$ python3 main.py sample.txt --color
```
![Текст с описанием картинки](/images/colored.jpg)

### How to install

```
git clone git@git.github.com:grenkoff/tetris-optimizer.git && cd tetris-optimizer/
```

### How to go run

```
go run . [FILE] [--color]
```

## Autor

* Follow me on <a href="https://github.com/grenkoff">GitHub.com/grenkoff</a>