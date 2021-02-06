from predictor import Predictor
from persist import Persist
import pathlib
import threading

# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('../test-images/images/')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))


class Runner:
    def __init__(self, img_path):
        self.img_path = img_path
        self.modelname = 'ssd_mobilenet_v1_coco_2017_11_17'
        self.modelname2 = 'mask_rcnn_inception_resnet_v2_atrous_coco_2018_01_28'
        self.result_file = self.modelname + '.json'
        self.result_file2 = self.modelname2 + '.json'
        self.model_ssd = Predictor('ssd_mobilenet_v1_coco_2017_11_17')
        self.model_mask = Predictor('mask_rcnn_inception_resnet_v2_atrous_coco_2018_01_28')
        self.persist = Persist('../test-images/results/tensorflow/' + self.result_file)
        self.persist2 = Persist('../test-images/results/tensorflow/' + self.result_file2)

    def p1(self):
        self.persist.append_to_json(self.model_ssd.predict(self.img_path))

    def p2(self):
        self.persist2.append_to_json(self.model_mask.predict(self.img_path))

    def run(self):
        self.p1()
        self.p2()
        # x = threading.Thread(target=self.p1, args=(1,))
        # x2 = threading.Thread(target=self.p2, args=(1,))
        # x.start()
        # x2.start()
        # x.join()
        # x2.join()


for image_path in TEST_IMAGE_PATHS:
    r = Runner(image_path)
    r.run()
    break
