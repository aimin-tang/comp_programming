from images import *
from lab import Image

def test_invert():
    image1 = Image(i1_data['height'], i1_data['width'], i1_data['pixels'])
    new_image = image1.invert()
    assert new_image.height == 3
    assert new_image.width == 2
    assert new_image.pixels == [255, 205, 205, 155, 155, 0]
