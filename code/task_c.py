#!//anaconda/envs/jnjtest/bin/python

""" 
Title of paper:
Comparison of assembled Clostridium botulinum A1 genomes revealed their evolutionary relationship
URL: http://www.sciencedirect.com/science/article/pii/S0888754313002280
Published: Jan 2014

Strain # 1: Clostridium botulinum A str. ATCC 3502
NCBI: https://www.ncbi.nlm.nih.gov/nuccore/NC_009495?report=genbank

Strain # 2: Clostridium botulinum A str. Hall chromosome
NCBI: https://www.ncbi.nlm.nih.gov/nuccore/NC_009698
"""

import os, subprocess
from Bio import Entrez

MAUVE_LOC = '/Applications/Mauve.app/Contents/MacOS/progressiveMauve'
Entrez.email = "A.N.Other@example.com"
strain_dict = {'NC_009495':'ATCC_3502','NC_009698':'Hall_A'} 
#TERM = "NC_009697 OR NC_009495"

accession = strain_dict.keys()
gid_name = {}

for x in accession:
	handle = Entrez.esearch(db="nuccore", term=x)
	record = Entrez.read(handle)
	gid_name[record["IdList"][0]] = x


for x in gid_name.keys():
	handle2 = Entrez.efetch(db="nuccore", id=x, rettype="fasta", retmode="text")
	outfile = open(strain_dict[gid_name[x]]+".fasta","w")
	outfile.write(handle2.read())
	outfile.close()

runmauve = '{0} --output=clostridia.xmfa {1} \
{2}'.format(MAUVE_LOC,strain_dict.values()[0]+".fasta",strain_dict.values()[1]+".fasta")
subprocess.call(runmauve, shell=True)

