numberGames = {}
numberGames[(1,2,4)] = 8
numberGames[(4,2,1)] = 10
numberGames[(1,2)] = 12

sum = 0
for k in numberGames:
    sum += numberGames[k]

print(len(numberGames) + sum)

t1 = (1, 2, 4, 3)
t2 = (1, 2, 3, 4)
print(t1 < t2)

tuple1 = ("Peach", [10, 20, 30], (5, 15, 25))
print(tuple1[1][2])

del sum
numbers = (7, 8, 9, 1, 10, 7)
print("Tuple:", numbers)
total = sum(numbers)
print("Sum:", total)

countries = ("Brazil", "Argentina", "Portugal", "Spain", "Canada", "Cameroon")
print("Original tuple:", countries)
sorted_countries = tuple(sorted(countries))
print("Sorted tuple:", sorted_countries)

numbers = (2, 3, 4, 2, 5, 6, 7, 3, 8, 5, 9, 6, 6, 7, 8, 9, 9, 4, 5)

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
for num, count in freq.items():
    print(num, "appears", count, "times")

    numbers = (100, 234, 87, 56, 78, 90)
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    print("Tuple:", numbers)
    print("Mean/Average:", mean)




