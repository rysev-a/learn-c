int get_string_length(char* input_string) {
    int i = 0;
    while (input_string[i]) {
        i++;
    }
    return i;
}


int is_substring(char* substring, char* full_string) {
    int main_index = 0;
    int max_result = 0;
    int substring_index = 0;
    int counter_index = 0;

    int full_string_length = get_string_length(full_string);
    int substring_length = get_string_length(substring);

    int counters[100] = {0};
    int max_match = 0;

    while (full_string[main_index]) {
        printf("main_index: %d\n", main_index);
        for (int counter_i=0;counter_i < (sizeof (counters) /sizeof (counters[0]));counter_i++) {
            printf("%d_",counters[counter_i]);
        }


        if (full_string[main_index] == substring[0]) {
            counters[main_index] = 1;
        }

        counter_index = main_index - 1;
        while (counter_index >= 0 && main_index - counter_index < substring_length) {
            if (counters[counter_index] > 0) {
                if (substring[main_index - counter_index] == full_string[main_index]) {
                    counters[counter_index]++;
                    if (counters[counter_index] > max_match) {
                        max_match = counters[counter_index];
                    }
                } else {
                    counters[counter_index] = 0;
                }
            }
            counter_index--;
        }
        main_index++;
    }

    if (max_match == substring_length) {
        return 1;
    };
    return 0;
}
