import cv2
from random import randrange

trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread("test.jpg")
webCam = cv2.VideoCapture(0)
while True:
    frame_read ,frame = webCam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h),(173,74,0) ,5)

    cv2.imshow("face_detector", frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break
        print('code complete')
