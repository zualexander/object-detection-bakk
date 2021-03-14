import pathlib
from file_handler import FileHandler

IMAGE_RESULTS_PATH = './../test-images/results/'
PATH_TO_PREDICTION_RESULTS = pathlib.Path(IMAGE_RESULTS_PATH)
PREDICTION_RESULT_PATHS = sorted(list(PATH_TO_PREDICTION_RESULTS.glob("*.json")))

if __name__ == '__main__':
    result_dict = dict()
    for result_path in PREDICTION_RESULT_PATHS:
        model_name = FileHandler.get_file_from_path_wo_ext(result_path)
        dataframe = FileHandler.readfile_as_dataframe(result_path, model_name)
        # result_dict[model_name] = np.array(prediction_data[0])

    print(result_dict)
    # for prediction in prediction_data:
    # img_path = prediction["filename"]
    #
    # if str(result_path).endswith("yolo-9000.json"):
    #     img_path = ".." + FileHandler.transform_image_path_of_yolo(img_path)
    # else:
    #     img_path = ".." + FileHandler.transform_image_path_of_tf(img_path)
    #
    # print(img_path)
    # print(prediction_data)
    #
    # print('\n\n')
