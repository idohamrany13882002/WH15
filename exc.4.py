l1: list[str] = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

# exc.a
print("a", list(map(lambda word: word[::-1], l1)))

# exc.b
print("b", list(map(lambda word: word[0], l1)))

# exc.c
print("c", list(map(lambda word: word.upper(), l1)))

# exc.d
print("d", list(map(lambda word: word[len(word) // 2], l1)))

# exc.e
print("e", list(map(lambda word: word + "!" if word.endswith("s") else word, l1)))
