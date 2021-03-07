import json
import os


class FileHandler:

    @staticmethod
    def readfile(file_path):
        with open(file_path) as f:
            return json.load(f)

    # remove the imagepath from the yolo docker-container
    def transform_image_path_of_yolo(img_path):
        return img_path[6:]

    # remove the imagepath from the tf docker-container
    def transform_image_path_of_tf(img_path):
        return img_path[3:]

    @staticmethod
    def add_suffix_to_file(path, filesuffix):
        splitfiles = os.path.splitext(path)
        file_extension = splitfiles[1]
        basepath = os.path.dirname(path)
        filename = os.path.basename(splitfiles[0]) + filesuffix
        new_path = basepath + '/' + filename + file_extension
        return new_path
