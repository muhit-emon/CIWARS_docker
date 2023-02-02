FROM python:3

WORKDIR /home/Assembly_megahit
RUN mkdir -p /home/Assembly_megahit/input
RUN mkdir -p /home/Assembly_megahit/output

RUN wget https://github.com/voutcn/megahit/releases/download/v1.2.9/MEGAHIT-1.2.9-Linux-x86_64-static.tar.gz
RUN tar zvxf MEGAHIT-1.2.9-Linux-x86_64-static.tar.gz

RUN chmod 777 /home/Assembly_megahit/MEGAHIT-1.2.9-Linux-x86_64-static
RUN chmod 777 /home/Assembly_megahit/MEGAHIT-1.2.9-Linux-x86_64-static/bin
RUN chmod 777 /home/Assembly_megahit/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit
