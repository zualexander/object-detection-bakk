import json
from json import JSONEncoder
import numpy as np
from pathlib import PosixPath
import os


class MyEncoder(JSONEncoder):
    def default(self, o):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(o, PosixPath):
            return os.path.abspath(o)
        if isinstance(o, np.int64):
            return str(o)
        if isinstance(o, np.float32):
            return str(o)
        return o.__dict__


class Persist:
    def __init__(self, file_path):
        self.file_path = file_path
        Persist.empty_file(file_path)

    def append_to_json(self, data):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            json.dump(data, f, cls=MyEncoder, ensure_ascii=False, indent=4)

    @staticmethod
    def empty_file(file_path):
        f = open(file_path, "w+")
        f.close()
