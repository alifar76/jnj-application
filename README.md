# jnj-application

Background
------

JNJ Application assignment

System specs & required packages
------

All analysis were done on MacBook Pro, OS X El Capitan, Version 10.11.4. I used conda 4.1.6 with Python 2.7.12. Following Python packages were used:

- [pandas 0.18.1](http://pandas.pydata.org/)
- [wget 3.2](https://pypi.python.org/pypi/wget)
- [Biopython 1.68](http://biopython.org/)

How to use
------

There are three scripts in the code folder. They are called:

- ```task_a.py```
- ```task_b.py```
- ```task_c.py```

Each script requires certain programs to be installed on the system, the details of which are in the assignment document. Relevant result output files are in the folder ```results```.


Task A
------

The output of ```task_a.py``` is a file called ```task-a-result.csv```, as per specification.


Task B
------

The script, ```task_b.py```, produces a number of files including a few .tre files. The file called ```RAxML_bipartitionsBranchLabels.tre``` can be opened and viewed with Dendroscope. The dendogram image file is called ```RAxML_bipartitionsBranchLabels_Faruqi.png```. 

Task C
------

The name of the paper and the two bacterial strains mentioned in that paper are part of the docstrings of ```task_c.py``` script. The script retrieves data from NCBI and runs progressiveMauve to produce an output file called ```clostridia.xmfa```.

The .xmfa file was viewed in Mauve and the resulting figure is called ```Task_C.png```.

Additionally, I'm running WebACT for this comparison. It can be accessed [here](http://www.webact.org/WebACT/generate?CGISESSID=8666a6010a5b4bd92ae2de7a323ecc91&rm=mode3).
