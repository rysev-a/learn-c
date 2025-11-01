#include <stdio.h>
#include <string.h>
#include "library/math.c"
#include "library/write_to_file.c"

int main(int argc, char *argv[]) {

    char command[50];
    int a, b;
    sscanf(argv[1], "%s", command);

    // buffer for write in result file
    char buffer[100];

    if (strcmp(command, "sum") == 0) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_sum(a, b));
        write_result_to_file(buffer);

        return 0;
    }

    if (strcmp(command, "multiply") == 0) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_multiply(a, b));
        write_result_to_file(buffer);

        return 0;
    }


    if (strcmp(command, "quotient") == 0) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_get_quotient(a, b));
        write_result_to_file(buffer);

        return 0;
    }

    if (strcmp(command, "remainder") == 0) {
        sscanf(argv[2], "%d", &a);
        sscanf(argv[3], "%d", &b);

        snprintf(buffer, sizeof(buffer), "%d\n", math_get_remainder(a, b));
        write_result_to_file(buffer);

        return 0;
    }

    if (strcmp(command, "ascii") == 0) {
        char e;
        sscanf(argv[2], "%c", &e);
        snprintf(buffer, sizeof(buffer), "ASCII-code %c=%d\n" , e , e);
        write_result_to_file(buffer);
        return 0;
    }

    write_result_to_file("Unknown command\n");
    return 0;
}