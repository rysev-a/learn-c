#include <stdio.h>
#include <stdlib.h>

void write_result_to_file(const char *result) {
    FILE *fptr;
    fptr = fopen("./tmp/output.txt", "w");
    if (fptr == NULL) {
        printf("Error: Could not open the file.\n");
        exit(1); // Exit the program if an error occurs
    }

    fprintf(fptr, "%s", result);
    fclose(fptr);
}

void write_array_to_file(int number_array[], int array_size) {
    FILE *fptr;
    fptr = fopen("./tmp/output.txt", "w");
    if (fptr == NULL) {
        printf("Error: Could not open the file.\n");
        exit(1); // Exit the program if an error occurs
    }

    for (int i = 0; i < array_size; i++) {
        fprintf(fptr, "%d", number_array[i]);
        if (i < array_size - 1) {
            fprintf(fptr, " ");
        }
    }
    fclose(fptr);
}
