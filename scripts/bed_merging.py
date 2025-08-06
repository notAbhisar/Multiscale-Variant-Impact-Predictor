import pandas as pd

# Load each BED file with appropriate column names
k4me1 = pd.read_csv("clinvar_H3K4me1_feature.bed", sep="\t", header=None,
                    names=["chrom", "start", "end", "id", "H3K4me1_count"])
k4me3 = pd.read_csv("clinvar_H3K4me3_feature.bed", sep="\t", header=None,
                    names=["chrom", "start", "end", "id", "H3K4me3_count"])
k27ac = pd.read_csv("clinvar_H3K27ac_feature.bed", sep="\t", header=None,
                    names=["chrom", "start", "end", "id", "H3K27ac_count"])
dnase = pd.read_csv("clinvar_DNase_feature.bed", sep="\t", header=None,
                    names=["chrom", "start", "end", "id", "DNase_count"])

# Merge all on chrom, start, end, id
merged = k4me1.merge(k4me3, on=["chrom", "start", "end", "id"], how="outer")
merged = merged.merge(k27ac, on=["chrom", "start", "end", "id"], how="outer")
merged = merged.merge(dnase, on=["chrom", "start", "end", "id"], how="outer")

# Fill NaNs (where there was no overlap) with 0s
merged.fillna(0, inplace=True)

# Save to CSV or TSV
merged.to_csv("clinvar_epigenomic_features.tsv", sep="\t", index=False)
