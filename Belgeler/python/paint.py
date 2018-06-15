import numpy as np 
import cv2

def nothing(x):
	pass

draw = False
color = []
image = np.zeros((512,512,3) , np.uint8)
cv2.namedWindow('image')

def create_trackbar():
	cv2.createTrackbar('R' , 'image' , 0 , 255 , nothing)
	cv2.createTrackbar('G' , 'image' , 0 , 255 , nothing)
	cv2.createTrackbar('B' , 'image' , 0 , 255 , nothing)

def take_color():
	r = cv2.getTrackbarPos('R' , 'image')
	g = cv2.getTrackbarPos('G' , 'image')
	b = cv2.getTrackbarPos('B' , 'image')
	return [b,g,r]

def drawing(event , x , y , flags , param):
	global draw , color , image
	if event == cv2.EVENT_LBUTTONDOWN:
		draw = True
	elif event == cv2.EVENT_MOUSEMOVE:
		if draw == True:
			cv2.circle(image , (x,y) , 3 , color , -1)
	elif event == cv2.EVENT_LBUTTONUP:
		draw = False
		cv2.circle(image , (x,y) , 3 , color , -1)

def start_fonc():
	global color ,image

	create_trackbar()
	"""
	cv2.createTrackbar('R' , 'image' , 0 , 255 , nothing)
	cv2.createTrackbar('G' , 'image' , 0 , 255 , nothing)
	cv2.createTrackbar('B' , 'image' , 0 , 255 , nothing)
	"""
	while True:
		cv2.imshow('image' , image)
		k = cv2.waitKey(1) & 0xff
		if k == 27:
			break
		elif k == ord('y'):
			cv2.setMouseCallback('image' , drawing)
		elif k == ord('c'):
			color = take_color()
			print(color)
		

	cv2.destroyAllWindow()

if __name__ == '__main__':
	start_fonc()



