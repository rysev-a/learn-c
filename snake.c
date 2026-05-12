#include <ncurses.h>
#include <stdlib.h>
#include <time.h>


int x;
int y;

int dx;
int dy;

int screen_width;
int screen_height;
int apple_x;
int apple_y;

void reset_apple() {
    apple_x = rand() % screen_width;
    apple_y = rand() % screen_height;
}

int main() {

    srand(time(NULL));
    initscr();

    int *snake_array_x = malloc(screen_width * screen_height * sizeof(int));
    int *snake_array_y = malloc(screen_width * screen_height * sizeof(int));

    int snake_length = 1;

    halfdelay(2);

    x = 0;
    y = 0;
    dx = 0;
    dy = 0;

    getmaxyx(stdscr, screen_height, screen_width);
    char key_symbol = '0';

    reset_apple();

    while (1) {
        char* key_string = malloc(2);
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

        x = x + dx;
        y = y + dy;

        if (x == apple_x && y == apple_y) {
            reset_apple();
        }
        erase();
        mvaddstr(10, 10, key_string);
        mvaddstr(y, x, "x");
        mvaddstr(apple_y, apple_x, "0");

        key_symbol = getch();
    }

    endwin();
}
