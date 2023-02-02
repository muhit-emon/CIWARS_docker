#!/bin/bash

f1=$(basename $1) # $1 or the first argument of this bash script should be the host file system absolute path of fw file. This fw file could be quality controlled (optional).
f2=$(basename $2) # $2 or the second argument of this bash script should be the host file system absolute path of rev file. This rev file could be quality controlled (optional).
# $3 or the third argument of this bash script should be the absolute path of the directory on host machine where the output files will be generated.
# $4 or the fourth argument of this bash script is the number of cpus to be utilized.
# $5 or the fifth argument of this bash script is the number of cpus to be utilized.

sudo docker run -v $1:/home/Assembly_megahit/input/$f1 -v $2:/home/Assembly_megahit/input/$f2 -v $3:/home/Assembly_megahit/output megahit ./MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit --presets meta-sensitive -1 ./input/$f1 -2 ./input/$f2 -t $4 -f -o ./output --out-prefix $5

cd $3
sudo rm checkpoints.txt options.json $5.log
sudo rm -r intermediate_contigs
