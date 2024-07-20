
def extract_mitochondrial_genes(fasta_file, output_file):
    with open(fasta_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as outfile:
        current_gene = None
        for line in lines:
            if line.startswith('>'):
                # Check if it is a mitochondrial gene
                if 'Mito' in line:
                    # Extract gene names
                    gene_name = line.strip()[1:].split()[0]
                    current_gene = gene_name
                    outfile.write(f">{gene_name}\n")
                else:
                    # Not a mitochondrial gene, reset the current gene
                    current_gene = None
            elif current_gene:
                outfile.write(line)

if __name__ == "__main__":
    fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all (2).fa'
    output_file = 'mito_genes.fa'
    extract_mitochondrial_genes(fasta_file, output_file)