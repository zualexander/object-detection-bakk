FROM jupyter/scipy-notebook

USER root
WORKDIR /main

COPY predict.sh /main/
RUN chmod -R 777 ./
RUN chmod +x predict.sh

RUN apt-get update &&\
	apt-get install -y --no-install-recommends \
	git \
	make && \
	rm -rf /var/lib/apt/lists/*


RUN git clone --recursive https://github.com/philipperemy/yolo-9000.git && \
cd yolo-9000 && \
cat yolo9000-weights/x* > yolo9000-weights/yolo9000.weights 
#&& \
#cd darknet && \
#wget https://pjreddie.com/media/files/yolov3.weights
RUN cd yolo-9000/darknet && \
make

CMD [ "predict.sh" ]



#sed -i s/CUDNN=0/CUDNN=1/g ./darknet/Makefile