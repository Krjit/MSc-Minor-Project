from statistics import NormalDist
import numpy as np
import cv2
import matplotlib.pyplot as plt
#from skimage import data, filters

# Open Video
cap = cv2.VideoCapture('sample.mp4')

# Randomly select 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=19)
print(frameIds)

# Store selected frames in an array
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    

# Display median frame
cv2.imshow('frame', medianFrame)
cv2.waitKey(0)


# Reset frame number to 0
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Convert background to grayscale
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)

# Loop over all frames
ret = True
frame2 = []
while(ret):   

    # Read frame
    ret, frame = cap.read()

    if ret == False:
        break
    # Convert current frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference of current frame and 
    # the median frame
    dframe = cv2.absdiff(frame, grayMedianFrame)

    # Threshold to binarize
    #th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY)
    
    frame2.append(dframe)

    # # Display image
    # cv2.imshow('frame', dframe)
    # key = cv2.waitKey(15)

    # if key == ord('q'):
    #     break
    



#print(np.asarray(frame2))
mu = np.mean(frame2)
print(mu)

stdv = np.std(frame2)
print(stdv)

th = (mu + 3*stdv)
capture = cv2.VideoCapture("sample2.avi")

if (capture.isOpened() == False):
	print("Error opening the video file")

frame3 = []

while(capture.isOpened()):

    ret, frame = cap.read()
    if ret == False:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame3.append(frame)

capture = cv2.VideoCapture("sample2.avi")

mu = np.mean(frame3)
std = np.std(frame3)

ret = True
while(ret):

    ret, frame = cap.read()
    if ret == False:
        break

    if (mu + 3 * std) > th :
        print ("A object is detect.")
        
        cv2.imshow('Frame',frame)

		# 20 is in milliseconds, try to increase the value, say 50 and observe
        key = cv2.waitKey(20)

        if key == ord('q'):
            break
    else:
        print("Event not occur")

# Release video object
cap.release()

# Release video object
capture.release()

# Destroy all windows
cv2.destroyAllWindows()
