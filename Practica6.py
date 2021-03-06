import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #HSV HUE, SAT, VALUE ROJO    
    rojo_bajo1 = np.array([0,255,20],np.uint8)
    rojo_alto1 = np.array([5,255,255],np.uint8)
    rojo_bajo2 = np.array([175,100,20],np.uint8)
    rojo_alto2 = np.array([179,255,255],np.uint8)

    mascara_rojo = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
    mascara_rojo2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)
    resultado_rojo = cv2.add(mascara_rojo, mascara_rojo2)
    resultado_rojo2 = cv2.bitwise_and(frame, frame, mask= resultado_rojo) 

    #HSV HUE, SAT, VALUE AZUL
    azul_bajo = np.array([100,100,20],np.uint8)
    azul_alto = np.array([125,255,255],np.uint8)

    mascara_azul = cv2.inRange(hsv, azul_bajo, azul_alto)
    resultado_azul = cv2.bitwise_and(frame, frame, mask= mascara_azul)
    
    #HSV HUE, SAT, VALUE AMARILLO
    amarillo_bajo = np.array([15,100,20],np.uint8)
    amarillo_alto = np.array([45,255,255],np.uint8)

    mascara_amarillo = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)
    resultado_amarillo = cv2.bitwise_and(frame, frame, mask= mascara_amarillo)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mascara Rojo", mascara_rojo)
    cv2.imshow("Resultado Rojo", resultado_rojo2)
    cv2.imshow("Mascara Azul", mascara_azul)
    cv2.imshow("Resultado Azul", resultado_azul)
    cv2.imshow("Mascara Amarillo", mascara_amarillo)
    cv2.imshow("Resultado Amarillo", resultado_amarillo)

    k = cv2.waitKey(5) & 0xFF
    if k ==27:
        break

cv2.destroyAllWindows()
cap.release()