number1 = (2, 3, 4, 2, 5, 6, 7, 3, 8, 5, 9, 6, 6, 7, 8, 9, 9, 4, 5)
max = max(number1)
print("Max:", max)

Christopher = ('C', 'h', 'r', 'i', 's', 't', 'o', 'p', 'h', 'e', 'r')
print("Original tuple:", Christopher)
sorted_letters = tuple(sorted(Christopher))
print("Sorted elements:", sorted_letters)

basketball = ("Jordan", "Kobe", "LeBron", "Curry", "Durant")
k = "Curry"
index_pos = basketball.index(k)
print(f"The index of {k} is:", index_pos)