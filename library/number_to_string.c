#include <stdio.h>
#include <string.h>


// write result to output.txt
#include "library/write_to_file.c"


char* append_l(char* input_str, char symbol) {
    int size = strlen(input_str);

    char* result = malloc(size + 2);

    result[0] = symbol;

    for (int i = 1; i < size + 1; i++) {
        result[i] = input_str[i - 1];
    }
    free(input_str);

    result[size + 1] = '\0';

    return result;
}

char* append_r(char* input_str, char symbol) {
    int size = strlen(input_str);
    char* result = malloc(size + 2);

    for (int i = 0; i < size + 1; i++) {
        result[i] = input_str[i];
    }

    result[size] = symbol;
    result[size + 1] = '\0';

    return result;
}

char* copy_str(char* input_string) {
    int size = strlen(input_string);
    char* result = malloc(size + 1);

    for (int i = 0; i < size; i++) {
        result[i] = input_string[i];
    }

    result[size] = '\0';

    return result;
}

char* number_to_string(int input_number) {
    char* result = copy_str("");


    while (input_number) {
        int number_symbol = input_number % 10;
        // char *prev_str = result;
        result = append_l(result, number_symbol + 48);

        // free(prev_str);

        input_number = input_number / 10;
    }


    return result;
}


int main() {
    printf("%s", number_to_string(1234));
    return 0;
 }
