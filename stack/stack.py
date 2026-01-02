stack = [5, 9, 3]
stack.append(7)
stack.append(11)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

books = [
    "Berserk",
    "1984",
    "Steins;Gate",
    "Brave New World",
    "The Witcher"
]
print("Original Stack:", books)
books.append("Dune")
books.append("Fahrenheit 451")
print("After adding 2 new books:", books)
removed_book = books.pop()
print("Removed Book:", removed_book)
print("Final Stack:", books)


classmates = [
    "Alex", "Ben", "Chris", "David", "Ethan", "Frank", "George",
    "Harry", "Ivan", "Jack", "Kevin", "Liam", "Mike"
]
print("Original Stack:")
print(classmates)
print("\nPopped Names:")
print(classmates.pop())
print(classmates.pop())
print(classmates.pop())
print("\nFinal Stack:")
print(classmates)