import json
import os


class FileHandler:

    @staticmethod
    def readfile(file_path):
        with open(file_path) as f:
            return json.load(f)

    # remove the imagepath from the yolo docker-container
    def transform_image_path_of_yolo(img_path):
        return ".." + img_path[5:]

    # remove the imagepath from the tf docker-container
    def transform_image_path_of_tf(img_path):
        return ".." + img_path[3:]

    @staticmethod
    def add_suffix_and_sub_directory(path, subdir_path, filesuffix):
        splitfiles = os.path.splitext(path)
        file_extension = splitfiles[1]
        basepath = os.path.dirname(path)
        filename = os.path.basename(splitfiles[0]) + filesuffix
        new_path = basepath + '/' + subdir_path + '/' + filename + file_extension
        return new_path

    @staticmethod
    def get_file_from_path_wo_ext(result_path):
        return os.path.splitext(os.path.basename(result_path))[0]
