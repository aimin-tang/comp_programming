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

    def round_and_clip_image(self):
        new_pixels = [] 

        for i in range(self.height):
            row = []
            for j in range(self.width):
                if self.pixels[i][j] > 255:
                    row.append(255)
                else:
                    row.append(int(self.pixels[i][j]))
            new_pixels.append(row)

        return Image(new_pixels)

    def invert(self):
        new_pixels = [] 

        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(255 - self.pixels[i][j])

            new_pixels.append(row)

        new_image = Image(new_pixels)
        return new_image.round_and_clip_image()

    def get_pixel(self, i, j, mode):
        if 0 <= i < self.height and 0 <= j < self.width:
            return self.pixels[i][j]
        else:
            if mode == 'zero':
                return 0
            elif mode == 'wrap':
                if i < 0:
                    i += self.height
                if i >= self.height:
                    i -= self.height
                if j < 0:
                    j += self.width
                if j >= self.width:
                    j -= self.width
                return self.pixels[i][j]
            elif mode == 'extend':
                if i < 0:
                    i = 0
                if i >= self.height:
                    i = self.height - 1
                if j < 0:
                    j = 0
                if j >= self.width:
                    j = self.width - 1
                return self.pixels[i][j]
            else:
                raise RuntimeError(f'Unknown mode {mode}')

    def get_matrix(self, p_height, p_width, mode, kernel):
        matrix = []
        adj_height = p_height - (kernel.height - 1) // 2
        adj_width = p_width - (kernel.width - 1) // 2

        for k_height in range(kernel.height):
            row = []
            for k_width in range(kernel.width):
                i = adj_height + k_height
                j = adj_width + k_width
                row.append(self.get_pixel(i, j, mode))
            matrix.append(row)

        return matrix

    def apply_kernel(self, matrix, kernel):
        pixel = 0

        for i in range(kernel.height):
            for j in range(kernel.width):
                pixel += matrix[i][j] * kernel.weights[i][j]

        return pixel

    def filter(self, mode, kernel):
        new_pixels = []

        for height in range(self.height):
            row = []
            for width in range(self.width):
                matrix = self.get_matrix(height, width, mode, kernel)
                pixel = self.apply_kernel(matrix, kernel)
                row.append(pixel)
            new_pixels.append(row)

        new_image = Image(new_pixels)
        return new_image.round_and_clip_image()

if __name__ == '__main__':
    image1 = Image(i1_data)
    print(image1)
    print(image1.invert())
    k_identity = Kernel([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print('zero:\n', image1.filter('zero', k_identity))
    print('extend:\n', image1.filter('extend', k_identity))
    print('wrap:\n', image1.filter('wrap', k_identity))
