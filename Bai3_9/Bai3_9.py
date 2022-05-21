# %% import
import cv2
import numpy as np

img1_path = "./image.jpg"
img = cv2.imread(img1_path)
img2 = cv2.resize(img, (600, 600))


# In[1]. Make black border
old_image_height, old_image_width, channels = img2.shape
new_image_width = 620
new_image_height = 620
color = (0, 0, 0)
new_img = np.full((new_image_height, new_image_width,
                   channels), color, dtype=np.uint8)

# compute center offset
x_center = (new_image_width - old_image_width) // 2
y_center = (new_image_height - old_image_height) // 2

# copy img image into center of result image
new_img[y_center:y_center+old_image_height,
        x_center:x_center+old_image_width] = img2

cv2.imshow("result", new_img)
cv2.imwrite("BlackBorder.jpg", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]. Make Constant border

old_image_height, old_image_width, channels = img2.shape
new_image_width = 620
new_image_height = 620
color = (256, 200, 0)
new_img = np.full((new_image_height, new_image_width,
                   channels), color, dtype=np.uint8)

# compute center offset
x_center = (new_image_width - old_image_width) // 2
y_center = (new_image_height - old_image_height) // 2

# copy img image into center of result image
new_img[y_center:y_center+old_image_height,
        x_center:x_center+old_image_width] = img2

cv2.imshow("result", new_img)
cv2.imwrite("Constant.jpg", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# In[3].  Make Clamp border
old_image_height, old_image_width, channels = img2.shape
new_image_width = 640
new_image_height = 640
new_img = np.zeros((new_image_height, new_image_width, 3), np.uint8)

for i in range(new_image_height):
    for j in range(new_image_width):
        k = np.max([0, np.min([599, i-20])])
        l = np.max([0, np.min([599, j-20])])
        new_img[i, j][0] = img2[k, l][0]
        new_img[i, j][1] = img2[k, l][1]
        new_img[i, j][2] = img2[k, l][2]

cv2.imshow('Clamp padded', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[4] Make Wrap border
old_image_height, old_image_width, channels = img2.shape
paddle_width = int(50)
paddle_height = int(50)
new_image_width = old_image_width + paddle_width*2
new_image_height = old_image_height + paddle_height*2
new_img = np.zeros((new_image_height, new_image_width, 3), np.uint8)

# image = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_WRAP, None)
for i in range(new_image_height):
    for j in range(new_image_width):
        if (i > paddle_height):
            k = int((i - paddle_height) % old_image_height)
        else:
            k = old_image_height - 1 - paddle_height + (i % old_image_height)
        if (j > paddle_width):
            l = int((j - paddle_width) % old_image_width)
        else:
            l = old_image_width - 1 - paddle_width + (j % old_image_width)
        new_img[i, j][0] = img2[k, l][0]
        new_img[i, j][1] = img2[k, l][1]
        new_img[i, j][2] = img2[k, l][2]

cv2.imshow('Wrap padded', new_img)
cv2.imwrite("Wrap.jpg", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[5] Make Mirror border
old_image_height, old_image_width, channels = img2.shape
paddle_width = int(50)
paddle_height = int(50)
new_image_width = old_image_width + paddle_width*2
new_image_height = old_image_height + paddle_height*2
new_img = np.zeros((new_image_height, new_image_width, 3), np.uint8)
for i in range(new_image_height):
    for j in range(new_image_width):
        if(i >= paddle_height + old_image_height):
            k = old_image_height - 1 - \
                int((i - paddle_height) % old_image_height)
        elif (i > paddle_height):
            k = int((i - paddle_height) % old_image_height)
        else:
            k = old_image_height - 1 - \
                (old_image_height - 1 - paddle_height + (i % old_image_height))
        if(j >= paddle_width + old_image_width):
            l = old_image_width - 1 - int((j - paddle_width) % old_image_width)
        elif (j > paddle_width):
            l = int((j - paddle_width) % old_image_width)
        else:
            l = old_image_width - 1 - \
                (old_image_width - 1 - paddle_width + (j % old_image_width))
        new_img[i, j][0] = img2[k, l][0]
        new_img[i, j][1] = img2[k, l][1]
        new_img[i, j][2] = img2[k, l][2]
# new_img = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_REFLECT, None)

cv2.imshow('Mirror padded', new_img)
cv2.imwrite("Mirror.jpg", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
