import pathlib
import os
import cv2

from coords_transformator import Coords_Transformator
from file_handler import FileHandler

IMAGE_RESULTS_PATH = './../test-images/results/'
PATH_TO_PREDICTION_RESULTS = pathlib.Path(IMAGE_RESULTS_PATH)
PREDICTION_RESULT_PATHS = sorted(list(PATH_TO_PREDICTION_RESULTS.glob("*.json")))

if __name__ == '__main__':
    for result_path in PREDICTION_RESULT_PATHS:
        model_name = FileHandler.get_file_from_path_wo_ext(result_path)

        # delete result directory
        # os.remove(PATH_TO_PREDICTION_RESULTS.joinpath(model_name + '/*'))
        prediction_data = FileHandler.readfile(result_path)
        for prediction in prediction_data:
            img_path = prediction["filename"]

            if str(result_path).endswith("yolo-9000.json"):
                img_path = ".." + FileHandler.transform_image_path_of_yolo(img_path)
            else:
                img_path = ".." + FileHandler.transform_image_path_of_tf(img_path)

            cv_image = cv2.imread(img_path)

            for prediction_object in prediction["objects"]:
                coords_transformer = Coords_Transformator(img_path, prediction_object["relative_coordinates"])
                coords = coords_transformer.get_coords_in_pixels()
                min_tupel = (int(coords['xmin']), int(coords['ymin']))
                max_tupel = (int(coords['xmax']), int(coords['ymax']))

                cv_image = cv2.rectangle(cv_image, min_tupel, max_tupel, (0, 255, 0))
                cv_image = cv2.putText(cv_image, prediction_object["name"], min_tupel, cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                       (0, 0, 0), 1)

            # cv2.imshow("Show", cv_image)
            cv2.imwrite(
                FileHandler.add_suffix_and_sub_directory(img_path, model_name, '--bounding-boxes'),
                cv_image
            )
