import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help = "path to the (optional) video file")
args = vars(ap.parse_args())
 
cv2.namedWindow("ori", 0);
cv2.resizeWindow("ori", 400,300);

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    # grab the current frame
    print 'Tu ok'
    (grabbed, frame) = camera.read()
   
    # if we are viewing a video and we did not grab a
    # frame, then we have reached the end of the video
    if args.get("video") and not grabbed:
        break
    # resize the frame, convert it to the HSV color space,
    # and determine the HSV pixel intensities that fall into
    # the speicifed upper and lower boundaries
    #frame = imutils.resize(frame, width = 400)
    cv2.imshow("ori", frame)
camera.release()
cv2.destroyAllWindows()
