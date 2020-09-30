# Simple Snake Game
## Overview
In this project, I wrote a simple snake game in python, using the *pyGame* module.

The snake game runs on a 500 by 500 window, and includes feautues such as:
- Apple eating
- Snake size increasing when eating apples
- Score counter
- Game ending when snake runs into itself

## Game Flow
the game is played using the up, down, right, and left arrow keys.

simply control the snake's direction using these keys and play along

## Code Design

The code was designed with a main objective of it being readable, open to changes, and compact.
The basic class design is as follows:

- **SnakeGame**
  the main game class, which is responsible for initializing and running the game.
  
- **GameGrid**
  the object which holds and manages all of the game objects such as *Snake* and *Apple*.
  
- **GameObject**
  An abstract class which is implemented by any game "object", an object in the game which has dynamic characteristics and is diplayed on the screen (such as *Snake* and *Apple*).
  
- **Snake, Apple, Counter, Block**
  GameObjects, each object has a class implementing *GameObject*, with *Apple* inheriting from *Block*, and *Snake* containing a list of *Blocks*
