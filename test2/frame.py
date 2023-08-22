# arr = ["Hello", "World", "in", "a", "frame"]
arr = ["Hello   ", "qefqefqefWorld", "in", "a", "framecefef", 'fgfwwgfwegwegwg', 'efq']

longest = 0
for i in arr:
    if len(i) > longest:
        longest =  len(i)


first_line = "****"
for i in range(longest):
    first_line+="*"

final = []

for i in arr:
    length = len(i)
    if length == longest:
        i = f"* {i} *"
    else:
        i = f"* {i}"
        for space in range(longest - length):
            i += f" "

        i += f" *"
    final.append(i)

print(first_line)
for i in final:
    print(i)
print(first_line)