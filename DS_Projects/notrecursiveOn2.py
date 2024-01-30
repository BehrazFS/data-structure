my_str = input()
index = len(my_str) - 1
while index >= 0:
    if my_str[index] == '(':
        index2 = index
        while my_str[index2] != ')':
            index2 += 1
        index3 = index - 1
        while my_str[index3 - 1] in "1234567890" and index3 > 0:
            index3 -= 1
        my_str = my_str[:index3] + int(my_str[index3: index]) * my_str[index + 1:index2] +\
                 my_str[index2 + 1:]
    index -= 1
print(my_str)
