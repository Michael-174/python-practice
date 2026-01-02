squares = {1:1,
           2:4,
           3:9,
           4:16,
           5:25}
print(squares)
key = int(input("Enter a key to delete:"))
print("you deleted",squares[key])
del squares[key]
print(squares)



