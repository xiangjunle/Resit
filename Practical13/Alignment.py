from Bio.SubsMat import MatrixInfo

# Function to read sequence files
def read_sequence(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read().strip()
    return sequence

# Function to calculate the alignment score
def calculate_score(seq1, seq2):
    blosum62 = MatrixInfo.blosum62
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += blosum62.get(aa1, {}).get(aa2, 0)
    return score

# Main function
def main():
    sequences = {'human': r'C:\Users\12249\Downloads\SOD2_human (1).fa','mouse': r'C:\Users\12249\Downloads\SOD2_mouse (1).fa','rat': r'C:\Users\12249\Downloads\RandomSeq (2).fa'}
    
    # Read sequences
    seqs = {key: read_sequence(value) for key, value in sequences.items()}
    
    # Compare all possible pairs of sequences
    for name1, seq1 in seqs.items():
        for name2, seq2 in seqs.items():
            if name1 < name2:  # Avoid duplicate comparisons
                score = calculate_score(seq1, seq2)
                print(f"Alignment score between {name1} and {name2}: {score}")

if __name__ == "__main__":
    main()