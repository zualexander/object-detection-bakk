from persist import Persist
from predictor import Predictor


class Pipeline:
     def __init__(self, modelname):
         self.modelname = modelname
         self.result_file = modelname + '.json'
         self.predictor = Predictor(self.modelname)
         self.persister = Persist('../test-images/results/' + self.result_file)

     def predict(self, img_path):
         result = self.predictor.predict(img_path)
         self.persister.append_to_json(result)
