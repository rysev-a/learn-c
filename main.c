#include <stdio.h>
#include "library/math.c"
#include "library/write_to_file.c"

int main(int argc, char *argv[]) {
    int a = 10;
    int b = 20;

    int command;
    sscanf(argv[1], "%d", &command);

    char buffer[100]; // Create a character array (string) to hold the result

    if (command == 1) {
        snprintf(buffer, sizeof(buffer), "%d\n", math_sum(a, b));
        printf("%s\n", buffer);
        write_result_to_file(buffer);

        return 0;
    }

    if (command == 2) {
        snprintf(buffer, sizeof(buffer), "%d\n", math_multiply(a, b));
        printf("%s\n", buffer);
        write_result_to_file(buffer);

        return 0;
    }

    write_result_to_file("Unknown command\n");

    return 0;
}