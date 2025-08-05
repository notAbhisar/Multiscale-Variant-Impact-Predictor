import vcf

# Set of allowed clinical significances (normalized)
allowed_significances = {
    "pathogenic",
    "likely_pathogenic",
    "benign",
    "likely_benign"
}

# Input and output file paths
input_vcf_path = "data/GRCh38_VCF/clinvar.vcf"
output_vcf_path = "data/GRCh38_VCF/filtered_clinvar.vcf"

# Counters
included = 0
excluded = 0

# Open VCF
vcf_reader = vcf.Reader(open(input_vcf_path, 'r'))
vcf_writer = vcf.Writer(open(output_vcf_path, 'w'), vcf_reader)

for record in vcf_reader:
    clnsig_values = record.INFO.get('CLNSIG', [])

    if not clnsig_values:
        excluded += 1
        continue

    # Normalize and split CLNSIG values
    normalized_values = set()
    for val in clnsig_values:
        split_vals = [v.strip().lower().replace(" ", "_") for v in val.split(",")]
        normalized_values.update(split_vals)

    # Check if any match
    if normalized_values & allowed_significances:
        vcf_writer.write_record(record)
        included += 1
    else:
        excluded += 1

vcf_writer.close()

print(f"✅ Filtering complete.")
print(f"Variants included: {included}")
print(f"Variants excluded: {excluded}")
