#!/usr/bin/sh
sudo rm -rf /main/test-images/results/yolo-9000/*
cd /main/darknet/

for file in /main/test-images/images/*.*; do
	name=${file##*/}
	echo $file
	sudo ./darknet detector test \
		cfg/combine9k.data cfg/yolo9000.cfg yolo9000.weights \
		$file \
		-dont_show \
		> /main/test-images/results/yolo-9000/${name}.txt
	sudo mv predictions.jpg /main/test-images/results/yolo-9000/$name
done
#	sudo ./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../yolo9000-weights/yolo9000.weights $file