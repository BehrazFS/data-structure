def solve(the_str):
    for i in range(len(the_str)):
        if the_str[i] == '(':
            m = 1
            j = i
            while m != 0:
                j += 1
                if the_str[j] == '(':
                    m += 1
                elif the_str[j] == ')':
                    m -= 1
            k = i - 1
            while the_str[k] in "0123456789":
                k -= 1
            return ("" if solve(the_str[:k + 1]) is None else solve(the_str[:k + 1])) + int(
                the_str[k + 1:i]) * solve(the_str[i + 1:j]) + solve(the_str[j + 1:])
    return the_str


my_str = input()
print(solve(my_str))
