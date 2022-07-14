# importing the module
import math

import cv2
x1=270
y1=439
# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		#print(x, ' ', y)
		dist=math.sqrt((x-x1)**2+(y-y1)**2)
		#print(dist)
		mlm=(dist*25.4)/96
		#print(mlm,'mm')
		float=mlm
		format_float="{:.2f}".format(float)
		print(format_float,'mm')
		

		
		

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('gray.jpg', img)

	# checking for right mouse clicks	
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('gray.jpg', img)

# driver function
if __name__=="__main__":

	# reading the image
	img = cv2.imread('gray.jpg', 1)

	# displaying the image
	cv2.imshow('gray.jpg', img)

	# setting mouse handler for the image
	# and calling the click_event() function
	cv2.setMouseCallback('gray.jpg', click_event)

	# wait for a key to be pressed to exit
	cv2.waitKey(0)

	# close the window
	cv2.destroyAllWindows()
