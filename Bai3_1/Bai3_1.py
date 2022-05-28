from turtle import width
import cv2

# Read Image


def open_image(path):
    image = cv2.imread(path)
    return image

# Get the pixel from the given image


def get_pixel(image, i, j):
    size = image.shape
    width = size[0]
    height = size[1]
    if i > width or j > height:
        return None
    return image[i, j]


# Change Color Balance of the image
def change_color_balance(image, R, G, B):
    # Get size
    size = image.shape
    width = size[0]
    height = size[1]

    # Create new Image and a Pixel Map
    new_image = image.copy()

    # Transform
    for i in range(width):
        for j in range(height):
            pixel = get_pixel(new_image, i, j)
            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0] * R
            green = pixel[1] * G
            blue = pixel[2] * B

            # Set Pixel in new image
            new_image[i, j][0] = red
            new_image[i, j][1] = green
            new_image[i, j][2] = blue

    return new_image


# Load Image (JPEG/JPG needs libjpeg to load)
original = open_image('./image.jpg')

# Const
R = 0.5
G = 0.5
B = 0.5

# Change balance
new = change_color_balance(original, R, G, B)
cv2.imwrite("result.jpg", new)
cv2.imshow("result", new)
cv2.waitKey(0)
