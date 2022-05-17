import cv2
import numpy as np

cap = cv2.VideoCapture(0)



while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    #HSV HUE, SAT, VALUE
    rojo_bajo = np.array([150,150,45])
    rojo_alto = np.array([180,255,150])

    mascara = cv2.inRange(hsv, rojo_bajo, rojo_alto)
    resultado = cv2.bitwise_and(frame, frame, mask= mascara)


    cv2.imshow("Frame", frame)
    cv2.imshow("Mascara", mascara)
    cv2.imshow("Resultado", resultado)

    k = cv2.waitKey(5) & 0xFF
    if k ==27:
        break

cv2.destroyAllWindows()
cap.release()
