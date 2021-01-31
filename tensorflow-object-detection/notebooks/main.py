from predictor import Predictor
from persist import Persist
import pathlib

# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('../test-images/images/')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))

modelname = 'ssd_mobilenet_v1_coco_2017_11_17'
result_file = modelname + '.json'
predictor = Predictor('ssd_mobilenet_v1_coco_2017_11_17')
persist = Persist('../test-images/results/tensorflow/' + result_file)

for image_path in TEST_IMAGE_PATHS:
    persist.append_to_json(predictor.predict(image_path))
    break
