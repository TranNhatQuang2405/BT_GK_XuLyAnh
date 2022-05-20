import cv2

img1 = cv2.imread('./bg.jpeg')
img2 = cv2.imread('./object.jpg')

# cv2.imshow("img1", img1)
# cv2.waitKey(0)
# cv2.imshow("img2", img2)
# cv2.waitKey(0)

while (True):
    alpha = float(input("Enter alpha value: "))
    dst = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)
    cv2.imwrite('alpha_mask_.png', dst)
    img3 = cv2.imread('alpha_mask_.png')
    cv2.imshow("result", img3)
    cv2.waitKey(0)
    choice = int(input("Enter 1 to continue and 0 to exit: "))
