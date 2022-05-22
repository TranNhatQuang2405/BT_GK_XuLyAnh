# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Reading the image
img = cv2.imread('nature.jpg')

# Gauusian kernel for sharpening
gaussian_blur = cv2.GaussianBlur(img, (7, 7), 2)

# Sharpening using addweighted()
sharpened1 = cv2.addWeighted(img, 1.5, gaussian_blur, -0.5, 0)
sharpened2 = cv2.addWeighted(img, 3.5, gaussian_blur, -2.5, 0)
sharpened3 = cv2.addWeighted(img, 7.5, gaussian_blur, -6.5, 0)

sharpened1 = cv2.cvtColor(sharpened1, cv2.COLOR_BGR2RGB)
sharpened2 = cv2.cvtColor(sharpened2, cv2.COLOR_BGR2RGB)
sharpened3 = cv2.cvtColor(sharpened3, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

f, axarr = plt.subplots(2, 2, figsize=(15, 15))
axarr[0, 0].imshow(sharpened1)
axarr[0, 0].set_title('Origin')
axarr[0, 1].imshow(sharpened2)
axarr[0, 1].set_title('Sharpened 1')
axarr[1, 0].imshow(sharpened3)
axarr[1, 0].set_title('Sharpened 2')
axarr[1, 1].imshow(sharpened3)
axarr[1, 1].set_title('Sharpened 3')

plt.show()


# reading a image from computer and taking dimensions
img = cv2.imread('noisy.jpg')
rows, cols = img.shape[:2]

# Kernel Blurring using filter2D()
kernel_25 = np.ones((25, 25), np.float32) / 625.0
output_kernel = cv2.filter2D(img, -1, kernel_25)

# Boxfilter and blur function blurring
output_blur = cv2.blur(img, (25, 25))
output_box = cv2.boxFilter(img, -1, (5, 5), normalize=False)

# gaussian Blur
output_gaus = cv2.GaussianBlur(img, (5, 5), 0)

# median Bur (reduction of noise)
output_med = cv2.medianBlur(img, 5)

# Bilateral filtering (Reduction of noise + Preserving of edges)

output_bil = cv2.bilateralFilter(img, 5, 6, 6)

output_kernel = cv2.cvtColor(output_kernel, cv2.COLOR_BGR2RGB)
output_blur = cv2.cvtColor(output_blur, cv2.COLOR_BGR2RGB)
output_box = cv2.cvtColor(output_box, cv2.COLOR_BGR2RGB)
output_gaus = cv2.cvtColor(output_gaus, cv2.COLOR_BGR2RGB)
output_bil = cv2.cvtColor(output_bil, cv2.COLOR_BGR2RGB)
output_med = cv2.cvtColor(output_med, cv2.COLOR_BGR2RGB)


f, axarr = plt.subplots(2, 3, figsize=(15, 15))
axarr[0, 0].imshow(output_kernel)
axarr[0, 0].set_title('kernel blur')
axarr[0, 1].imshow(output_blur)
axarr[0, 1].set_title('Blur() output')
axarr[0, 2].imshow(output_box)
axarr[0, 2].set_title('Box filter')
axarr[1, 0].imshow(output_gaus)
axarr[1, 0].set_title('Gaussian')
axarr[1, 1].imshow(output_bil)
axarr[1, 1].set_title('Bilateral')
axarr[1, 2].imshow(output_med)
axarr[1, 2].set_title('Median Blur')
plt.show()
