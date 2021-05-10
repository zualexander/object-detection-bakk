import cv2
import pathlib
from coords_transformator import Coords_Transformator
from file_handler import FileHandler

PATH_TO_PREDICTION_RESULTS = pathlib.Path('./../test-images/results/')
PREDICTION_RESULT_PATHS = sorted(list(PATH_TO_PREDICTION_RESULTS.glob("*.json")))

if __name__ == '__main__':
    for result_path in PREDICTION_RESULT_PATHS:
        prediction_data = FileHandler.readfile(result_path)
        for prediction in prediction_data:
            print(prediction)
            img_path = prediction["filename"]

            if str(result_path).endswith("yolo-9000.json"):
                img_path = "../" + FileHandler.transform_image_path_of_yolo(img_path)
            else:
                img_path = "../" + FileHandler.transform_image_path_of_tf(img_path)

            print(img_path)
            cv_image = cv2.imread(img_path)

            for prediction_object in prediction["objects"]:
                coords_transformer = Coords_Transformator(img_path, prediction_object["relative_coordinates"])
                coords = coords_transformer.get_coords_in_pixels()
                min_tupel = (int(coords['xmin']), int(coords['ymin']))
                max_tupel = (int(coords['xmax']), int(coords['ymax']))

                print(min_tupel, max_tupel)

                cv_image = cv2.rectangle(cv_image, min_tupel, max_tupel, (0, 255, 0))
                cv_image = cv2.putText(cv_image, prediction_object["name"], max_tupel, cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                       (0, 0, 0), 1)

            cv2.imshow("Show", cv_image)
            cv2.imwrite(FileHandler.add_suffix_to_file(img_path, '--bounding-boxes'), cv_image)
