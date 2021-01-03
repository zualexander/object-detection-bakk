#!/usr/bin/sh
sudo rm -rf /main/test-images/results/*
cd /main/yolo-9000/darknet/

for file in /main/test-images/images/*.*; do
	name=${file##*/}
	echo $file
	# !!!!! WHY DOESNT IT WORK WITH MULTIPLE IMAGES
	sudo ./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../yolo9000-weights/yolo9000.weights $file > /main/test-images/results/${name}.txt
	sudo mv predictions.jpg /main/test-images/results/$name
done
#	sudo ./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../yolo9000-weights/yolo9000.weights $file