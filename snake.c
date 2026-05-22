#include <ncurses.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int head_x;
int head_y;

int snake_length;

int dx;
int dy;

int head_position;
int tail_position;

int screen_width;
int screen_height;
int apple_x;
int apple_y;

int game_over = 0;

void reset_apple() {
  apple_x = rand() % screen_width - 3;
  apple_y = rand() % screen_height - 3;

  if (apple_x < 0)
    apple_x = 2;
  if (apple_y < 0)
    apple_y = 2;
}

void draw_borders(int width, int height) {
  for (int i = 0; i < width; i++) {
    mvaddstr(0, i, "-");
    mvaddstr(height - 1, i, "-");
  }
  for (int i = 0; i < height; i++) {
    mvaddstr(i, 0, "|");
    mvaddstr(i, width - 1, "|");
  }
}

int main() {
  srand(time(NULL));
  initscr();

  getmaxyx(stdscr, screen_height, screen_width);


  int stack_size = screen_width * screen_height;

  int *snake_array_x = malloc(screen_width * screen_height * sizeof(int));
  int *snake_array_y = malloc(screen_width * screen_height * sizeof(int));

  snake_length = 20;
  head_position = snake_length - 1;


  for (int i = 0; i < snake_length; i++) {
      snake_array_x[i] = i + 1;
      snake_array_y[i] = 2;
  }


  halfdelay(2);

  dx = 0;
  dy = 0;

  char key_symbol = '0';
  reset_apple();

  while (!game_over) {
    char *key_string = malloc(2);
    key_string[0] = key_symbol;
    key_string[1] = '\0';

    switch (key_symbol) {
    case 'w':
      dy = -1;
      dx = 0;
      break;
    case 's':
      dy = 1;
      dx = 0;
      break;
    case 'a':
      dx = -1;
      dy = 0;
      break;
    case 'd':
      dx = 1;
      dy = 0;
      break;
    }

    if (dx != 0 || dy != 0) {

      // move snake
      head_x = snake_array_x[head_position];
      head_y = snake_array_y[head_position];

      head_x = head_x + dx;
      head_y = head_y + dy;

      if (head_x == 0)
        head_x = screen_width - 2;
      if (head_y == 0)
        head_y = screen_height - 2;
      if (head_x == screen_width - 1)
        head_x = 1;
      if (head_y == screen_height - 1)
        head_y = 1;

      // check game over
      for (int i = 3; i < snake_length; i++) {
        int check_index = (head_position - i + stack_size) % stack_size;
        if (head_x == snake_array_x[check_index] &&
            head_y == snake_array_y[check_index]) {
          erase();
          game_over = 1;
        }
      }

      head_position++;
      snake_array_x[head_position] = head_x;
      snake_array_y[head_position] = head_y;

      // reset apple
      if (head_x == apple_x && head_y == apple_y) {
        reset_apple();
        snake_length++;
      }
    }

    // draw
    erase();
    for (int i = 0; i < snake_length; i++) {
      int draw_index = (head_position - i + stack_size) % stack_size;
      mvaddstr(snake_array_y[draw_index], snake_array_x[draw_index], "x");
    }
    mvaddstr(apple_y, apple_x, "0");
    draw_borders(screen_width, screen_height);

    key_symbol = getch();
  }

  mvaddstr(screen_height / 2, screen_width / 2 - 5, "Game Over");
  halfdelay(20);
  key_symbol = getch();

  endwin();
}
