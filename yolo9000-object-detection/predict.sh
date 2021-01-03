#!/usr/bin/sh
cd /main/yolo-9000/darknet/

for file in /main/test-images/images/*.*; do
	name=${file##*/}
	sudo ./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../yolo9000-weights/yolo9000.weights $file
	sudo rm -rf /main/test-images/results
	sudo mv predictions.jpg /main/test-images/results/$name
done