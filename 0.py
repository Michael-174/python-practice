data = "nigga nigga nigga nigga nigga"

freq = {}
for a in data:
    freq[a] = freq.get(a, 0) + 1

for key in freq:
    print(key, freq[key])