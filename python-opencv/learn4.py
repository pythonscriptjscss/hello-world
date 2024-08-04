import cv2 as cv
img = cv.imread("D:\mystudy\pythonOCR\python-opencv\images\h.jpg")
cv.imshow("Cat",img)

# this function help to convert RGB images to grey images 

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

# this function helps to convert an image to blur

blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) # (3,3) is the kenel size that saya the intensity of blur and it shold be an odd number
cv.imshow('blur',blur)

# this function shows only the edges of the image

edges = cv.Canny(img,125,175)
cv.imshow("edges",edges)

# this function dialated images of te canny images

dialated = cv.dilate(edges,(7,7),iterations=3)
cv.imshow("dialated",dialated)

# this function shows the dialated images into its edges form

eroded = cv.erode(edges,(7,7),iterations=3)
cv.imshow("erodated",eroded)

# this function helps to crop the image

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

resized_ = cv.resize(cv.cvtColor(img,cv.COLOR_BGR2GRAY),(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized_)
cv.waitKey(0)
