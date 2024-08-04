import cv2 as cv

def rescaleFrame(frame,scale=2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

capture = cv.VideoCapture("D:\mystudy\pythonOCR\python-opencv\Videos\eh.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    if not isTrue:
        break
    cv.imshow("Video", frame)
    cv.imshow("video_resized",frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows() 