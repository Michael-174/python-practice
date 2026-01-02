data= "Python dictionary is amazing"

freq = {}
for letter in data:
    freq[letter] = freq.get(letter,0) + 1

for key in freq:
    print(key,freq[key])