import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
count_line = 550
min_width_rect = 80
min_height_rect = 80
# InitialiZe Substructor

algo = cv2.createBackgroundSubtractorMOG2()


def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


detect = []
offset = 6
counter = 0

while True:
    ret, frame1 = cap.read()
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    # appplying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatboeing = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatboeing = cv2.morphologyEx(dilatboeing, cv2.MORPH_CLOSE, kernel)
    countershape, h = cv2.findContours(dilatboeing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line), (1200, count_line), (255, 127, 0), 3)

    for (i, c) in enumerate(countershape):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_rect) and (h >= min_height_rect)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "VEHICLE:" + str(counter), (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            if y < (count_line + offset) and y > (count_line - offset):
                counter += 1
                cv2.line(frame1, (25, count_line), (1200, count_line), (0, 127, 255), 3)
                detect.remove((x, y))
                print("Vehicle Counter:" + str(counter))

    cv2.putText(frame1, "VEHICLE COUNTER:" + str(counter), (450, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow('Detector',dilatboeing)

    cv2.imshow('Image', frame1)

    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()
