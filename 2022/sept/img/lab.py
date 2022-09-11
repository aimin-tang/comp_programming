from images import image1

def invert(height, width, pixels):
    new_pixels = [255 - pixel for pixel in pixels]
    return {
        'height': height, 
        'width': width, 
        'pixels': new_pixels
    }

if __name__ == '__main__':
    print(invert(image1['height'], image1['width'], image1['pixels']))
