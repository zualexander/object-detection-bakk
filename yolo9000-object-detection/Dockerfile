FROM jupyter/scipy-notebook

USER root
WORKDIR /main

# copy automated prediction script
COPY predict.sh /main/
RUN chmod -R 777 ./
RUN chmod +x predict.sh


# install dependencies
RUN apt-get update &&\
	apt-get install -y --no-install-recommends \
	git \
	make && \
	rm -rf /var/lib/apt/lists/*

# clone and build darknet
RUN git clone https://github.com/AlexeyAB/darknet.git
WORKDIR /main/darknet
RUN sed -i -e 's/OPENCV=0/OPENCEV=1/' -e 's/DEBUG=0/DEBUG=1/' Makefile
RUN make

RUN wget http://pjreddie.com/media/files/yolo9000.weights
RUN wget https://github.com/AlexeyAB/darknet/blob/617cf313ccb1fe005db3f7d88dec04a04bd97cc2/cfg/yolo9000.cfg#L217-L218
RUN wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/build/darknet/x64/data/combine9k.data

WORKDIR /main/darknet/data
RUN wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/build/darknet/x64/data/9k.labels
RUN wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/build/darknet/x64/data/9k.names
RUN wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/build/darknet/x64/data/inet9k.map

WORKDIR /main

CMD [ "./predict.sh" ]