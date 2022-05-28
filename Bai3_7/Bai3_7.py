# %%
from matplotlib import pyplot as plt
import cv2
import numpy as np
import pyautogui
import matplotlib.pyplot as plt


# %% RESIZE function
width, height = pyautogui.size()
width = width/2
height = height/2
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
    image = cv2.resize(image, (640, 375), interpolation=cv2.INTER_AREA)
    return image


img = cv2.imread("./kurumi.jpg")
img = resize_frame(img)

gray = img[:, :, 2]*0.2126 + img[:, :, 1]*0.7152 + img[:, :, 0]*0.0722
gray = gray.astype(np.uint8)
cv2.imshow("Image Origin Gray", gray)
cv2.waitKey(0)

# %%

# Create a histogram array
hist1, bins1 = np.histogram(gray.flatten(), 256, [0, 256])
print('Histogram array...')
print(hist1)
# find the cumulative sum
cms = hist1.cumsum()
print('Cumulative Sum...')
print(cms)
# Normalize the cumulative sum
cms_n = cms*float(hist1.max())/cms.max()
print('Normalized sum...')
print(cms_n)

# Plotting the histogram
plt.plot(cms_n, color='b')
plt.hist(gray.flatten(), 256, [0, 256], color='r')
plt.show()

# Histogram Equalization and its plot
y = cv2.equalizeHist(gray)
hist1, bins1 = np.histogram(y.flatten(), 256, [0, 256])
print('Histogram array...')
print(hist1)
cms = hist1.cumsum()
print('Cumulative Sum...')
print(cms)
cms_n = cms*float(hist1.max())/cms.max()
print('Normalized sum...')
print(cms_n)
plt.plot(cms_n, color='b')
plt.hist(y.flatten(), 256, [0, 256], color='r')
plt.show()

# stacking images
w = np.hstack((gray, y))
# cv2.imshow('Original Image', gray)
cv2.imshow('Transformed Images', w)
cv2.waitKey(0)
