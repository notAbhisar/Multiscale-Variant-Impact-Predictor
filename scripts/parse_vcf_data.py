import vcf
import csv

reader = vcf.Reader(open('data/processed/filtered_clinvar.vcf', 'r'))

with open('data/processed/clinvar_features.csv', 'w', newline='') as csvfile:
    fieldnames = ['POS', 'REF', 'ALT', 'CLNSIG', 'GENE', 'MC', 'CLNVC', 'CLNREVSTAT']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for record in reader:
        info = record.INFO
        geneinfo = info.get('GENEINFO', [''])[0].split(':')[0] if 'GENEINFO' in info else ''
        mc = info.get('MC', [''])[0].split('|')[1] if 'MC' in info and '|' in info['MC'][0] else ''
        writer.writerow({
            'POS': record.POS,
            'REF': record.REF,
            'ALT': str(record.ALT[0]),
            'CLNSIG': info.get('CLNSIG', [''])[0],
            'GENE': geneinfo,
            'MC': mc,
            'CLNVC': info.get('CLNVC', ''),
            'CLNREVSTAT': info.get('CLNREVSTAT', [''])[0],
        })
