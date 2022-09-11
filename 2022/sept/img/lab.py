import os
import json

def load_image(image_name):
    par_dir = os.path.dirname(os.path.realpath(__file__))
    image_file = os.path.join(par_dir, 'images.json')
    with open(image_file) as f:
        images = json.load(f)

    return images['i1']

if __name__ == '__main__':
    print(load_image('i1'))

    

