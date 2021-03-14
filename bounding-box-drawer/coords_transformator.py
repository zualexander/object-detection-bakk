import cv2


class Coords_Transformator:
    def __init__(self, img, relative_coords):
        self.center_x = float(relative_coords['center_x'])
        self.center_y = float(relative_coords['center_y'])
        self.width = float(relative_coords['width'])
        self.height = float(relative_coords['height'])
        img = cv2.imread(img)
        h, w, _ = img.shape
        self.image_height = h
        self.image_width = w

    def get_coords_in_pixels(self):
        return {
            'xmin': (self.center_x * self.image_width) - (self.width / 2) * self.image_width,
            'ymin': (self.center_y * self.image_height) - (self.height / 2) * self.image_height,
            'xmax': (self.center_x * self.image_width) + (self.width / 2) * self.image_width,
            'ymax': (self.center_y * self.image_height) + (self.height / 2) * self.image_height
        }
