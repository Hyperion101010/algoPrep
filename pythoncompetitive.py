# A sample problem regarding strings and converting string char to ascii and storing them as unique

words = ["apple", "apel", "silent", "listen", "papel"]

tmp = []

for word in words:
    sm = 0
    mp = dict()
    for j in word:
        mp[ord(j)] = ord(j)
    for k, v in mp.items():
        sm += v
    tmp.append(sm)

tmp = sorted(tmp)

#print(tmp)
dt = dict()
for i in tmp:
    if i in dt:
        dt[i] += 1
    else:
        dt[i] = 1

ans = 0
for k, v in dt.items():
    ans += int((v*(v-1))/2)
print(ans)


# To sort the dictionary according to the value of dictionary
dict(sorted(my_dict.items(), key=lambda item: item[1]))
