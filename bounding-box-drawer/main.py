import pathlib

import cv2
import os

from coords_transformator import Coords_Transformator
from file_handler import FileHandler

IMAGE_PATH = './../test-images/images/'
PATH_TO_IMAGES = pathlib.Path(IMAGE_PATH)

IMAGE_RESULTS_PATH = './../test-images/results/'
PATH_TO_PREDICTION_RESULTS = pathlib.Path(IMAGE_RESULTS_PATH)
PREDICTION_RESULT_PATHS = sorted(list(PATH_TO_PREDICTION_RESULTS.glob("*.json")))

LABEL_COLOR = (255, 20, 147)
RECT_COLOR = (255, 20, 147)
RECT_BORDER_WIDTH = 1
LABEL_FONT_WIDTH = 1

if __name__ == '__main__':
    for result_path in PREDICTION_RESULT_PATHS:
        model_name = FileHandler.get_file_from_path_wo_ext(result_path)

        # delete result directory
        existing_files = os.listdir(PATH_TO_IMAGES.joinpath(model_name))
        for f in existing_files:
            os.remove(os.path.join(PATH_TO_IMAGES.joinpath(model_name), f))

        prediction_data = FileHandler.readfile(result_path)
        for prediction in prediction_data:
            img_path = prediction["filename"]

            if str(result_path).endswith("yolo-9000.json"):
                img_path = FileHandler.transform_image_path_of_yolo(img_path)
            else:
                img_path = FileHandler.transform_image_path_of_tf(img_path)

            cv_image = cv2.imread(img_path)

            for idx, prediction_object in enumerate(prediction["objects"]):
                if (idx > 5):
                    break
                coords_transformer = Coords_Transformator(img_path, prediction_object["relative_coordinates"])
                coords = coords_transformer.get_coords_in_pixels()
                min_tupel = (int(coords['xmin']), int(coords['ymin']))
                max_tupel = (int(coords['xmax']), int(coords['ymax']))
                cv_image = cv2.rectangle(cv_image, min_tupel, max_tupel, RECT_COLOR, RECT_BORDER_WIDTH)
                # black background
                cv_image = cv2.putText(cv_image,
                                       prediction_object["name"] + ' - ' + str(prediction_object['confidence']),
                                       (min_tupel[0] + RECT_BORDER_WIDTH, max_tupel[1] - RECT_BORDER_WIDTH),
                                       cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0), LABEL_FONT_WIDTH*3)
                # real annotation
                cv_image = cv2.putText(cv_image,
                                       prediction_object["name"] + ' - ' + str(prediction_object['confidence']),
                                       (min_tupel[0] + RECT_BORDER_WIDTH, max_tupel[1] - RECT_BORDER_WIDTH),
                                       cv2.FONT_HERSHEY_COMPLEX, 1, LABEL_COLOR, LABEL_FONT_WIDTH)

            cv2.imwrite(
                FileHandler.add_suffix_and_sub_directory(img_path, model_name, '--bounding-boxes'),
                cv_image
            )
