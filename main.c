#include <stdio.h>
#include <string.h>
#include "library/math.c"
#include "library/strings.c"

// write result to output.txt
#include "library/write_to_file.c"

// use strcspn to remove \n\r symbols


FILE *fptr;

// Open a file in read mode

int main() {
    fptr = fopen("tmp/input.txt", "r");

    int arg_1_int;
    int arg_2_int;
    char arg_1_str[100];
    char arg_2_str[100];

    char command[100];
    char result[100];

    fgets(command, 100, fptr);
    command[strcspn(command, "\r\n")] = 0;

    // read first argument
    char arg_1[100];
    fgets(arg_1, 100, fptr);


    char arg_1_buffer[100];
    int i = 2;

    while (arg_1[i]) {
        if (arg_1[0] == 'd') {
            arg_1_buffer[i - 2] = arg_1[i];
        }

        if (arg_1[0] == 's') {
            arg_1_str[i - 2] = arg_1[i];
        }

        i++;
    }

    if (arg_1[0] == 'd') {
        arg_1_int = atoi(arg_1_buffer);
    } else {
        arg_1_str[strcspn(arg_1_str, "\r\n")] = 0;
    }

    // read second argument
    char arg_2[100];
    fgets(arg_2, 100, fptr);
    char arg_2_buffer[100];
    i = 2;
    while (arg_2[i]) {
        if (arg_2[0] == 'd') {
            arg_2_buffer[i - 2] = arg_2[i];
        }

        if (arg_2[0] == 's') {
            arg_2_str[i - 2] = arg_2[i];
        }

        i++;
    }

    if (arg_2[0] == 'd') {
        arg_2_int = atoi(arg_2_buffer);
    } else {
        arg_2_str[strcspn(arg_2_str, "\r\n")] = 0;
    }

    // math functions
    if (strcmp(command, "sum") == 0) {
        snprintf(result, sizeof(result), "%d\n", math_sum(arg_1_int, arg_2_int));
    }

    if (strcmp(command, "multiply") == 0) {
        snprintf(result, sizeof(result), "%d\n", math_multiply(arg_1_int, arg_2_int));
    }

    if (strcmp(command, "quotient") == 0) {
        snprintf(result, sizeof(result), "%d\n", math_get_quotient(arg_1_int, arg_2_int));
    }

    if (strcmp(command, "remainder") == 0) {
        snprintf(result, sizeof(result), "%d\n", math_get_remainder(arg_1_int, arg_2_int));
    }

    // string functions
    if (strcmp(command, "length") == 0) {
        snprintf(result, sizeof(result), "%d\n", get_string_length(arg_1_str));
    }

    if (strcmp(command, "is_substring") == 0) {
        snprintf(result, sizeof(result), "%d\n", is_substring(arg_1_str, arg_2_str));
    }

    if (strcmp(command, "is_beginning") == 0) {
        snprintf(result, sizeof(result), "%d\n", is_beginning(arg_1_str, arg_2_str));
    }

    if (strcmp(command, "is_palindrome") == 0) {
        snprintf(result, sizeof(result), "%d\n", is_palindrome(arg_1_str));
    }

    if (strcmp(command, "is_lower_case") == 0) {
        snprintf(result, sizeof(result), "%d\n", is_lower_case(arg_1_str));
    }

    if (strcmp(command, "is_identifier") == 0) {
        snprintf(result, sizeof(result), "%d\n", is_identifier(arg_1_str));
    }

    if (strcmp(command, "upcase") == 0) {
        upcase(arg_1_str);
        snprintf(result, sizeof(result), "%s\n", arg_1_str);
    }

    if (strcmp(command, "swap_case") == 0) {
        swap_case(arg_1_str);
        snprintf(result, sizeof(result), "%s\n", arg_1_str);
    }

    if (strcmp(command, "reverse") == 0) {
        reverse(arg_1_str);
        snprintf(result, sizeof(result), "%s\n", arg_1_str);
    }

    if (strcmp(command, "duplicate") == 0) {
        char* duplicated = duplicate_string(arg_1_str, arg_2_int);
        snprintf(result, sizeof(result), "%s\n", duplicated);
        free(duplicated);
    }

    if (strcmp(command, "concat_strings") == 0) {
        char* concatenated = concat_strings(arg_1_str, arg_2_str);
        snprintf(result, sizeof(result), "%s\n", concatenated);
        free(concatenated);
    }

    if (strcmp(command, "delete_symbol") == 0) {
        char* deleted = delete_symbol(arg_1_str, arg_2_int);
        snprintf(result, sizeof(result), "%s\n", deleted);
        free(deleted);
    }

    write_result_to_file(result);
    fclose(fptr);

    return 0;
 }
