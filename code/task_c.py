#!//anaconda/envs/jnjtest/bin/python

""" 
Title of paper:
Comparison of assembled Clostridium botulinum A1 genomes revealed their evolutionary relationship
URL: http://www.sciencedirect.com/science/article/pii/S0888754313002280
Published: Jan 2014

Strain # 1: Clostridium botulinum A str. ATCC 3502
NCBI: https://www.ncbi.nlm.nih.gov/nuccore/NC_009495?report=genbank

Strain # 2: Clostridium botulinum A str. ATCC 19397
NCBI: https://www.ncbi.nlm.nih.gov/nuccore/NC_009697?report=genbank
"""

import zipfile, os, subprocess
from Bio import Entrez


TERM = "NC_009697 OR NC_009495"
MAUVE_LOC = '/Applications/Mauve.app/Contents/MacOS/progressiveMauve'
Entrez.email = "A.N.Other@example.com"


handle = Entrez.esearch(db="nuccore", term=TERM)
record = Entrez.read(handle)
gi_list = record["IdList"]


for x in gi_list:
	handle2 = Entrez.efetch(db="nuccore", id=x, rettype="fasta", retmode="text")
	outfile = open(x+".fasta","w")
	outfile.write(handle2.read())
	outfile.close()

runmauve = '{0} --output=clostridia.xmfa {1} \
{2}'.format(MAUVE_LOC,gi_list[0]+".fasta",gi_list[1]+".fasta")

subprocess.call(runmauve, shell=True)