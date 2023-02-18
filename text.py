import random


def factorial(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
    return temp


while True:
    try:
        n = int(input())
        t = list()
        t1 = set()
        for i in range(1, n + 1):
            t.append(str(i))

        while True:
            if len(t1) >= factorial(n):
                break

            random.shuffle(t)
            t1.add(" ".join(t))

        s = sorted(t1)
        for i in s:
            print(i)

    except:
        break
