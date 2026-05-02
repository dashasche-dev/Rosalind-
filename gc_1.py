# Computing GC Content.
from Bio import SeqIO
seq_1 = "C:\\Users\\PC\\Desktop\\data\\seq_1.fasta.txt"
seq_2 ="C:\\Users\\PC\\Desktop\\data\\seq_2.fasta.txt"
seq_3 = "C:\\Users\\PC\\Desktop\\data\\seq_3.fasta.txt"
seq_record_1 = SeqIO.read(seq_1, "fasta")
seq_record_2 = SeqIO.read(seq_2, "fasta")
seq_record_3 = SeqIO.read(seq_3, "fasta")
def gc_counter(seq_record):
    number_of_g = seq_record.seq.count("G")
    number_of_c = seq_record.seq.count("C")
    gc_content = (number_of_g + number_of_c) / len(seq_record.seq) * 100
    return gc_content
gc_of_all_seq = {}
for seq in [seq_record_1, seq_record_2, seq_record_3]:
    gc_of_all_seq[seq.id] = gc_counter(seq)
max_gc_number = max(gc_of_all_seq.values())
for seq.id, gc in gc_of_all_seq.items():
    if gc == max_gc_number:
        print(f">{seq.id}")
print(f"{max_gc_number:.6f}")
