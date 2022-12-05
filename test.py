# Тестовый файл для попыток поиска картинки

import cv2 as cv
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

cv.namedWindow("frames", cv.WINDOW_GUI_NORMAL)
frame = plt.imread("frame.jpg")

frame = frame[:, :, : : -1]

gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

_, tresh = cv.threshold(gray, 130, 255, 1)

# tresh = cv.erode(tresh, None, iterations=1)
tresh = cv.dilate(tresh, None, iterations=2)
# tresh = cv.erode(tresh, None, iterations=3)

labeled = label(tresh)
props = regionprops(labeled)

for p in props[:]:
    # print(f"area -> {p.area} ; eccentricity -> {p.eccentricity}")
    if p.area < 1000 or p.area > 3000:
        props.remove(p)

print(len(props))

for p in props:
    print(f"area -> {p.area} ; eccentricity -> {p.eccentricity}")

plt.imshow(tresh)
plt.show()
cv.imshow("Frames", tresh)

key = cv.waitKey(0)
cv.destroyAllWindows()