from lab import Image, Kernel

def test_round_and_clip_image():
    data = [[0, 50.1], [50, 100], [100, 258]]
    image1 = Image(data)
    new_image = image1.round_and_clip_image()
    assert new_image.height == 3
    assert new_image.width == 2
    assert new_image.pixels == [[0, 50], [50, 100], [100, 255]]

def test_invert():
    data = [[0, 50], [50, 100], [100, 255]]
    image1 = Image(data)
    new_image = image1.invert()
    assert new_image.height == 3
    assert new_image.width == 2
    assert new_image.pixels == [[255, 205], [205, 155], [155, 0]]

def test_get_pixel_zero():
    data = [[1, 50], [50, 100], [100, 255]]
    image1 = Image(data)
    pixel = image1.get_pixel(0, 0, 'zero')
    assert pixel == 1
    pixel = image1.get_pixel(-1, 0, 'zero')
    assert pixel == 0
    pixel = image1.get_pixel(2, -1, 'zero')
    assert pixel == 0
    pixel = image1.get_pixel(3, 0, 'zero')
    assert pixel == 0
    pixel = image1.get_pixel(2, 2, 'zero')
    assert pixel == 0
    pixel = image1.get_pixel(3, 3, 'zero')
    assert pixel == 0

def test_get_pixel_extend():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    pixel = image1.get_pixel(0, 0, 'extend')
    assert pixel == 1
    pixel = image1.get_pixel(-1, 0, 'extend')
    assert pixel == 1
    pixel = image1.get_pixel(2, -1, 'extend')
    assert pixel == 5
    pixel = image1.get_pixel(3, 0, 'extend')
    assert pixel == 5
    pixel = image1.get_pixel(2, 2, 'extend')
    assert pixel == 6
    pixel = image1.get_pixel(3, 3, 'extend')
    assert pixel == 6

def test_get_pixel_wrap():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    pixel = image1.get_pixel(0, 0, 'wrap')
    assert pixel == 1
    pixel = image1.get_pixel(-1, 0, 'wrap')
    assert pixel == 5
    pixel = image1.get_pixel(2, -1, 'wrap')
    assert pixel == 6
    pixel = image1.get_pixel(3, 0, 'wrap')
    assert pixel == 1
    pixel = image1.get_pixel(2, 2, 'wrap')
    assert pixel == 5
    pixel = image1.get_pixel(3, 3, 'wrap')
    assert pixel == 2

def test_get_matrix():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    matrix = image1.get_matrix(0, 0, 'zero', k)
    assert matrix == [[0, 0, 0], [0, 1, 2], [0, 3, 4]]

def test_apply_kernel():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    matrix = [[0, 0, 0], [0, 1, 2], [0, 3, 4]]
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    pixel = image1.apply_kernel(matrix, k)
    assert pixel == 1

def test_filter_zero():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    new_image = image1.filter('zero', k)
    assert new_image.pixels == [[1, 2], [3, 4], [5, 6]]

def test_filter_extend():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    new_image = image1.filter('extend', k)
    assert new_image.pixels == [[1, 2], [3, 4], [5, 6]]


