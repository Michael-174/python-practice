
#for each letter in FAVOURITE turn it into lower case and print them as a list
print([i.lower() for i in "FAVORITE"])

#for the first x in python c, it will contain 2 y in language programing
l = [x + y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]
print(l)

odd = [1, 9]
odd.insert(1, 3)
print(odd)
odd[2:2] = [5, 7]
print(odd)

#to replace the first 10 into 100
numbers = [1,2,3,4,5,6,7,8,9,10,10]
numbers[numbers.index(10)] = 100
print(numbers)

numbers = [1,2,3,4,5,6,7,8,9,10,10]
print(max(numbers))

#to count how many times does 10 appear
numbers = [1,2,3,4,5,6,7,8,9,10,10,20,30]
print(numbers.count(10))

A = [9, 5, 6, 4, 7, 3, 1, 8]
print(A[A.index(7):])
print(A[A.index(5):A.index(7)])







