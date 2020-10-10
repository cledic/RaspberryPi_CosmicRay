import numpy as np
import time
import cv2
import glob
import os

threshold = 50

def filebrowser(ext=""):
  "Returns files with an extension"
  return [f for f in glob.glob(f"/tmp/images/*{ext}")]

ftxt = filebrowser(".txt")

# Ciclo per ogni file .TXT che trovo nel folder.
for f in ftxt:

  fimg, _ = os.path.splitext(f)
  fpng = fimg + ".png"
  
  # Cancello il file .TXT
  os.remove(f)
  
  # Proseguo analizzando il file .PNG
  frame = cv2.imread(fpng,0)
  data = np.array(frame)

  if isinstance(data,int) != True:  
    pass

  all_coordinate_x = list(np.where(data >= int(threshold))[1])
  all_coordinate_y = list(np.where(data >= int(threshold))[0])
  all_ziped = list(zip(all_coordinate_x,all_coordinate_y))
  all_ziped.sort()
  
  counter=0
  xy_coordinates = []
  while counter < len(all_ziped):
    if len(all_ziped) == 1:
      xy_coordinates.append(all_ziped[0])
      break
    elif counter == 0:
      xy_coordinates.append(all_ziped[counter])
      counter += 1
    elif all_ziped[counter][0] - 10 < all_ziped[counter - 1][0]:
      counter += 1
    else:
      xy_coordinates.append(all_ziped[counter])
      counter += 1
                  
  sample_save = 0
  
  for x, y in xy_coordinates:
    if x >= 11 and y >= 11:
      img_crop = data[y-10:y + 10,x-10:x + 10]
    else:
      # Gestisco i punti sul bordo immagine.
      if ( x<= 10):
        img_crop = data[y-10:y + 10,0:x + 20]
      else:
        img_crop = data[0:y + 20,x-10:x + 10]
      
    r = 50.0 / img_crop.shape[1]
    dim = (50, int(img_crop.shape[0] * r))
    sample_save = sample_save + 1
    if img_crop is None:
      pass
    else:
      report = fimg+","+str(sample_save)+","+str(x)+","+str(y)+","+str(round(np.average(data), 4))+","+str(np.max(data))+"\n"
      with open( "/tmp/images/Report.lst", "a") as file:
       file.write(report)
      #print(fimg, sample_save, x, y,round(np.average(data), 4), np.max(data),sep=',', file=open( "/tmp/images/Report.lst", "a"))
      img_zoom = cv2.resize(img_crop, dim, interpolation=cv2.INTER_AREA)
      file_name = fimg + "_%i.png" % (sample_save)
      cv2.imwrite(file_name, img_zoom)
      print(file_name)
      

