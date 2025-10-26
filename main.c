#include <stdio.h>
#include "library/math.c"
#include "library/write_to_file.c"

int main(int argc, char *argv[]) {
    int command, a, b;
    sscanf(argv[1], "%d", &command);

    char buffer[100]; // Create a character array (string) to hold the result

    if (command == 1) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_sum(a, b));
        write_result_to_file(buffer);

        return 0;
    }

    if (command == 2) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_multiply(a, b));
        write_result_to_file(buffer);

        return 0;
    }

    if (command == 3) {
        char e;
        sscanf(argv[2], "%c", &e);
        snprintf(buffer, sizeof(buffer), "ASCII-code %c=%d\n" , e , e);
        write_result_to_file(buffer);
        return 0;
    }

    if (command == 4) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_get_quotient(a, b));
        write_result_to_file(buffer);

        return 0;
    }

    if (command == 5) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_get_remainder(a, b));
        write_result_to_file(buffer);

        return 0;
    }

    write_result_to_file("Unknown command\n");
    return 0;
}