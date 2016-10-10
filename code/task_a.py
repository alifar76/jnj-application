#!//anaconda/envs/jnjtest/bin/python

import tarfile, os, wget, subprocess
import pandas as pd

"""
Mac OSX specific blast executables were downloaded from:
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
"""

#### Variables that can change from system to system
#Location of blastn executable file
BLASTN_EXEC = '$PWD/blastn'
# NCBI FTP Server address for 16SMicrobial database
DB_16S = 'ftp://ftp.ncbi.nih.gov/blast/db/16SMicrobial.tar.gz'
# Location of input file for Task A
TASK_A_INPUT = '$PWD/task-a.fasta'


# Get 16SMicrobial db file
wget.download(DB_16S)
# Untar the 16SMicrobial db file
tar = tarfile.open("16SMicrobial.tar.gz")
tar.extractall()
tar.close()
# blastn command
runblast = '{0} -query {1} -db 16SMicrobial -out out_blast.txt \
-outfmt "6 qseqid evalue stitle"'.format(BLASTN_EXEC,TASK_A_INPUT)
# Command with shell expansion
subprocess.call(runblast, shell=True)
# Read in BLAST output file
data = pd.read_table('out_blast.txt',header=None,
   converters={0: str}, engine='python')
# The sequence header in input file
inputseqs = data[0].unique()
# Create new data frame to store results
df = pd.DataFrame()
# Loop over each individual query sequence
for x in inputseqs:
    subset = data.loc[data[0] == x]
    new_df = subset[subset[1] == min(subset[1])]
    if new_df.shape[0] == 1:
    	species = ' '.join(list(new_df[2].values)[0].split()[:2])
    	result = [list(new_df[0].values)[0],species]
    	df2 = pd.DataFrame([result],)
        df = df.append(df2,ignore_index=True)
    else:
    	result = [list(set(new_df[0].values))[0],'n.a.']
        df2 = pd.DataFrame([result],)
        df = df.append(df2,ignore_index=True)
 
# Write output file
df.to_csv("task-a-result.csv",header=False,index=False)