# import the necessary packages
from __future__ import print_function
from photoboothapp import PhotoBoothApp
from imutils.video import VideoStream
import argparse
import time
 
# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(0).start()
time.sleep(2.0)

output="output"

# start the app
pba = PhotoBoothApp(vs,output)
pba.root.mainloop()
