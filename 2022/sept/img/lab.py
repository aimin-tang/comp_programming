import math
from images import *

class Kernel:
    def __init__(self, weights):
        """
        for example, weights can be: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        """
        self.height = len(weights)
        self.width = len(weights[0])
        self.weights = weights

class Image:
    def __init__(self, pixels):
        """
        for example, pixels can be: [[1, 2], [3, 4], [5, 6]]
        """
        self.height = len(pixels)
        self.width = len(pixels[0])
        self.pixels = pixels

    def __repr__(self):
        result = f'height: {self.height}\nwidth: {self.width}\npixels: {self.pixels}'
        return result

def round_and_clip_image(image):
    new_pixels = [] 

    for i in range(image.height):
        row = []
        for j in range(image.width):
            if image.pixels[i][j] > 255:
                row.append(255)
            else:
                row.append(int(image.pixels[i][j]))
        new_pixels.append(row)

    return Image(new_pixels)

def invert(image):
    new_pixels = [] 

    for i in range(image.height):
        row = []
        for j in range(image.width):
            row.append(255 - image.pixels[i][j])

        new_pixels.append(row)

    new_image = Image(new_pixels)
    return round_and_clip_image(new_image)

# helper functions for filter
def get_pixel(image, i, j, mode):
    if 0 <= i < image.height and 0 <= j < image.width:
        return image.pixels[i][j]
    else:
        if mode == 'zero':
            return 0
        elif mode == 'wrap':
            if i < 0:
                i += image.height
            if i >= image.height:
                i -= image.height
            if j < 0:
                j += image.width
            if j >= image.width:
                j -= image.width
            return image.pixels[i][j]
        elif mode == 'extend':
            if i < 0:
                i = 0
            if i >= image.height:
                i = image.height - 1
            if j < 0:
                j = 0
            if j >= image.width:
                j = image.width - 1
            return image.pixels[i][j]
        else:
            raise RuntimeError(f'Unknown mode {mode}')

def get_matrix(image, p_height, p_width, mode, kernel):
    matrix = []
    adj_height = p_height - (kernel.height - 1) // 2
    adj_width = p_width - (kernel.width - 1) // 2

    for k_height in range(kernel.height):
        row = []
        for k_width in range(kernel.width):
            i = adj_height + k_height
            j = adj_width + k_width
            row.append(get_pixel(image, i, j, mode))
        matrix.append(row)

    return matrix

def apply_kernel(matrix, kernel):
    pixel = 0

    for i in range(kernel.height):
        for j in range(kernel.width):
            pixel += matrix[i][j] * kernel.weights[i][j]

    return pixel

def filter(image, mode, kernel, round=True):
    new_pixels = []

    for i in range(image.height):
        row = []
        for j in range(image.width):
            matrix = get_matrix(image, i, j, mode, kernel)
            pixel = apply_kernel(matrix, kernel)
            row.append(pixel)
        new_pixels.append(row)

    new_image = Image(new_pixels)
    if round:
        return round_and_clip_image(new_image)
    else:
        return new_image

def get_blur_kernel(n):
    weight = 1 / (n * n)
    weights = [[weight] * n for _ in range(n)]
    return Kernel(weights)

def blur(image, n):
    kernel = get_blur_kernel(n)
    return filter(image, 'extend', kernel)

def sharpen(image, n):
    blurred = blur(image, n)
    new_pixels = []

    for i in range(image.height):
        row = []
        for j in range(image.width):
            pixel = 2 * image.pixels[i][j] - blurred.pixels[i][j]
            row.append(pixel)
        new_pixels.append(row)

    new_image = Image(new_pixels)
    return round_and_clip_image(new_image)

def edges(image):
    kx = Kernel([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    ky = Kernel([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    edgex = filter(image, 'extend', kx, round=False)
    edgey = filter(image, 'extend', ky, round=False)

    pixels = []
    for i in range(image.height):
        row = []
        for j in range(image.width):
            pixelx = edgex.pixels[i][j]
            pixely = edgey.pixels[i][j]
            row.append(math.sqrt(pixelx * pixelx + pixely * pixely))
        pixels.append(row)

    new_image = Image(pixels)
    return round_and_clip_image(new_image)

    
if __name__ == '__main__':
    image1 = Image(i1_data)
    print(image1)
    print(invert(image1))
    k_identity = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print('zero:\n', filter(image1, 'zero', k_identity))
    print('extend:\n', filter(image1, 'extend', k_identity))
    print('wrap:\n', filter(image1, 'wrap', k_identity))
