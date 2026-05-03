s = list('GAGCCTACTAACGGGAT')
t = list('CATCGTAATGACGGCCT')
hamm_dist = 0
for i in range (len(s)):
    if s[i] != t[i]:
        hamm_dist +=1
print(hamm_dist)