# Поиск картинки здесь

FRAMES_PER_SECONDS = 25

import cv2 as cv
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

cap = cv.VideoCapture("data_video\\video2.mp4")

cv.namedWindow("frames", cv.WINDOW_GUI_NORMAL)

total_frame_counter = 0

is_my_pict = False
appearance_counter = 0  # Количество раз появления своего "объекта"
min_frame = []
max_frame = []

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    total_frame_counter += 1

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    _, tresh = cv.threshold(gray, 130, 255, 1)
    tresh = cv.dilate(tresh, None, iterations=2)

    labeled = label(tresh)
    props = regionprops(labeled)

#    print(len(props))

    for p in props[:]:
        # print(f"area -> {p.area} ; eccentricity -> {p.eccentricity}")
        if p.area < 1000 or p.area > 3000:
            props.remove(p)

    if len(props) >= 6 and len(props) <= 10:
        cv.putText(frame, f"YOUR PICTURE NOW: time -> {total_frame_counter / FRAMES_PER_SECONDS} ; frame -> {total_frame_counter}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
        if is_my_pict:
            max_frame[-1] = total_frame_counter
        else:
            appearance_counter += 1
            plt.imsave(f"frames\\frame_{appearance_counter}.jpg", frame[ :, :, : : -1])
            min_frame += [total_frame_counter]
            max_frame += [total_frame_counter]
            is_my_pict = True
    else:
        is_my_pict = False

    cv.imshow("frames", frame)

    key = cv.waitKey(FRAMES_PER_SECONDS)
    if key == ord('q'):
        break
    elif key == ord('p'):
        plt.imshow(tresh)
        plt.show()
    elif key == ord('s'):
        plt.imsave("frame.jpg", frame[ :, :, : : -1])

key = cv.waitKey(5)
cap.release()
cv.destroyAllWindows()

print(f"Инфо о появлянии картинки на видео:")
for i in range(len(min_frame)):
    print(f"{i+1} -> Кадры: [{max_frame[i] - min_frame[i]}] Продолжительность: {(max_frame[i] - min_frame[i]) / FRAMES_PER_SECONDS}")