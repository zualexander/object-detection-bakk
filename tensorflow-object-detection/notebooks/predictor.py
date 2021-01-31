import numpy as np
import os
import pathlib
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from IPython.display import display

from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

import json

# patch tf1 into `utils.ops`
utils_ops.tf = tf.compat.v1

# Patch the location of gfile
tf.gfile = tf.io.gfile

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = '../models/research/object_detection/data/mscoco_label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)


class Predictor:

    def __init__(self, model_name):
        self.model_name = model_name
        self.model = self.load_model()
        print("loaded")

    def writeToJsonFile(data):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_model(self):
        base_url = '/models/'
        # model_file = self.model_name + '.tar.gz'
        # orig_url = 'http://download.tensorflow.org/models/object_detection/'
        # model_dir = tf.keras.utils.get_file(fname=base_url + model_file, origin=orig_url + model_file, untar=True)
        # model_dir = pathlib.Path(model_dir) / "saved_model"
        # model = tf.keras.models.load_model(base_url + self.model_name + "/saved_model")
        model = tf.saved_model.load(base_url + self.model_name + "/saved_model")
        return model

    def run_inference_for_single_image(self, model, image):
        image = np.asarray(image)
        # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
        input_tensor = tf.convert_to_tensor(image)
        # The model expects a batch of images, so add an axis with `tf.newaxis`.
        input_tensor = input_tensor[tf.newaxis, ...]

        # Run inference
        model_fn = model.signatures['serving_default']
        output_dict = model_fn(input_tensor)

        # All outputs are batches tensors.
        # Convert to numpy arrays, and take index [0] to remove the batch dimension.
        # We're only interested in the first num_detections.
        num_detections = int(output_dict.pop('num_detections'))
        output_dict = {key: value[0, :num_detections].numpy()
                       for key, value in output_dict.items()}
        output_dict['num_detections'] = num_detections

        # detection_classes should be ints.
        output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)

        # Handle models with masks:
        if 'detection_masks' in output_dict:
            # Reframe the the bbox mask to the image size.
            detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                tf.convert_to_tensor(output_dict['detection_masks']), output_dict['detection_boxes'],
                image.shape[0], image.shape[1])
            detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                               tf.uint8)
            output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()

        return output_dict

    def predict(self, image_path):
        print("predict")
        # the array based representation of the image will be used later in order to prepare the
        # result image with boxes and labels on it.
        image_np = np.array(Image.open(image_path))
        # Actual detection.
        output_dict = self.run_inference_for_single_image(self.model, image_np)
        # Visualization of the results of a detection.
        print(output_dict['detection_boxes'],
              output_dict['detection_classes'],
              output_dict['detection_scores'],
              category_index)
        #        vis_util.visualize_boxes_and_labels_on_image_array(
        #            image_np,
        #            output_dict['detection_boxes'],
        #            output_dict['detection_classes'],
        #            output_dict['detection_scores'],
        #            category_index,
        #            instance_masks=output_dict.get('detection_masks_reframed', None),
        #            use_normalized_coordinates=True,
        #            line_thickness=8)
        # isplay(Image.fromarray(image_np))
        return output_dict
