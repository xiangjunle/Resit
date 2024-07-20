seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
# Function to calculate the reverse complement of a DNA sequence
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join([complement[base] for base in reversed(dna)])
    return reverse_comp


rc_seq = reverse_complement(seq)
print("The reverse complementary sequence is:", rc_seq)