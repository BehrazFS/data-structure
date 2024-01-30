for i in range(1, 100):
    lines = None
    path = rf'C:\Users\behraz\Downloads\Compressed\New folder\in\input{i}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [str(len(lines)) + "\n"] + lines
    # print(lines)
    with open(path,'w') as file:
        file.writelines(lines)
# def func(k):
#     return k[1]
#
#
# n = int(input())
# l = []
# for i in range(n):
#     line = input()
#     num = int(line.split()[1])
#     grade = "A"
#     if 14 <= num <= 15:
#         grade = "B"
#     elif 12 <= num <= 13:
#         grade = "C"
#     elif 10 <= num <= 11:
#         grade = "D"
#     elif 0 <= num <= 9:
#         grade = "F"
#     l.append([line.split()[0], int(line.split()[1]), grade])
# l.sort(key=func, reverse=True)
# for i in range(n//5):
#     print(l[i][0], l[i][1] , l[i][2])
