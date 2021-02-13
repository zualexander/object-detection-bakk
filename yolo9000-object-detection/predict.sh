#!/usr/bin/sh
sudo rm -rf /main/test-images/results/yolo-9000/*
cd /main/darknet/

for file in /main/test-images/images/*.*; do
	name=${file##*/}
	echo $file
	echo $file >> /main/darknet/data/train.txt
done

sudo ./darknet detector test \
	cfg/combine9k.data cfg/yolo9000.cfg yolo9000.weights \
	-ext_output -dont_show -out /main/test-images/results/yolo-9000.json < data/train.txt