FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

WORKDIR /home/pytorch/ 

COPY . .

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install python3-pip python3 python3-opencv -y

RUN pip install -r yolov5/requirements.txt
RUN pip install -r requirements.txt
RUN pip install coremltools
RUN pip install Cython --install-option="--no-cython-compile"
