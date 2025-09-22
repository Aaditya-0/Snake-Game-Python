# Snake Game

A classic Snake Game implemented in Python using Pygame.

## Features

- Player controls the snake using arrow keys
- Eat food to grow longer
- Game ends on collision with wall or self
- Score tracking
- Start and game over screens
- Custom graphics for snake, food, and background

## Configuration

The snake's size, grid size, and speed are configurable in the code.  
To change these settings, open `src/main.py` and modify the following variables in the `__init__` method of the `SnakeGame` class:

```python
self.BLOCK_SIZE = 30        # Size of each block (snake and food)
self.GRID_WIDTH = 20        # Number of blocks horizontally
self.GRID_HEIGHT = 20       # Number of blocks vertically
# To change speed, adjust the value in self.clock.tick(10) in the run() method
```

For example, to make the snake move faster, increase the value in `self.clock.tick(10)` (higher value = slower game, lower value = faster game) as it changes the tick speed.

## Project Structure

```
requirements.txt

src/
    main.py
    resources/
        block.png
        food.jpeg
        snake.png
```

- `src/main.py`: Main game logic and entry point
- `src/resources/`: Game images (snake, food, background)

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) (see `requirements.txt`)

## Installation

1. Clone this repository or download the source code.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Ensure the images (`snake.png`, `block.png`, `food.jpeg`) are present in `src/resources/`.

## How to Play

1. Run the game:
    ```sh
    python src/main.py
    ```
2. Press any key to start.
3. Use the arrow keys to control the snake.
4. Eat food to grow and increase your score.
5. Avoid colliding with the walls or yourself.
6. After game over, press any key to play again.

## Credits

- Developed using Python and Pygame
- Custom images for snake, food, and background

## License

This project is for educational purposes.