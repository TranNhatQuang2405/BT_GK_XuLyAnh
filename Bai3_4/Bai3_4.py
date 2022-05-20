# %%
import cv2
import numpy as np
import pyautogui


# %% RESIZE function
width, height = pyautogui.size()

# resize fuction


def resize_frame(image, COLOUR=[0, 0, 0]):
    h, w, layers = image.shape
    if h > height:
        ratio = height/h
        image = cv2.resize(
            image, (int(image.shape[1]*ratio), int(image.shape[0]*ratio)))
    h, w, layers = image.shape
    if w > width:
        ratio = width/w
        image = cv2.resize(
            image, (int(image.shape[1]*ratio), int(image.shape[0]*ratio)))
    h, w, layers = image.shape
    if h < height and w < width:
        hless = height/h
        wless = width/w
        if(hless < wless):
            image = cv2.resize(
                image, (int(image.shape[1] * hless), int(image.shape[0] * hless)))
        else:
            image = cv2.resize(
                image, (int(image.shape[1] * wless), int(image.shape[0] * wless)))
    h, w, layers = image.shape
    if h < height:
        df = height - h
        df /= 2
        image = cv2.copyMakeBorder(image, int(df), int(
            df), 0, 0, cv2.BORDER_CONSTANT, value=COLOUR)
    if w < width:
        df = width - w
        df /= 2
        image = cv2.copyMakeBorder(image, 0, 0, int(
            df), int(df), cv2.BORDER_CONSTANT, value=COLOUR)
    image = cv2.resize(image, (1280, 720), interpolation=cv2.INTER_AREA)
    return image


# %% image blue background
image = cv2.imread('./735967.png')
print('Image type: ', type(image),
      'Image Dimensions : ', image.shape)
image = resize_frame(image)
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
lower_blue = np.array([0, 0, 100])  # [R value, G value, B value]
upper_blue = np.array([120, 100, 255])
mask = cv2.inRange(image_copy, lower_blue, upper_blue)
cv2.imshow("img1", mask)
cv2.waitKey(0)

# %% mask image
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
cv2.imshow("a", masked_image)
cv2.waitKey(0)

# %% bakcground image
background_image = cv2.imread('./background.jpg')
background_image = resize_frame(background_image)
crop_background = background_image[0:720, 0:1280]
crop_background[mask == 0] = [0, 0, 0]
cv2.imshow("background", crop_background)
cv2.waitKey(0)

# %% result
masked_image = cv2.cvtColor(masked_image, cv2.COLOR_RGB2BGR)
final_image = crop_background + masked_image
cv2.imshow("result", final_image)
cv2.waitKey(0)
