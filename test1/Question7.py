#Write a function that combines two lists by alternatingly taking elements, e.g. [a, b, c], [1, 2,3] becomes – [a, 1, b, 2, c, 3].

def combine_alternate_lists(list1, list2):
    combined_list = []
    len1, len2 = len(list1), len(list2)
    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            combined_list.append(list1[i])
        if i < len2:
            combined_list.append(list2[i])

    return combined_list


list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
result = combine_alternate_lists(list1, list2)
print(result) 


