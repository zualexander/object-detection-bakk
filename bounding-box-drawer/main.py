import cv2
import pathlib
from coords_transformator import Coords_Transformator

PATH_TO_TEST_IMAGES_DIR = pathlib.Path('./../test-images/images/')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))

if __name__ == '__main__':
    for image_path in TEST_IMAGE_PATHS:
        coords_transformer = Coords_Transformator(image_path,
                                                  {
                                                      "center_x": 0.279958,
                                                      "center_y": 0.665772,
                                                      "width": 0.312861,
                                                      "height": 0.658425
                                                  })
        coords = coords_transformer.get_coords_in_pixels()

        min_tupel = (int(coords['xmin']), int(coords['ymin']))
        max_tupel = (int(coords['xmax']), int(coords['ymax']))

        print(min_tupel, max_tupel)

        im = cv2.imread(image_path)
        im = cv2.rectangle(im, min_tupel, max_tupel, (0, 255, 0))
        im = cv2.putText(im, 'text', min_tupel, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
        cv2.imshow("Show", im)
        cv2.imwrite(image_path + 'tmp', im)


def get_list_of_images(self):
