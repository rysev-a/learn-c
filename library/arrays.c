#include <stdio.h>
#include <string.h>


void print_array_numbers(int number_array[], int array_size) {
    for (int i = 0; i < array_size; i++) {
        printf("%d ", number_array[i]);
    }
}

int is_sorted_array(int number_array[], int array_size) {
    for (int i = 1; i < array_size; i++) {
        if (number_array[i - 1] > number_array[i]) {
            return 0;
        }
    }
    return 1;
}

void bubble_sorting(int number_array[], int array_size) {
    for (int i = 0; i < array_size; i++) {
        for (int j = 0; j < array_size - 1 - i; j++) {
	    int left_value = number_array[j];
            int right_value = number_array[j + 1];

            if (left_value > right_value) {
                number_array[j] = right_value;
                number_array[j + 1] = left_value;
            }
        }
    }
}
