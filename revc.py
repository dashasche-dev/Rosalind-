# Complementing a strand of DNA.
s = "AAAACCCGGT"
s = list(s)
s_reversed = []
for i in range(len(s)):
    l = s[-1]
    s_reversed.append(l)
    s.pop(-1)
complementary = {"A": "T", "T": "A", "C": "G", "G": "C"}
s_reversed_complementary = "".join(complementary[base] for base in s_reversed)
print(s_reversed_complementary)