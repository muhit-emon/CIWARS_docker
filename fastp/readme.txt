Docker usage:

Download this fastp directory on your machine and then cd fastp.
sudo docker build -t fastp . # this will create a docker image named "fastp" for this tool.

To run this docker image you will just run the downloaded bash script with the following instructions.

bash fastp_docker_run_comnd.sh /home/muhitemon/sample_files/f1.fastq /home/muhitemon/sample_files/f2.fastq /home/muhitemon/nf_with_docker/


output files:

Two output files having the substring "_clean" will be generated in /global/path/to/host/input/read/files directory. For the above example, two output files named forward_read_clean.fastq and reverse_read_clean.fastq will be generated in /home/input_paired_end_reads.
