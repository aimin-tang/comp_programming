import os
import json

class Image:
    def __init__(self, height, width, pixels) -> None:
        self.height = height
        self.width = width
        self.pixels = pixels

    def __repr__(self):
        return f"height: {self.height}\nwidth: {self.width}\npixels: {self.pixels}"

    def invert(self):
        new_pixels = [255 - pixel for pixel in self.pixels]
        return Image(self.height, self.width, new_pixels)
        

def load_image(image_name):
    par_dir = os.path.dirname(os.path.realpath(__file__))
    image_file = os.path.join(par_dir, 'images.json')
    with open(image_file) as f:
        images = json.load(f)

    image_json = images[image_name]
    return Image(image_json['height'], image_json['width'], image_json['pixels'])

if __name__ == '__main__':
    image_i1 = load_image('i1')
    print(image_i1.invert())

