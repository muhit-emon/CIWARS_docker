Docker usage:

Download this megahit directory on your machine and then cd megahit.
sudo docker build -t megahit . # this will create a docker image named "megahit" for this tool.

To run this docker image you will just run the downloaded bash script with the following instructions.
This bash script takes five(5) command line arguments.

Argument #1 -> The absolute path of file1 (forward file) on your machine.
Argument #2 -> The absolute path of file2 (reverse file) on your machine.
Argument #3 -> The absolute path of a directory on your machine where the output files will be generated.
Argument #4 -> The number of CPUs to be utilized to run this tool.
Argument $5 -> Output file prefix. 

An example run of the bash script is shown below:

bash megahit_docker_run_cmnd.sh /home/muhitemon/sample_files/f1.fastq /home/muhitemon/sample_files/f2.fastq /home/muhitemon/test/ 16 muhit

Here, /home/muhitemon/sample_files/f1.fastq is the file1 (forward file) and /home/muhitemon/sample_files/f2.fastq is the file2 (reverse file).
/home/muhitemon/test/ is the output directory where the output files will be generated.
16 is the number of CPUs to be utilized to run the tool.
muhit is the output prefix.
In the output directory /home/muhitemon/test/, you will find a file named muhit.contigs.fa (here, muhit is the output prefix). This is the output file of this tool.
