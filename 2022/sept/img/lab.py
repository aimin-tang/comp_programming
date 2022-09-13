#!/usr/bin/env python3

import math
from re import I

from PIL import Image as Image

# NO ADDITIONAL IMPORTS ALLOWED!


def get_pixel(image, x, y):
    idx = x * image['width'] + y
    return image['pixels'][idx]


def set_pixel(image, x, y, c):
    idx = x * image['width'] + y
    image['pixels'][idx] = c


def apply_per_pixel(image, func):
    result = {
        'height': image['height'],
        'width': image['width'],
        'pixels': [-1 for _ in range(image['height'] * image['width'])],
    }
    for x in range(image['height']):
        for y in range(image['width']):
            color = get_pixel(image, x, y)
            newcolor = func(color)
            set_pixel(result, x, y, newcolor)
    return result


def inverted(image):
    return apply_per_pixel(image, lambda c: 255-c)


# HELPER FUNCTIONS
def get_2d_pixels(w, pixels):
    # turn 1-d list of pixels to a 2-d list
    result = []
    curr = 0
    while curr < len(pixels):
        result.append(pixels[curr:curr+w][:])
        curr += w

    return result

def get_1d_pixels(pixels):
    # turn 2-d list to a 1-d list
    result = []
    for row in pixels:
        result.extend(row[:])

    return result

def calc_new_pixel(image, x, y, boundary_behavior):
    h = image['height']
    w = image['width']
    pixels = get_2d_pixels(w, image['pixels'])

    if 0 <= x < h and 0 <= y < w:
        return pixels[x][y]
    else:
        if boundary_behavior == 'zero':
            return 0
        elif boundary_behavior == 'wrap':
            if x < 0:
                x += h
            if x >= h:
                x -= h
            if y < 0:
                y += w
            if y >= w:
                y -= w
            return pixels[x][y]
        elif boundary_behavior == 'extend':
            if x < 0:
                x = 0
            if x >= h:
                x = h - 1
            if y < 0:
                y = 0
            if y >= w:
                y = w - 1
            return pixels[x][y]
        else:
            return None

def get_matrix(image, px, py, boundary_behavior, kernel):
    n = len(kernel)
    matrix = []
    adj_height = px - (n - 1) // 2
    adj_width = py - (n - 1) // 2

    for kx in range(n):
        row = []
        for ky in range(n):
            i = adj_height + kx
            j = adj_width + ky
            row.append(calc_new_pixel(image, i, j, boundary_behavior))
        matrix.append(row)

    return matrix

def apply_kernel(matrix, kernel):
    pixel = 0
    n = len(kernel)

    for i in range(n):
        for j in range(n):
            pixel += matrix[i][j] * kernel[i][j]

    return pixel

def correlate(image, kernel, boundary_behavior):
    """
    Compute the result of correlating the given image with the given kernel.
    `boundary_behavior` will one of the strings 'zero', 'extend', or 'wrap',
    and this function will treat out-of-bounds pixels as having the value zero,
    the value of the nearest edge, or the value wrapped around the other edge
    of the image, respectively.

    if boundary_behavior is not one of 'zero', 'extend', or 'wrap', return
    None.

    Otherwise, the output of this function should have the same form as a 6.101
    image (a dictionary with 'height', 'width', and 'pixels' keys), but its
    pixel values do not necessarily need to be in the range [0,255], nor do
    they need to be integers (they should not be clipped or rounded at all).

    This process should not mutate the input image; rather, it should create a
    separate structure to represent the output.

    DESCRIBE YOUR KERNEL REPRESENTATION HERE
    it's a 2-d list of n * n
    """
    new_pixels = []

    h = image['height']
    w = image['width']

    for px in range(h):
        row = []
        for py in range(w):
            matrix = get_matrix(image, px, py, boundary_behavior, kernel)
            pixel = apply_kernel(matrix, kernel)
            row.append(pixel)
        new_pixels.append(row)

    print(f"Done: {px} {py}")
    p1d = get_1d_pixels(new_pixels)
    new_image = {'height': h, 'width': w, 'pixels': p1d}
    return new_image


