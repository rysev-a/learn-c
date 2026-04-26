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
