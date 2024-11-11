l1: list[str] = ["Grand Theft Auto V", "Fortnite", "Overwatch", "Dark souls", "The Elder Scrolls V: Skyrim"]

# exc.a
print("a", list(filter(lambda word: len(word) > 8, l1)))

# exc.b
print("b", list(filter(lambda word: word.upper().startswith("F"), l1)))

# exc.c
print("c", list(filter(lambda word: " " in word and word.count(" ") == 1, l1)))

# exc.d
print("d", list(filter(lambda word: "V" in word.upper(), l1)))
