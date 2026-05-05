# Finding a motif in DNA.
s = "GATATATGCATATACTT"
t = "ATAT"
position = []
for i in range(len(s) - len(t)+1):
    j = 0
    while j<len(t) and s[i+j] == t[j]:
        j +=1
    if j == len(t):
        position.append(i+1)
print(*position)
