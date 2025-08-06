import pandas as pd

def vcf_to_bed(vcf_file, bed_file):
    with open(vcf_file) as vcf, open(bed_file, 'w') as bed:
        for line in vcf:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            chrom = "chr" + parts[0]  # <-- Add this line
            pos = int(parts[1])
            var_id = parts[2] if parts[2] != '.' else f"{chrom}_{pos}"
            start = pos - 1
            end = pos
            bed.write(f"{chrom}\t{start}\t{end}\t{var_id}\n")


vcf_to_bed("data/processed/filtered_clinvar.vcf", "data/processed/filtered_clinvar.bed")
