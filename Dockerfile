FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04 

RUN mkdir /src
WORKDIR /src

RUN apt-get update; apt-get -y install python3.10 python3.10-venv python3-pip git curl aria2; 

RUN git clone https://github.com/lewangdev/ChatGLM2-6B; cd /src/ChatGLM2-6B; pip install -r requirements.txt 
