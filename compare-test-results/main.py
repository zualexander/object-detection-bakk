import pathlib
from file_handler import FileHandler
import pandas as pd

IMAGE_RESULTS_PATH = './../test-images/results/'
PATH_TO_PREDICTION_RESULTS = pathlib.Path(IMAGE_RESULTS_PATH)
PREDICTION_RESULT_PATHS = sorted(list(PATH_TO_PREDICTION_RESULTS.glob("*.json")))

if __name__ == '__main__':
    dataframe = pd.DataFrame()
    for result_path in PREDICTION_RESULT_PATHS:
        model_name = FileHandler.get_file_from_path_wo_ext(result_path)
        dataframe = pd.concat([dataframe, FileHandler.readfile_as_dataframe(result_path, model_name)])

    print(dataframe.size)
