# Translating RNA into Protein.
from Bio.Seq import Seq
s ='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
s = Seq(s)
protein = s.translate()
print(protein.split('*')[0])