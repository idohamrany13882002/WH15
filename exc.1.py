import random

l1: list[int] = []
for _ in range(50):
    l1.append(random.randint(1, 100))
print(l1)

# exc.a
print("a", list(filter(lambda x: x > 50, l1)))

# exc.b
print("b", list(filter(lambda x: x % 7 == 0, l1)))

# exc.c
print("c", list(filter(lambda x: 10 <= x <= 99, l1)))

# exc.d
print("d", list(filter(lambda x: 10 <= x <= 99 and x // 10 == x % 10, l1)))

# exc.e
print("e", list(filter(lambda x: (x // 10) + (x % 10) == 9, l1)))

# exc.f
print("f", list(filter(lambda x: x > (sum(l1) / 100), l1)))

# exc.g
print("g", list(filter(lambda x: x > (max(l1) / 2), l1)))
