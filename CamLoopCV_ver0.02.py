import signal
import numpy as np
import time
from datetime import datetime
import cv2


def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if input("\nReally quit? (y/n)> ").lower().startswith('y'):
            cap.release()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        cap.release()
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)


# store the original SIGINT handler
original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit_gracefully)
    
threshold = 50
result = 0
result2 = 0

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
#cap.set(15,-5) # CV_CAP_PROP_EXPOSURE
#cap.set(11,90) # CV_CAP_PROP_CONTRAST

b,frame = cap.read()

while True:
    start_time = time.time()
    b,frame = cap.read()
    # Azzero l'ultimo pixel perche' e' sempre 240
    frame[:,int(cap.get(3))-1,:] = 0
    data = np.array(frame)
    result =  np.max(data)
    if ( result > threshold):
      time_dat = datetime.now().strftime("%Y-%m-%d_%H:%M:%S:%f")[:-3]
      cv2.imwrite("/tmp/images/" + str(time_dat) + ".png", frame)
      print("Value: %d " % (result))
      file = open("/tmp/images/" + str(time_dat) + ".txt", "w")
      file.close()
    end_time = time.time()
    print("-- %s --" % (end_time - start_time))
    cv2.imshow("frame", frame)
    cv2.waitKey(1)


