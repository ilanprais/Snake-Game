# Snake-Game
## Basic Requirements
A simple snake game. the snake moves on a 2x by 3x grid, and apples appear.
the snakes head moves with arrow press. when the snake head reaches an apple the snakes length is increased by 1.
If the snake touches itself the plater loses.

**optional:**
- keep high score
- menu and end screen
- multiplayer

## Design

- Window (frame and attributes) displaying:
- Game grid (each cell is the size of a block and an apple)
- Snake:
  - Block(s)
- Apples
- Score

### GameObject Interface
- doOneFrame()

### GameGrid Interface implement Displayable
- members:
  - height
  - width
  - pixels (array of rgb color values)
  - list of GameObjects
- functions:
  - doOneFrame()
  - display(Gui window)
  - add(GameObject)

### Displayable Interface
- display()

### Game Interface
- create()
- run()
- close()

### SnakeGame implemets Game
- in interface

### Block implements GameObject
- members:
   - x
   - y
   - color
- functions:
  - setLocation(x, y)
  - in interface

### Snake implemets GameObject
- members:
  - list of Blocks (index 0 head index size-1 tail)
  - color
  - head direction
  - turn location (the location where the head direction was changed, starts at null)
- functions:
  - in interface
  
  ### SnakeGameGrid implements GameGrid
  - in interface




