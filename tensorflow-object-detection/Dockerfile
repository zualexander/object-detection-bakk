FROM tensorflow/tensorflow:2.2.0-jupyter

ARG DEBIAN_FRONTEND=noninteractive
USER root

# Install apt dependencies
RUN apt-get update && apt-get install -y \
	git \
	lsb-release \
	gpg-agent \
	python3-cairocffi \
	protobuf-compiler \
	python3-pil \
	python3-lxml \
	python3-tk \
	ca-certificates \
	curl \
	git \
#	ssh \
	less \
	unzip \
	wget \
	zip && \
	/usr/local/bin/python -m pip install --upgrade pip && \
	rm -rf /var/lib/apt/lists/*



# Install gcloud and gsutil commands
# https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
	echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
	curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
	apt-get update -y && apt-get install google-cloud-sdk -y

# Add new user to avoid running as root
WORKDIR /tf

RUN git clone https://github.com/tensorflow/models.git

# copy model folder to this folder

# Compile protobuf configs

RUN (cd /tf/models/research/ && protoc object_detection/protos/*.proto --python_out=.)
WORKDIR /tf/models/research/

RUN cp object_detection/packages/tf2/setup.py ./
ENV PATH="/home/tensorflow/.local/bin:${PATH}"

RUN python -m pip install -U pip
RUN python -m pip install .

ENV TF_CPP_MIN_LOG_LEVEL 3


