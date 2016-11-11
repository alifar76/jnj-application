#!//anaconda/envs/jnjtest/bin/python

import zipfile, os, subprocess

#### Variables that can change from system to system
# Location of input file for Task B
# Assumes the zip file in in working directory
TASK_B_INPUT = 'test-contigs.zip'


# Extract zipfile
zipfile.ZipFile(TASK_B_INPUT).extractall()

contig_folder = TASK_B_INPUT.split('.zip')[0]
fasta = os.listdir(contig_folder)
for x in fasta:
    if '.fasta' in x:
        prefix = x.split('-contigs.fasta')[0]
        runprokka = 'prokka --kingdom Bacteria --outdir prokka_JNJ_{0} \
--locustag {1} {2}/{3} --centre X --compliant'.format(prefix,prefix,contig_folder,x)
        # Run prokka 
        subprocess.call(runprokka, shell=True)

currfolder = os.getcwd()
roary_fold = currfolder+"/roary_input/"
# Create a list of commands to copy gff files for Roary
cmds_list = ['mkdir roary_input/']

currdir = os.listdir(".")
for a in currdir:
    if 'prokka_JNJ_' in a:
        prok_fold = currfolder+"/"+a+"/"
        gff = [x for x in os.listdir(prok_fold) if '.gff' in x][0]
        copycmd = 'cp {0}{1} {2}{3}.gff'.format(prok_fold,gff,roary_fold,a)
        cmds_list.append(copycmd)

# Create folders and copy files for Roary
for cmd in cmds_list:
    subprocess.call(cmd, shell=True)

# Run Roary
runroary = 'roary -f ./roary_output -e -n -v roary_input/*.gff'
subprocess.call(runroary, shell=True)

# random seed is 12345
# 100 ML searches on 100 randomized stepwise addition parsimony trees
# rapid bootstrapping is that it allows you to do a complete analysis (ML search + Bootstrapping) in one single step by typing
# Run RaxML
raxmlcmd = 'raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -# 100 -s roary_output/core_gene_alignment.aln -n tre'
subprocess.call(raxmlcmd, shell=True)
