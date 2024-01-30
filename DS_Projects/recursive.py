def prettify(the_str):
    i = 0
    while i < len(the_str):
        if the_str[i] not in "1234567890()":
            if the_str[i - 1] != '(' or the_str[i + 1] != ')':
                the_str = the_str[:i] + "1(" + the_str[i] + ")" + the_str[i + 1:]
                i += 2
        i += 1
    return the_str


def solve(the_str):
    if len(the_str) <= 1:
        return the_str
    for i in range(len(the_str)):
        m = 0
        if the_str[i] == '(':
            m += 1
            j = i
            while m != 0:
                j += 1
                if the_str[j] == '(':
                    m += 1
                elif the_str[j] == ')':
                    m -= 1
            return int(the_str[:i]) * solve(the_str[i + 1:j]) + solve(the_str[j + 1:])


my_str = input()
print(solve(prettify(my_str)))
