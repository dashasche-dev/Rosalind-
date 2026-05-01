# Rabbits and Recurrence Relations.
n=5
k=3
rabbit_pairs = {0:1, 1:1}
for i in range(2, n):
    rabbit_pairs[i] = rabbit_pairs[i-1] + k*rabbit_pairs[i-2]
print(rabbit_pairs[n-1])
