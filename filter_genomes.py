# This python3 script inputs a SARS-CoV2 protein alignment file of spike protein sequences and outputs lists of genome ID's with complete spike protein sequences. The output ID lists are split up by 300 at a time. Geneious software only allows searching for a few hundred ID's at once.

complete_sequences=[]

for line in open("all_sars2_protein_alignment.fasta"):
    i=line.strip().split()
    if line[0]==">":
        id = i[0].split("_-_")[0].strip(">")
        continue
    else:
        seq = line.strip()
        gap = seq.count("X")
        # My threshold in this case is 0 gaps (X's)
        if gap == 0:
            complete_sequences.append(id)

# Print out multiple comma-separated lists as input for Geneious nucleotide search. Select all and then download.
print(",".join(L[:300]))
print("  ")
print(",".join(L[300:600]))
print("  ")
print(",".join(L[600:900]))
print("  ")
print(",".join(L[900:1200]))
print("  ")
print(",".join(L[1200:1500]))
