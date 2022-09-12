from lab import *

def test_round_and_clip_image():
    data = [[0, 50.1], [50, 100], [100, 258]]
    image1 = Image(data)
    image2 = round_and_clip_image(image1)
    assert image2.height == 3
    assert image2.width == 2
    assert image2.pixels == [[0, 50], [50, 100], [100, 255]]

def test_invert():
    data = [[0, 50], [50, 100], [100, 255]]
    image1 = Image(data)
    image2 = invert(image1)
    assert image2.height == 3
    assert image2.width == 2
    assert image2.pixels == [[255, 205], [205, 155], [155, 0]]

def test_get_pixel_zero():
    data = [[1, 50], [50, 100], [100, 255]]
    image1 = Image(data)
    pixel = get_pixel(image1, 0, 0, 'zero')
    assert pixel == 1
    pixel = get_pixel(image1, -1, 0, 'zero')
    assert pixel == 0
    pixel = get_pixel(image1, 2, -1, 'zero')
    assert pixel == 0
    pixel = get_pixel(image1, 3, 0, 'zero')
    assert pixel == 0
    pixel = get_pixel(image1, 2, 2, 'zero')
    assert pixel == 0
    pixel = get_pixel(image1, 3, 3, 'zero')
    assert pixel == 0

def test_get_pixel_extend():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    pixel = get_pixel(image1, 0, 0, 'extend')
    assert pixel == 1
    pixel = get_pixel(image1, -1, 0, 'extend')
    assert pixel == 1
    pixel = get_pixel(image1, 2, -1, 'extend')
    assert pixel == 5
    pixel = get_pixel(image1, 3, 0, 'extend')
    assert pixel == 5
    pixel = get_pixel(image1, 2, 2, 'extend')
    assert pixel == 6
    pixel = get_pixel(image1, 3, 3, 'extend')
    assert pixel == 6

def test_get_pixel_wrap():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    pixel = get_pixel(image1, 0, 0, 'wrap')
    assert pixel == 1
    pixel = get_pixel(image1, -1, 0, 'wrap')
    assert pixel == 5
    pixel = get_pixel(image1, 2, -1, 'wrap')
    assert pixel == 6
    pixel = get_pixel(image1, 3, 0, 'wrap')
    assert pixel == 1
    pixel = get_pixel(image1, 2, 2, 'wrap')
    assert pixel == 5
    pixel = get_pixel(image1, 3, 3, 'wrap')
    assert pixel == 2

def test_get_matrix():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    matrix = get_matrix(image1, 0, 0, 'zero', k)
    assert matrix == [[0, 0, 0], [0, 1, 2], [0, 3, 4]]

def test_apply_kernel():
    matrix = [[0, 0, 0], [0, 1, 2], [0, 3, 4]]
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    pixel = apply_kernel(matrix, k)
    assert pixel == 1

def test_filter_zero():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    image2 = filter(image1, 'zero', k)
    assert image2.pixels == [[1, 2], [3, 4], [5, 6]]

def test_filter_extend():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    image2 = filter(image1, 'extend', k)
    assert image2.pixels == [[1, 2], [3, 4], [5, 6]]

def test_filter_wrap():
    data = [[1, 2], [3, 4], [5, 6]]
    image1 = Image(data)
    k = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    image2 = filter(image1, 'wrap', k)
    assert image2.pixels == [[1, 2], [3, 4], [5, 6]]

def test_get_blur_kernel():
    k = get_blur_kernel(3)
    # each weight should be around 0.11
    assert int(k.weights[0][0] * 100) == 11

def test_blur():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    image1 = Image(data)
    image2 = blur(image1, 3)
    assert image2.pixels == [[2, 2, 3], [4, 5, 5], [7, 8, 8], [10, 10, 11], [12, 12, 13]]

def test_sharpen():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    image1 = Image(data)
    image2 = sharpen(image1, 3)
    assert image2.pixels == [[0, 2, 3], [4, 5, 7], [7, 8, 10], [10, 12, 13], [14, 16, 17]]

def test_edges():
    # not confirmed
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    image1 = Image(data)
    image2 = edges(image1)
    assert image2.pixels == [[12, 14, 12], [24, 25, 24], [24, 25, 24], [24, 25, 24], [12, 14, 12]]