def round_and_clip_image(image):
    """
    Given a dictionary, ensure that the values in the 'pixels' list are all
    integers in the range [0, 255].

    All values should be converted to integers using Python's `round` function.

    Any locations with values higher than 255 in the input should have value
    255 in the output; and any locations with values lower than 0 in the input
    should have value 0 in the output.
    """
    h = image['height']
    w = image['width']
    new_pixels = [] 
    pixels = image['pixels']

    for i in range(len(pixels)):
        if pixels[i] > 255:
            new_pixels.append(255)
        elif pixels[i] < 0: 
            new_pixels.append(0)
        else:
            new_pixels.append(int(pixels[i] + 0.5))

    return {
        'height': h,
        'width': w,
        'pixels': new_pixels,
    }

def get_blur_kernel(n):
    weight = 1 / (n * n)
    weights = [[weight] * n for _ in range(n)]
    return weights

# FILTERS

def blurred(image, n):
    """
    Return a new image representing the result of applying a box blur (with
    kernel size n) to the given input image.

    This process should not mutate the input image; rather, it should create a
    separate structure to represent the output.
    """
    # first, create a representation for the appropriate n-by-n kernel (you may
    # wish to define another helper function for this)
    blur_kernel = get_blur_kernel(n)

    # then compute the correlation of the input image with that kernel
    correlated = correlate(image, blur_kernel, 'extend')

    # and, finally, make sure that the output is a valid image (using the
    # helper function from above) before returning it.
    result = round_and_clip_image(correlated)
    return result

def sharpened(image, n):
    blurred_image = blurred(image, n)
    new_pixels = []
    h = image['height']
    w = image['width']
    pixels = image['pixels']

    for i in range(len(pixels)):
        pixel = 2 * pixels[i] - blurred_image['pixels'][i]
        new_pixels.append(pixel)

    new_image = {'height': h, 'width': w, 'pixels': new_pixels}
    return round_and_clip_image(new_image)

def edges(image):
    kx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    ky = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    h = image['height']
    w = image['width']
    pixels = image['pixels']
    new_pixels = []
    
    edgex = correlate(image, kx, 'extend')
    edgey = correlate(image, ky, 'extend')

    for i in range(len(pixels)):
        pixelx = edgex['pixels'][i]
        pixely = edgey['pixels'][i]
        new_pixels.append(math.sqrt(pixelx * pixelx + pixely * pixely))

    new_image = {'height': h, 'width': w, 'pixels': new_pixels}
    return round_and_clip_image(new_image)

# HELPER FUNCTIONS FOR LOADING AND SAVING IMAGES

def load_greyscale_image(filename):
    """
    Loads an image from the given file and returns a dictionary
    representing that image.  This also performs conversion to greyscale.

    Invoked as, for example:
       i = load_image('test_images/cat.png')
    """
    with open(filename, 'rb') as img_handle:
        img = Image.open(img_handle)
        img_data = img.getdata()
        if img.mode.startswith('RGB'):
            pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2])
                      for p in img_data]
        elif img.mode == 'LA':
            pixels = [p[0] for p in img_data]
        elif img.mode == 'L':
            pixels = list(img_data)
        else:
            raise ValueError('Unsupported image mode: %r' % img.mode)
        w, h = img.size
        return {'height': h, 'width': w, 'pixels': pixels}


def save_greyscale_image(image, filename, mode='PNG'):
    """
    Saves the given image to disk or to a file-like object.  If filename is
    given as a string, the file type will be inferred from the given name.  If
    filename is given as a file-like object, the file type will be determined
    by the 'mode' parameter.
    """
    out = Image.new(mode='L', size=(image['width'], image['height']))
    out.putdata(image['pixels'])
    if isinstance(filename, str):
        out.save(filename)
    else:
        out.save(filename, mode)
    out.close()


if __name__ == '__main__':
    # code in this block will only be run when you explicitly run your script,
    # and not when the tests are being run.  this is a good place for
    # generating images, etc.
    pass
