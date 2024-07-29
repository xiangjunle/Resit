def separate_genes(gene_names):
    gene_count = {}
    for gene in gene_names:
        if gene in gene_count:
            gene_count[gene] += 1
        else:
            gene_count[gene] = 1
    
    # Separate the genes into unique and duplicate lists based on their counts
    unique_genes = [gene for gene, count in gene_count.items() if count == 1]
    duplicate_genes = [gene for gene, count in gene_count.items() if count > 1]
    
    return unique_genes, duplicate_genes

# Example
gene_names = ['DLX5', 'DLX6', 'NBAS', 'BRCA2', 'BRCA2', 'NBAS']
unique, duplicates = separate_genes(gene_names)
print("Unique genes:", unique)
print("Duplicate genes:", duplicates)