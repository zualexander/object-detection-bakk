import json
import os
import pandas as pd

pd.set_option('display.max_columns', 9)


class FileHandler:

    @staticmethod
    def readfile_as_dataframe(file_path, model_name):
        with open(file_path) as f:
            data = json.load(f)

        dataframe = pd.json_normalize(data, "objects", 'filename')

        dataframe['model'] = model_name
        dataframe['filename'] = dataframe['filename'].apply(lambda d: FileHandler.transform_image_path_of_yolo(d) if model_name == 'yolo-9000' else FileHandler.transform_image_path_of_tf(d))
        return dataframe

    # remove the imagepath from the yolo docker-container
    @staticmethod
    def transform_image_path_of_yolo(img_path):
        return ".." + img_path[5:]

    # remove the imagepath from the tf docker-container
    @staticmethod
    def transform_image_path_of_tf(img_path):
        return ".." + img_path[3:]

    @staticmethod
    def get_file_from_path_wo_ext(result_path):
        return os.path.splitext(os.path.basename(result_path))[0]

    @staticmethod
    def get_file_from_path_wo_ext_until_first_dash(result_path):
        filename_wo_ext = FileHandler.get_file_from_path_wo_ext(result_path)
        pos = filename_wo_ext.find('-') if filename_wo_ext.find('-') > 0 else len(filename_wo_ext)
        return filename_wo_ext[0:pos]
