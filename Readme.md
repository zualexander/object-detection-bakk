# practiacl work for bachelor thesis about object detection/image-classification 

## prerequisites
* maven
* docker

## setup tensorflow object detection-api

### with maven
* execute `mvn build-tf` for building the image, and from then on use 
* `mvn run-tf` to run the container
### without maven
* see the commands in the makefile and replace the variable with a manual given name in the command line

### what it does
TBD - should start jupyter notebook with two notebooks which also does recognition in a different folder in the directory

## yolo9000

### with maven
* execute `mvn build-yolo` for building the image, and from then on use 
* `mvn run-yolo` to run the container
### without maven
* see the commands in the makefile and replace the variable with a manual given name in the command line

### what it does
it runs a script for every image in the directory `./test-images/images` and puts the results in `./test-images/results/yolo-9000`

### used repos
* https://github.com/AlexeyAB/darknet/wiki/Using-Yolo9000

# urls for other/different approaches:
 * [tensorflow object detection with tensorflow2 in docker](https://github.com/TannerGilbert/Tensorflow-Object-Detection-with-Tensorflow-2.0)
 * [tensorflow object detection models](https://github.com/tensorflow/models)


* trouble shooting object detection example:
https://github.com/tensorflow/models/issues/9236
https://github.com/tensorflow/models/pull/9430/files
https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects