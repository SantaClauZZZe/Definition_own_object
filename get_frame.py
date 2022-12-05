# Сохранить кадр из видео в файл

import cv2 as cv
import matplotlib.pyplot as plt

cv.namedWindow("frames", cv.WINDOW_GUI_NORMAL)

cap = cv.VideoCapture("data_video\\video2.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    _, tresh = cv.threshold(gray, 130, 255, 1)
    
    cv.imshow("frames", tresh)

    key = cv.waitKey(25)
    if key == ord('q'):
        break
    elif key == ord('p'):
        plt.imshow(tresh)
        plt.show()
    elif key == ord('s'):
        plt.imsave("frame.jpg", frame[ :, :, : : -1])

cap.release()
cv.destroyAllWindows()