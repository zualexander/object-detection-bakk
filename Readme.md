# practiacl work for bachelor thesis about object detection/image-classification 

## prerequisites
* maven
* docker
* python3

## build environments for models
`make build`

## execute prediction pipeline
`make run`

### what it does
it runs a script for every image in the directory `./test-images/images` and puts the results in `./test-images/results/__MODEL_NAME__`

## further commands for bounding box drawers and result observation
### bounding boxes:
exeucte `python3 main.py` in the `bounding-box-drawer` directory, to create bounding box images versions in the image directory for each model

### dataframe
create a pandas dataframe of results and save it as tmp.csv in the `compare-test-results` directory.
change into this directory and execute `python3 main.py`

### used repos
* https://github.com/AlexeyAB/darknet/wiki/Using-Yolo9000
* https://github.com/tensorflow/models

* trouble shooting object detection example:
https://github.com/tensorflow/models/issues/9236
https://github.com/tensorflow/models/pull/9430/files
https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects