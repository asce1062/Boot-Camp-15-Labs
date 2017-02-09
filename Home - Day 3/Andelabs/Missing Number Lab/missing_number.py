# Function that when passed two arrays of positive integers
# returns missing number in one of the arrays and not the other.
# Returns 0 if both arrays empty both have the same numbers.


def convert(final_array):  # function to convert a list to an integer
    num = int(''.join(map(str, final_array)))
    return num


def find_missing(first_array, second_array):  # function to find the missing number

    if len(first_array) > len(second_array):
        final_array = list(set(first_array) - set(second_array))
        return convert(final_array)
    elif len(second_array) > len(first_array):
        final_array = list(set(second_array) - set(first_array))
        return convert(final_array)
    elif len(second_array) == 0 and len(first_array) == 0:
        return 0
    elif len(first_array) == len(second_array):
        return 0
