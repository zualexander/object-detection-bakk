import pathlib

from pipeline import Pipeline

# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('../test-images/images/')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))

p1 = Pipeline('ssd_mobilenet_v1_coco_2017_11_17')
p2 = Pipeline('mask_rcnn_inception_resnet_v2_atrous_coco_2018_01_28')

for image_path in TEST_IMAGE_PATHS:
    p1.predict(image_path)
    p2.predict(image_path)
    break
