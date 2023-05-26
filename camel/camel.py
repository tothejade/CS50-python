strings = input("camelCase: ")
print("snake_case: ", end="")
for s in strings:
    if s.islower():
        print(s, end="")
    else:
        print(f"_{s.lower()}", end="")
print()