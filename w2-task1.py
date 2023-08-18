import cv2 as cv
import numpy as np

def main():
    
    image = np.zeros([500, 500, 3])

    pt1 = (350,250)
    pt2 = (450,350)
    B, G, R =125, 50, 255
    colour = (B, G, R)

    cv.line(image, pt1, pt2, colour, 5)
    #cv.rectangle(image, pt1, pt2, colour, 5)

    cv.imshow()
    