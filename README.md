# XOX BINARY
Tic-Tac-Toe with bitwise operators.

I was bored... And I realized that I had never done tic-tac-toe before. TADA 🎉

If you see any problem open new [issue](https://github.com/DazzGranto/tic-tac-toe-binary/issues).

## How to play

Just type indexes

```
123     ---
456 ->  --- -> GRID
789     ---
```

## Logic

```
! (BINARY)
> For grid I used 18 bit (Please let me know if you think you can do better.)
> 9 for O and 9 for X positions

GRID = 000000000_000000000

> First 9 bit for X

-O-         000 010
OX-   ->    010 100   ->  0b000_010_101_010_100_010
XOX         101 010

WIN CASES:

XXX X-- X--
--- X-- -X-
--- X-- --X

--- -X-		->	111 000 000 - 000 000 000 \ 100 100 100 - 000 000 000 \ 100 010 001 - 000 000 000
XXX -X-		bin	000 111 100 - 000 000 000 \ 010 010 010 - 000 000 000
--- -X-		->	000 000 111 - 000 000 000 \ 001 001 001 - 000 000 000 \ 001 010 100 - 000 000 000

--- --X --X
--- --X -X-
XXX --X X--

ADD PLAYER TO POSITION AND IS POSITION EMPTY:
  
  ADD X OR O:
    > I used bitwise OR (|)
    
    010 | 001 == 011
    000 | 100 == 100
    011 | 010 == 011
    
  IS POSITON EMPTY:
  > I used bitwise AND (&)
    GRID = 001
    
    GRID & 001 == 001
    GRID & 100 == 000
    011  & 010 == 010
```

