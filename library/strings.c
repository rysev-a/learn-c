#include <cmath>
#include <ctype.h>

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


int is_beginning(char* begin, char* full_string) {
    int begin_len = get_string_length(begin);
    int full_string_length = get_string_length(full_string);

    if (begin_len > full_string_length) {
        return 0;
    }

    int i = 0;
    while (i < begin_len) {
        if (begin[i] != full_string[i]) {
            return 0;
        }
        i++;
    }

    return 1;
}


int is_palindrome(char* input_string) {
    int string_length = get_string_length(input_string);
    int i = 0;
    int j = string_length - 1;
    while (i < j) {
        if (input_string[i] != input_string[j]) {
            return 0;
        }
        i++;
        j--;
    }

    return 1;
}


int is_lower_case(char* input_string) {
    int string_length = get_string_length(input_string);

    for (int i = 0; i < string_length; i++) {
        if (input_string[i] < 97 || input_string[i] > 122) {
            return 0;
        }
    }

    return 1;
}

//int is_identifier(char* input_string) {
//    if (input_string[0] < 97 || input_string[0] > 122) {
//        return 0;
//    }
//
//    int i = 1;
//    while (input_string[i]) {
//        if (is_alpha(input_string[i])) {
//            return 0;
//        }
//    }
//
//    return 1;
//}
