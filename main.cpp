#include <cstdio>
#include <stdio.h>
#include <stdlib.h>

class DynamicArray {
    public:
    int *data;
    int full_size;
    int filled_size;

    DynamicArray() {
        data = (int *)malloc(5 * sizeof(int));
        full_size = 5;
        filled_size = 0;
    }

    void add_element_to_array(int value) {
        data[filled_size] = value;
        filled_size++;
        
        
        free(data);
        data = (int *)malloc(10 * sizeof(int));
    }

    void show_array_elements() {
        for (int i = 0; i < filled_size; i++) {
            printf("%d\n", data[i]);
        }
    }
};


int main() {
    DynamicArray dynamic_array;
    dynamic_array.add_element_to_array(5);
    dynamic_array.show_array_elements();

    return 0;
}
