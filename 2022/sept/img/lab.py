from images import *

class Image:
    def __init__(self, height, width, pixels):
        self.height = height
        self.width = width
        self.pixels = pixels

    def __repr__(self):
        result = f'height: {self.height}\nwidth: {self.width}\npixels: {self.pixels}'
        return result

    def _round_and_clip_image(self):
        new_pixels = [] 
        for pixel in self.pixels:
            if pixel > 255:
                new_pixels.append(255)
            else:
                new_pixels.append(int(pixel))

        return Image(self.height, self.width, new_pixels)

    def invert(self):
        new_pixels = [255 - pixel for pixel in self.pixels]

        return Image(self.height, self.width, new_pixels)

if __name__ == '__main__':
    image1 = Image(i1_data['height'], i1_data['width'], i1_data['pixels'])
    print(image1)
    print(image1.invert())
