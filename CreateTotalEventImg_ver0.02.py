import numpy as np
import time
import cv2
import glob
import os

threshold = 50
firstTime = True

def filebrowser(ext=""):
  "Returns files with an extension"
  return [f for f in glob.glob(f"/tmp/images/*{ext}")]

fpng = filebrowser(".png")

# Ciclo per ogni file .PNG che trovo nel folder.
for f in fpng:

  fimg, _ = os.path.splitext(f)
  if fimg.count("_") == 2:
    continue

  if ("totalEvent" in fimg) == True:
    continue

  frame = cv2.imread(f, 0)
  
  if firstTime == True:
    ftot = frame
    firstTime = False
    
  ftot = cv2.add(frame,ftot)
  print(f)
  
cv2.imwrite( "/tmp/images/totalEvent.png", ftot)
print("/tmp/images/totalEvent.png")


