c = 600851475143
a = []
for i in range(2, 2000000):
    while c % i == 0:
        c //= i
        if c == 1 or c == i:
            print(i)
