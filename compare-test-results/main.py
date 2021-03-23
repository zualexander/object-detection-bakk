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

    # convert confidence string to float
    dataframe['confidence'] = dataframe['confidence'].apply(pd.to_numeric)

    # extract result class from filename CLASS-xxxx.jpg is the file pattern
    dataframe['gt'] = dataframe['filename'].apply(lambda f: FileHandler.get_file_from_path_wo_ext_until_first_dash(f))

    # sort dataframe by filename and then by modelname and then by predicted class name
    dataframe = dataframe.sort_values([
        'filename',
        'model',
        'name'
    ])

    # filter confidence
    dataframe = dataframe[dataframe['confidence'] > 0.9]

    # create class match column
    # dataframe['predicted'] = dataframe.apply(
    #     lambda row: FileHandler.get_file_from_path_wo_ext_until_first_dash(row['filename']) == row['gt'], axis=1)
    print(dataframe.size)
    dataframe = dataframe.query('gt != name')
    print(dataframe.head())

    # print(dataframe)
    dataframe.to_csv('tmp.csv')

    grp = dataframe.groupby([
        'filename',
        'model'
    ])

    # for name, group in grp:
    #     print(group.head(10))

    # grp = dataframe.groupby([
    #     'filename',
    #     'model',
    #     'name',
    #     'relative_coordinates.center_x',
    #     'relative_coordinates.center_y',
    #     'relative_coordinates.width',
    #     'relative_coordinates.height'
    # ])['confidence'].max().to_frame().reset_index()
    # print(grp.head(13))
    # print(grp)
    # for name, group in grp:
    #     print('name', group)
    #     # print(group)
    #     print('___________________________________________--')
