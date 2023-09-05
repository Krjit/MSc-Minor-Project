
# import cv2
 
# # Opens the inbuilt camera of laptop to capture video.
# cap = cv2.VideoCapture("sample.mp4")
# i = 0
 
# while(cap.isOpened()):
#     ret, frame = cap.read()
    
#     # This condition prevents from infinite looping
#     # incase video ends.
#     if ret == False:
#         break
     
#     # Save Frame by Frame into disk using imwrite method
#     cv2.imwrite('Frame'+str(i)+'.jpg', frame)
#     i += 1

# cap.release()
# cv2.destroyAllWindows()

#-----------------------------------------------------------------------

import numpy as np
import cv2
#from skimage import data, filters

# Open Video

cap = cv2.VideoCapture('sample.mp4')

# Randomly select 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=250)
#print(frameIds)

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
while(ret):   

    # Read frame
    ret, frame = cap.read()

    # Convert current frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference of current frame and the median frame
    dframe = cv2.absdiff(frame, grayMedianFrame)

    # Threshold to binarize
    th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY)
    # print(th)
    
    # Display image
    cv2.imshow('frame', dframe)
    key = cv2.waitKey(15)
    if key == ord('q'):
        break

# Release video object
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
