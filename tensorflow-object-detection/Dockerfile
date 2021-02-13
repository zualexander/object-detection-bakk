#FROM tensorflow/tensorflow:latest-jupyter
FROM tensorflow/tensorflow:latest
ARG DEBIAN_FRONTEND=noninteractive
USER root
WORKDIR /tf

# Install apt dependencies
RUN apt-get update && apt-get install -y \
	apt-utils \
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
	less \
	unzip \
	wget \
	zip && \
	python -m pip install pathlib pycocotools && \
	/usr/local/bin/python -m pip install --upgrade pip && \
	rm -rf /var/lib/apt/lists/*



# Install gcloud and gsutil commands
# https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
	echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
	curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
	apt-get update -y && apt-get install google-cloud-sdk -y


# copy model folder to this folder
RUN git clone https://github.com/tensorflow/models.git


# Compile protobuf configs

RUN (cd /tf/models/research/ && protoc object_detection/protos/*.proto --python_out=.)
WORKDIR /tf/models/research/

RUN cp object_detection/packages/tf2/setup.py ./
ENV PATH="/home/tensorflow/.local/bin:${PATH}"

RUN export PYTHONPATH=$PYTHONPATH:/tf/models/

RUN python -m pip install -U pip
RUN python -m pip install .
RUN pip3 install --user -r /tf/models/official/requirements.txt

ENV TF_CPP_MIN_LOG_LEVEL 3

WORKDIR /models
RUN wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz && \
	tar xf ssd_mobilenet_v1_coco_2017_11_17.tar.gz

RUN wget http://download.tensorflow.org/models/object_detection/mask_rcnn_inception_resnet_v2_atrous_coco_2018_01_28.tar.gz && \
	tar xf mask_rcnn_inception_resnet_v2_atrous_coco_2018_01_28.tar.gz


# maybe not necessary
WORKDIR /tf/notebooks
ENTRYPOINT [ "python", "main.py" ]



