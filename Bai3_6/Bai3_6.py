import cv2


def BrightnessContrast(brightness=0):
    brightness = cv2.getTrackbarPos('Brightness',
                                    'Color Balance')
    contrast = cv2.getTrackbarPos('Contrast',
                                  'Color Balance')
    img = original.copy()

    effect = controller(img, brightness,
                        contrast)
    cv2.imshow('Effect', effect)


def controller(img, brightness=255,
               contrast=127):

    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    Alpha = 0
    Gamma = 0
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness

        Alpha = (max - shadow) / 255
        Gamma = shadow
        cal = cv2.addWeighted(img, Alpha,
                              img, 0, Gamma)
    else:
        cal = img
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
        cal = cv2.addWeighted(cal, Alpha,
                              cal, 0, Gamma)
        cv2.putText(cal, 'A:{},G:{}'.format(round(Alpha, 2),
                                            round(Gamma, 2)), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return cal


if __name__ == '__main__':
    original = cv2.imread("./image.jpg")

    img = original.copy()
    cv2.namedWindow('Color Balance')
    cv2.imshow('Color Balance', original)
    cv2.createTrackbar('Brightness',
                       'Color Balance', 255, 2 * 255,
                       BrightnessContrast)
    cv2.createTrackbar('Contrast', 'Color Balance',
                       127, 2 * 127,
                       BrightnessContrast)
cv2.waitKey(0)
