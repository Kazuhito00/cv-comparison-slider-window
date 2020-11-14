import copy
import numpy as np
import cv2 as cv

from cvstacksliderwindow import CvStackSliderWindow


def main():
    cvwindow = CvStackSliderWindow(
        window_name='debug',
        line_color=(255, 255, 255),
        line_thickness=1,
    )

    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv.resize(frame, (960, 540))
        original_frame = copy.deepcopy(frame)

        frame = cv.Canny(frame, 100, 100)
        frame = cv.cvtColor(frame, cv.COLOR_GRAY2BGR)

        cvwindow.imshow(original_frame, frame)
        key = cv.waitKey(1)
        if key == 27:  # ESC
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()