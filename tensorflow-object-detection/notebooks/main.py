from predictor import Predictor
import pathlib

# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('../test-images/images/')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))

predictor = Predictor('ssd_mobilenet_v1_coco_2017_11_17')
print(TEST_IMAGE_PATHS)

for image_path in TEST_IMAGE_PATHS:
	print(image_path)
	predictor.predict(image_path)

