#include <ctype.h>
#include <stdlib.h>
#include <string.h>


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

int is_identifier(char* input_string) {
   if (!isalpha(input_string[0])) {
       return 0;
   }

   int i = 1;
   while (input_string[i]) {
       if (!isalnum(input_string[i])) {
           return 0;
       }
       i++;
   }

   return 1;
}

void upcase(char* input_string) {
    int string_length = get_string_length(input_string);

    for (int i = 0; i < string_length; i++) {
        if (input_string[i] >= 97 && input_string[i] <= 122) {
            input_string[i] -= 32;
        }
    }
}


void swap_case(char* input_string) {
    int string_length = get_string_length(input_string);

    for (int i = 0; i < string_length; i++) {
        if (input_string[i] >= 97 && input_string[i] <= 122) {
            input_string[i] -= 32;
        } else if (input_string[i] >= 65 && input_string[i] <= 90) {
            input_string[i] += 32;
        }
    }
}


void reverse(char* input_string) {
    int string_length = get_string_length(input_string);
    int i = 0;
    int j = string_length - 1;
    while (i < j) {
        char temp = input_string[i];
        input_string[i] = input_string[j];
        input_string[j] = temp;
        i++;
        j--;
    }
}


char* duplicate_string(char* input_string, int count) {
    int string_length = get_string_length(input_string);
    char* result = malloc(count * string_length + 1);
    for (int repeat_index = 0; repeat_index < count; repeat_index++) {
        for (int i = 0; i < string_length; i++) {
            result[repeat_index * string_length + i] = input_string[i];
        }
    }
    result[count * string_length] = '\0';

    return result;
}

char* concat_strings(char* left_string, char* right_string) {
    int left_string_length = get_string_length(left_string);
    int right_string_length = get_string_length(right_string);
    int result_length = left_string_length + right_string_length;

    char* result = malloc(result_length + 1);


    for (int i = 0; i < left_string_length; i++) {
        result[i] = left_string[i];
    }

    for (int i = 0; i < right_string_length; i++) {
        result[left_string_length + i] = right_string[i];
    }

    result[result_length] = '\0';
    return result;
}

char* delete_symbol(char* input_str, int index) {
    int original_string_length = get_string_length(input_str);
    int result_length = original_string_length - 1;
    char* result = malloc(result_length + 1);

    int shift = 0;

    for (int i = 0; i < original_string_length; i++) {
        if (i == index) {
            shift = 1;
            continue;
        }
        result[i - shift] = input_str[i];
    }

    result[result_length] = '\0';
    return result;
}

char* title_case(char* input_string) {
    int string_length = get_string_length(input_string);
    char* result = malloc(string_length + 1);

    for (int i = 0; i < string_length; i++) {
        if (i == 0 || input_string[i - 1] == ' ') {
            result[i] = toupper(input_string[i]);
        } else {
            result[i] = input_string[i];
        }
    }

    result[string_length] = '\0';
    return result;
}
