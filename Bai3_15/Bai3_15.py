# In[0]: Import and init
import cv2
import numpy as np
from pandas import array
import math


def printArray(array):
    width, height = array.shape
    atype = array.dtype
    if(atype == np.float32):
        for i in range(width):
            print("", end="   ")
            for j in range(height):
                print("%3.2f" % (array[i, j]), end="  ")
            print()
        print()
    else:
        for i in range(width):
            print("", end=" ")
            for j in range(height):
                print("%3d" % (array[i, j]), end="  ")
            print()
        print()


# bw_img = np.array([
#   [0, 0, 0],
#   [0, 1, 0],
#   [0, 0, 0]
# ])
bw_img = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)
print("Origin: ")
printArray(bw_img)
width, height = bw_img.shape

# In[1] get array 1
arrayB = []
for i in range(width):
    for j in range(height):
        if(bw_img[i, j] == 1):
            arrayB.append([i,  j])
arrayB = np.array(arrayB)

# In[2] city block distance transform

# tranform
arrayTransform = np.array([[0 for i in range(width)] for j in range(height)])
lengthB, _ = arrayB.shape
for i in range(width):
    for j in range(height):
        tmp = np.abs(i - arrayB[0][0]) + np.abs(j - arrayB[0][1])
        for k in range(lengthB):
            tmp2 = np.abs(i - arrayB[k][0]) + np.abs(j - arrayB[k][1])
            if tmp2 < tmp:
                tmp = tmp2
        arrayTransform[i, j] = tmp

arrayTransform = np.array(arrayTransform, dtype=np.uint8)
print("City block distance: ")
printArray(arrayTransform)


# In[3] city block distance transform
# tranform
arrayTransform = np.array([[0 for i in range(width)]
                          for j in range(height)], dtype='f')
lengthB, _ = arrayB.shape
for i in range(width):
    for j in range(height):
        tmp = math.sqrt((i - arrayB[0][0])**2 + (j - arrayB[0][1])**2)
        for k in range(lengthB):
            tmp2 = math.sqrt((i - arrayB[k][0])**2 + (j - arrayB[k][1])**2)
            if tmp2 < tmp:
                tmp = tmp2
        arrayTransform[i, j] = tmp
arrayTransform = np.around(arrayTransform, 2)
print("Euclidean distance: ")
printArray(arrayTransform)

# %%
