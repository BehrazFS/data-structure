works = list(input().strip()[2:-2].split("),("))
num = 0
money = 0
max_deadline = -1
for i in range(len(works)):
    works[i] = list(map(int, works[i].split(",")))
    if max_deadline < works[i][1]:
        max_deadline = works[i][1]
while max_deadline > 0:
    lw = [[item[0], item[1], item[2]] for item in works if item[1] >= max_deadline]
    index = 0
    for i in range(len(lw)):
        if lw[index][2] < lw[i][2]:
            index = i
    num += 1
    money += lw[index][2]
    temp = lw[index][0]
    max_deadline -= 1
    works = [[item[0], item[1], item[2]] for item in works if item[0] != temp]

print(num, money)
