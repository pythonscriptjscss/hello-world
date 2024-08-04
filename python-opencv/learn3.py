import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # the third attribute includes the color scale 
cv.imshow("Blank",blank)

# blank[:] = 0,255,0
# cv.imshow("pic",blank)

cv.rectangle(blank,(0,0),(250,250),(26,152,56),thickness=2) #thickness = cv.Filled or (-1) -- to fill some color to the rectangle
cv.imshow("Rectangle",blank)
# similarly we can use the cv.circle() function to draw a circle , in this case the parameters required are the blank image , the center , the radius , the color , the thickness
# similarly we have the cv.line() function to draw a line and requies exactly the same parameters

another_blank = np.zeros((500,500,3), dtype='uint8')
cv.putText(another_blank,"Sayan Mandal",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=3)
cv.imshow("text",another_blank)
cv.waitKey(0)

