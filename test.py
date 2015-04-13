import numpy as np
import argparse
import cv2
sw_ori=1
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
  help = "path to the (optional) video file")
args = vars(ap.parse_args())

def count(x):
  pass

cv2.namedWindow('tomograph')
cv2.createTrackbar('filtr','tomograph',0,180,count)
cv2.setTrackbarPos('filtr','tomograph',30)


if sw_ori>0:
  cv2.resizeWindow("tomograph", 800,640);

if not args.get("video", False):
  camera = cv2.VideoCapture(0)
else:
  camera = cv2.VideoCapture(args["video"])

while True:
  # grab the current frame
  (grabbed, frame) = camera.read()
  frame = cv2.flip(frame,1)
  if args.get("video") and not grabbed:
    break  #jesli nie wykryl wskazanego filmu

  ori_frame=frame
  if sw_ori>0:
    cv2.imshow("tomograph", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()
