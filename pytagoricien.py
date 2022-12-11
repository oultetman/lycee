def pytagoricien(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a ** 2 + b ** 2 == c ** 2


for a in range(1, 51):
    for b in range(a+1, 51):
        for c in range(b+1, 51):
            if pytagoricien(a, b, c):
                print(a, b, c, end=" ")
                if a == 15 or b == 15 or c == 15:
                    print("*")
                else:
                    print()
