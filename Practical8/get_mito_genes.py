# get_mito_genes.py

def extract_mitochondrial_genes(fasta_file, output_file):
    with open(fasta_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as outfile:
        current_gene = None
        for line in lines:
            if line.startswith('>'):
                # 检查是否是线粒体基因
                if 'Mito' in line:
                    # 提取基因名称
                    gene_name = line.strip()[1:].split()[0]
                    current_gene = gene_name
                    outfile.write(f">{gene_name}\n")
                else:
                    # 不是线粒体基因，重置当前基因
                    current_gene = None
            elif current_gene:
                # 写入当前基因的序列
                outfile.write(line)

if __name__ == "__main__":
    fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all (2).fa'
    output_file = 'mito_genes.fa'
    extract_mitochondrial_genes(fasta_file, output_file)