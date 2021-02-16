import cv2
import pathlib
from coords_transformator import Coords_Transformator
from json_loader import JsonLoader

PATH_TO_PREDICTION_RESULTS = pathlib.Path('./../test-images/results/')
PREDICTION_RESULT_PATHS = sorted(list(PATH_TO_PREDICTION_RESULTS.glob("*.json")))

if __name__ == '__main__':
    for result_path in PREDICTION_RESULT_PATHS:
        prediction_data = JsonLoader.readfile(result_path)
        for prediction in prediction_data:
            print(prediction)
            img_path = prediction["filename"]

            if (str(result_path).endswith("yolo-9000.json")):
                img_path = "../" + JsonLoader.transform_image_path_yolo(img_path)
            else:
                img_path = "../" + JsonLoader.transform_image_path_tf(img_path)

            im = cv2.imread(img_path)

            for prediction_object in prediction["objects"]:
                coords_transformer = Coords_Transformator(img_path, prediction_object["relative_coordinates"])
                coords = coords_transformer.get_coords_in_pixels()
                min_tupel = (int(coords['xmin']), int(coords['ymin']))
                max_tupel = (int(coords['xmax']), int(coords['ymax']))

                print(min_tupel, max_tupel)

                im = cv2.rectangle(im, min_tupel, max_tupel, (0, 255, 0))
                im = cv2.putText(im, prediction_object["name"], min_tupel, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

            cv2.imshow("Show", im)
            cv2.imwrite(img_path + ".png", im)
