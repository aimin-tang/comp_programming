from images import *

class Kernel:
    def __init__(self, height, width, weights):
        self.height = height
        self.width = width
        self.weights = weights

class Image:
    def __init__(self, height, width, pixels):
        self.height = height
        self.width = width
        self.pixels = pixels

    def __repr__(self):
        result = f'height: {self.height}\nwidth: {self.width}\npixels: {self.pixels}'
        return result

    def round_and_clip_image(self):
        new_pixels = [] 
        for pixel in self.pixels:
            if pixel > 255:
                new_pixels.append(255)
            else:
                new_pixels.append(int(pixel))

        return Image(self.height, self.width, new_pixels)

    def invert(self):
        new_pixels = [255 - pixel for pixel in self.pixels]

        new_image = Image(self.height, self.width, new_pixels)
        return new_image.round_and_clip_image()

    def get_pixel(self, p_height, p_width, k_height, k_width, mode):
        return 0

    def get_matrix(self, p_height, p_width, mode, kernel):
        matrix = []

        for k_height in range(kernel.height):
            row = []
            for k_width in range(kernel.width):
                row.append(self.get_pixel(p_height, p_width, k_height, k_width, mode))
            matrix.append(row)

        return matrix

    def filter_pixel(self, matrix, kernel):
        pixel = 0

        for i in range(kernel.height):
            for j in range(kernel.width):
                pixel += matrix[i][j] * kernel.weights[i][j]

        return pixel

    def filter(self, mode, kernel):
        new_pixels = []

        for height in range(self.height):
            for width in range(self.width):
                matrix = self.get_matrix(height, width, mode, kernel)
                pixel = self.filter_pixel(matrix, kernel)
                new_pixels.append(pixel)

        new_image = Image(self.height, self.width, new_pixels)
        return new_image.round_and_clip_image()

if __name__ == '__main__':
    image1 = Image(i1_data['height'], i1_data['width'], i1_data['pixels'])
    print(image1)
    print(image1.invert())
    k_identity = Kernel(3, 3, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(image1.filter('zero', k_identity))
