# Consensus and Profile.
s = ["ATCCAGCT", "GGGCAACT", "ATGGATCT", "AAGCAACC", "TTGGAACT", "ATGCCATT", "ATGGCACT"]
profile_matrix = {"A": [0] * len(s[0]), "C": [0] * len(s[0]), "G": [0] * len(s[0]), "T": [0] * len(s[0])}
for dna in s:
    for position, nucleotide in enumerate(dna):
        profile_matrix[nucleotide][position] += 1
print(profile_matrix)
result = []
for position in range(len(s[0])):
    max_count = 0
    max_nucleotide = ""
    for nucleotide, counts in profile_matrix.items():
        count = profile_matrix[nucleotide][position]
        if count > max_count:
            max_count = count
            max_nucleotide = nucleotide
            result.append(max_nucleotide)
print("".join(result))
print("A:", *profile_matrix['A'])
print("C:", *profile_matrix['C'])
print("G:", *profile_matrix['G'])
print("T:", *profile_matrix['T'])