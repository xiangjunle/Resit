def reverse_complement(dna):
    """Function to calculate the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in reversed(dna)])

def extract_mitochondrial_genes(fasta_file, output_file):
    """Function to extract mitochondrial genes and write their reverse complements to a new FASTA file."""
    with open(fasta_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as outfile:
        current_gene = None
        for line in lines:
            if line.startswith('>'):
                # Check if it's a mitochondrial gene
                if 'Mito' in line:
                    # Extract the gene name and sequence length
                    gene_name = line.strip()[1:].split()[0]
                    sequence_length = len(current_gene) if current_gene else 0

                    # Write the reverse complement sequence with simplified header
                    outfile.write(f">{gene_name}_{sequence_length}\n")
                    outfile.write(reverse_complement(current_gene) + "\n")
                    current_gene = None
                else:
                    # Not a mitochondrial gene, reset current gene
                    current_gene = None
            elif current_gene is None:
                # First sequence line after a header
                current_gene = line.strip()
            else:
                # Append subsequent sequence lines
                current_gene += line.strip()

def main():
    # Ask the user for a filename
    filename = input("Enter the name for the new FASTA file: ")
    fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = filename

    # Extract mitochondrial genes and write their reverse complements
    extract_mitochondrial_genes(fasta_file, output_file)
    print(f"Reverse complement sequences saved to {output_file}")

if __name__ == "__main__":
    main()