import cv2
import numpy

image = cv2.imread('test.jpg')

def detect_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    newimg = cv2.Canny(gray, 75, 150)

    lines = cv2.HoughLinesP(newimg, 1, numpy.pi/180, 300)

    for l in lines:
        x1,x2,y1,y2 = l[0]

        linedimg = cv2.line(image, (x1,x2), (y1,y2), (0,255,0), 3)

        return linedimg
    
while True:

    # Convert to gray first
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny the image
    newimg = cv2.Canny(gray, 75, 150)

    # HERE IS WHERE IT DETECTS LINES
    lines = cv2.HoughLinesP(newimg, 1, numpy.pi/180, 50)

    # FOR L IN LINES
    for l in lines:

        # X1,X2,Y1,Y2 IS EQUAL TO THE 4 VALUES IN L[0] BECAUSE L IS AN ARRAY WITHIN AN ARRAY: [[VAL]] AND L[0] IS: [VAL]
        x1,x2,y1,y2 = l[0]

        # DRAW THE LINES DETECTED
        linedimg = cv2.line(image, (x1,x2), (y1,y2), (0,255,0), 3)

    cv2.imshow('Edges', image)
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
    