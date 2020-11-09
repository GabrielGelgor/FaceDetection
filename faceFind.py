import cv2 as cv
import time

# define the video to be used:
vidName = input("What is the name of the video you wish to play: ")
vid = cv.VideoCapture("./videos/" + vidName + ".mp4")

try:
    if (vid.read()[1] == None):
        print("File not found!")
        exit(-1)
except:
    print("Video found!")

Faces = []
faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

timeStart = time.time()
count = 0
while True:
    ret, frame = vid.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imwrite("frames/frame%d.jpg" % count, gray) 
    
    img = cv.imread("frames/frame%d.jpg" % count)
    Faces = faceCascade.detectMultiScale(img, 1.3, 5)

    if (len(Faces) >= 2):
        print("Two faces detected at: \n" + str(Faces[0]) + "\n" + str(Faces[1]))
        print("Time taken: " + str(time.time() - timeStart))
        vid.release()
        break