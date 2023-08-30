def print_strings_in_frame(strings):
    if not strings:
        print("Empty list")
        return

    max_length = max(len(s) for s in strings)
    border = '+' + '-' * (max_length + 2) + '+'

    print(border)
    for string in strings:
        print('| ' + string + ' ' * (max_length - len(string)) + ' |')
    print(border)

string_list = ["Hello my name is Maurice", "And this is my world", "in python"]
print_strings_in_frame(string_list)
