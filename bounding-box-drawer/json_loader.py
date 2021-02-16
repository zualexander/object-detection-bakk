import json


class JsonLoader:

    @staticmethod
    def readfile(file_path):
        with open(file_path) as f:
            return json.load(f)

    # remove the imagepath from the yolo docker-container
    def transform_image_path_yolo(img_path):
        return img_path[5:]

    # remove the imagepath from the tf docker-container
    def transform_image_path_tf(img_path):
        return img_path[3:]
