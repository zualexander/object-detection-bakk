from persist import Persist
from predictor import Predictor


class Pipeline:
    def __init__(self, modelname):
        self.modelname = modelname
        self.result_file = modelname + '.json'
        self.predictor = Predictor(self.modelname)
        self.persister = Persist('../test-images/results/' + self.result_file)
        self.result = []

    def predict(self, img_path):
        prediction_result = self.predictor.predict(img_path)
        self.result.append(prediction_result)

    def persist(self):
        self.persister.append_to_json(self.result)
