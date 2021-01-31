import json


class Persist:
    def __init__(self, file_path):
        self.file_path = file_path
        self.empty_file(file_path)

    def append_to_json(self, data):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def empty_file(file_path):
        f = open(file_path, "w+")
        f.close()
