# import numpy as np
from PIL import Image

# img_filename = 'input_image.jpg'
# save_filename = 'output_image.jpg'

# ######################################
# # READ IMAGE FROM FILE
# ######################################
# #load file as pillow Image 
# img = Image.open('nature.jpg')

# # convert to grayscale
# imgray = img.convert(mode='L')

# #convert to NumPy array
# img_array = np.asarray(imgray)

# print(img_array.shape)
# ######################################
# # PERFORM HISTOGRAM EQUALIZATION
# ######################################

# """
# STEP 1: Normalized cumulative histogram
# """
# #flatten image array and calculate histogram via binning
# histogram_array = np.bincount(img_array.flatten(), minlength=256)

# #normalize
# num_pixels = np.sum(histogram_array)
# histogram_array = histogram_array/num_pixels

# #normalized cumulative histogram
# chistogram_array = np.cumsum(histogram_array)


# """
# STEP 2: Pixel mapping lookup table
# """
# transform_map = np.floor(255 * chistogram_array).astype(np.uint8)


# """
# STEP 3: Transformation
# """
# # flatten image array into 1D list
# img_list = list(img_array.flatten())

# # transform pixel values to equalize
# eq_img_list = [transform_map[p] for p in img_list]

# # reshape and write back into img_array
# eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)

# ######################################
# # WRITE EQUALIZED IMAGE TO FILE
# ######################################
# #convert NumPy array to pillow Image and write to file
# eq_img = Image.fromarray(eq_img_array, mode='L')
# eq_img.save(save_filename)

import cv2 

# Create a video capture object, in this case we are reading the video from a file
vid_capture = cv2.VideoCapture('sample2.avi')

if (vid_capture.isOpened() == False):
	print("Error opening the video file")
# Read fps and frame count
else:
	# Get frame rate information
	# You can replace 5 with CAP_PROP_FPS as well, they are enumerations
	fps = vid_capture.get(5)
	print('Frames per second : ', fps,'FPS')

	# Get frame count
	# You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
	frame_count = vid_capture.get(7)
	print('Frame count : ', frame_count)

while(vid_capture.isOpened()):
	# vid_capture.read() methods returns a tuple, first element is a bool 
	# and the second is frame
	ret, frame = vid_capture.read()
	if ret == True:
		cv2.imshow('Frame',frame)
		# 20 is in milliseconds, try to increase the value, say 50 and observe
		key = cv2.waitKey(20)
		
		if key == ord('q'):
			break
	else:
		break

# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()