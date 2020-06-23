# This python script prints out the number of sequence matches in our oligo library.
# This was used to confirm that PEPSYN software worked properly.
# As these restriction sites are palidromic sequences, the rev. complement is the same.
2020-06-23
bmain 

hind='AAGCTT'
EcoR1='GAATTC'

input = "protien_seqs_sorted.tsv"

def cut_site_finder(oligo_file,site):
    D={}
    for line in open(oligo_file):
        i=line.strip().split()
        oligo = i[1]
        cut_count = oligo.count(site)
        if cut_count not in D:
            D[cut_count]=0
        D[cut_count]+=1
    return(D)

HindIII_cuts = cut_site_finder(input,hind)
for c in HindIII_cuts:
    print("HindIII",c,HindIII_cuts[c])

EcoR1_cuts = cut_site_finder(input,EcoR1)
for count in EcoR1_cuts:
    print("EcoR1",count,EcoR1_cuts[count])

