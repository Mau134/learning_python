def print_strings_in_frame(strings):
    if not strings:
        print("Empty list")
        return

    max_length = 0
    for string in strings:
        current_length = 0
        for char in string:
            current_length += 1
        if current_length > max_length:
            max_length = current_length

    border = '*' + '*' * (max_length + 2) + '*'

    print(border)
    for string in strings:
        padding = ' ' * (max_length - len(string))
        print('* ' + string + padding + ' *')
    print(border)

# Example usage:
string_list = ["Hello my name is Maurice", "And this is my world", "in python"]
print_strings_in_frame(string_list)
