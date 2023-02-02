#!/bin/bash

f1=$(basename $1) # $1 or the first argument of this bash script should be the host file system absolute path of fw file
f2=$(basename $2) # $2 or the second argument of this bash script should be the host file system absolute path of rev file
# $3 of the third argument of this bash script should be the host file absolute path where the outputs will be generated

sudo docker run -v $1:/home/QC_fastp/input/$f1 -v $2:/home/QC_fastp/input/$f2 -v $3:/home/QC_fastp/output fastp python3 QC_fastp.py -if input/$f1 -ir input/$f2