Docker usage:

Download this fastp directory on your machine and then cd fastp.
sudo docker build -t fastp . # this will create a docker image named "fastp" for this tool.

To run this docker image you will just run the downloaded bash script with the following instructions.
This bash script takes three(3) command line arguments.

Argument #1 -> The absolute path of file1 (forward file) on your machine.
Argument #2 -> The absolute path of file2 (reverse file) on your machine.
Argument #3 -> The absolute path of a directory on your machine where the output files will be generated. In this directory you will find two output files having the substring "_clean" in their names.

An example run of the bash script is shown below:

bash fastp_docker_run_comnd.sh /home/muhitemon/sample_files/f1.fastq /home/muhitemon/sample_files/f2.fastq /home/muhitemon/fastp_output/

Here, /home/muhitemon/sample_files/f1.fastq is the file1 (forward file) and /home/muhitemon/sample_files/f2.fastq is the file2 (reverse file).
In the directory /home/muhitemon/fastp_output/, two output files named f1_clean.fastq and f2_clean.fastq will be generated.
