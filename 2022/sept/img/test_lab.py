from images import image1
from lab import invert

def test_invert():
    new_image = invert(image1['height'], image1['width'], image1['pixels'])
    assert new_image['height'] == 3
    assert new_image['width'] == 2
    assert new_image['pixels'] == [255, 205, 205, 155, 155, 0]
