import random

l1: list[int] = []
for _ in range(20):
    l1.append(random.randint(-50, 50))
print(l1)

# exc.a
print("a", list(map(lambda x: x ** 3, l1)))

# exc.b
print("b", list(map(lambda x: x % 10 if x > 0 else (x % -10) * (-1), l1)))

# exc.c
print("c", list(map(lambda x: (x * (9 / 5) + 32), l1)))

# exc.d
print("d", list(map(lambda x: "positive" if x >= 0 else "negative", l1)))
