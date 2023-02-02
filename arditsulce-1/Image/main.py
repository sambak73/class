import cv2
import time
video = cv2.VideoCapture(0)
time.sleep(1)
first_frame = None
while True:
    #time.sleep(1)
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_g = cv2.GaussianBlur(gray_frame, (21,21), 0)

    if first_frame is None:
        first_frame = gray_frame_g
    delta_frame = cv2.absdiff(first_frame, gray_frame_g)
    cv2.imshow('My video', delta_frame)
    #cv2.imwrite('capture.png', delta_frame)
    key = cv2.waitKey(1)

    if key == ord('x'):
            #cv2.imwrite('image1.png', frame)
        break
video.release()
#cv2.imwrite('image1.png', frame)


