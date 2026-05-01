num = 1
while num != 20:
    print(num)
    if num == 15:
        break
    num += 1

num = 1
while num != 30:
    if num % 2 == 0:
        num +=1
        continue
    print(num)
    num +=1