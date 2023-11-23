FROM bitnami/pytorch

USER 0

RUN apt update && apt upgrade -y

RUN apt-get install git -y

RUN git clone https://github.com/facebookresearch/dinov2.git 

COPY ./datasetFinal.py /app/dinov2

COPY ./labels.txt /app/
