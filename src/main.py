import pygame as pg
import random


class SnakeGame:
    def __init__(self):
        pg.init()
        self.BLOCK_SIZE = 30
        self.GRID_WIDTH = 20
        self.GRID_HEIGHT = 20
        self.SCREEN_WIDTH = self.BLOCK_SIZE * self.GRID_WIDTH
        self.SCREEN_HEIGHT = self.BLOCK_SIZE * self.GRID_HEIGHT

        self.snake_img = pg.image.load(r"C:\Users\singh\Desktop\snake game\src\resources\snake.png")
        self.snake_img = pg.transform.scale(self.snake_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.background_img = pg.image.load(r"C:\Users\singh\Desktop\snake game\src\resources\block.png")
        self.background_img = pg.transform.scale(self.background_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.food_img = pg.image.load(r"C:\Users\singh\Desktop\snake game\src\resources\food.jpeg")
        self.food_img = pg.transform.scale(self.food_img, (self.BLOCK_SIZE, self.BLOCK_SIZE))

        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption("Snake Game")
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 36)

    def draw_background(self):
        for x in range(self.GRID_WIDTH):
            for y in range(self.GRID_HEIGHT):
                self.screen.blit(self.background_img, (x * self.BLOCK_SIZE, y * self.BLOCK_SIZE))

    def draw_snake(self, snake):
        for pos in snake:
            self.screen.blit(self.snake_img, (pos[0] * self.BLOCK_SIZE, pos[1] * self.BLOCK_SIZE))

    def draw_food(self, food_pos):
        self.screen.blit(self.food_img, (food_pos[0] * self.BLOCK_SIZE, food_pos[1] * self.BLOCK_SIZE))

    def random_food(self, snake):
        while True:
            pos = (random.randint(0, self.GRID_WIDTH - 1), random.randint(0, self.GRID_HEIGHT - 1))
            if pos not in snake:
                return pos

    def show_game_over(self, score):
        self.screen.fill((0, 0, 0))
        game_over_text = self.font.render("Game Over!", True, (255, 0, 0))
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        restart_text = self.font.render("Press any key to play again", True, (200, 200, 200))
        self.screen.blit(game_over_text, (self.SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 70))
        self.screen.blit(score_text, (self.SCREEN_WIDTH // 2 - score_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 10))
        self.screen.blit(restart_text, (self.SCREEN_WIDTH // 2 - restart_text.get_width() // 2, self.SCREEN_HEIGHT // 2 + 50))
        pg.display.flip()
        self.wait_for_key()

    def show_start_screen(self):
        self.screen.fill((0, 0, 0))
        title_text = self.font.render("Snake Game", True, (0, 255, 0))
        start_text = self.font.render("Press any key to start", True, (200, 200, 200))
        self.screen.blit(title_text, (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(start_text, (self.SCREEN_WIDTH // 2 - start_text.get_width() // 2, self.SCREEN_HEIGHT // 2 + 10))
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                elif event.type == pg.KEYDOWN:
                    waiting = False

    def run(self):
        snake = [(self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2)]
        direction = (0, -1)  
        food = self.random_food(snake)
        score = 0
        running = True

        while running:
            self.clock.tick(10)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                elif event.type == pg.KEYDOWN: 
                    if event.key == pg.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pg.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pg.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pg.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)

            # Move snake
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # Check collisions
            if (
                new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
                new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT or
                new_head in snake
            ):
                self.show_game_over(score)
                running = False
                break

            snake.insert(0, new_head)

            # Check food
            if new_head == food:
                score += 1
                food = self.random_food(snake)
            else:
                snake.pop()

            # Draw everything
            self.draw_background()
            self.draw_snake(snake)
            self.draw_food(food)
            pg.display.flip()

if __name__ == "__main__":
    game = SnakeGame()
    while True:
        game.show_start_screen()
        game.run()