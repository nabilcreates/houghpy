import cv2
import numpy

readVideo = cv2.VideoCapture('./video3.mp4')

while True:

    ret, img = readVideo.read()
    
    if ret:
        # Convert to gray first
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Canny the readVideo
        newimg = cv2.Canny(gray, 75, 150)

        # HERE IS WHERE IT DETECTS LINES
        lines = cv2.HoughLinesP(newimg, 1, numpy.pi/180, 50)

        # FOR L IN LINES
        for l in lines:

            # X1,X2,Y1,Y2 IS EQUAL TO THE 4 VALUES IN L[0] BECAUSE L IS AN ARRAY WITHIN AN $
            x1,x2,y1,y2 = l[0]

            # DRAW THE LINES DETECTED
            linedimg = cv2.line(img, (x1,x2), (y1,y2), (255,255,0), 3)

        # Check if the item is in range, so it needs the source and also the lower brightness of the color and the higher brightness of the color
        mask = cv2.inRange(img, numpy.array([255,255,0]), numpy.array([255,255,0]))

        # bitwise is basically masking, first 2 args is source and the mask is the mask
        bitwise = cv2.bitwise_and(img, img, mask=mask)


        cv2.imshow('Edges', bitwise)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

readVideo.release()
cv2.destroyAllWindows()
    