FROM python:3

WORKDIR /home/QC_fastp
RUN mkdir -p /home/QC_fastp/input
RUN mkdir -p /home/QC_fastp/output

RUN wget http://opengene.org/fastp/fastp

RUN chmod 777 /home/QC_fastp/fastp
COPY QC_fastp.py /home/QC_fastp