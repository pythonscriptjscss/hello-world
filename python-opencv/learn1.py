import cv2 as cv
# img = cv.imread("D:\mystudy\pythonOCR\python-opencv\images\h.jpg")
# cv.imshow("Cat",img)
# cv.waitKey(0)

capture = cv.VideoCapture("D:\mystudy\pythonOCR\python-opencv\Videos\eh.mp4")
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord('s'):
        break
capture.release()
cv.destroyAllWindows() 
