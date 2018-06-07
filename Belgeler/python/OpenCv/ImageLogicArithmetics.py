import cv2
import numpy as np

img1 = cv2.imread("image.jpg")

rows , cols , channels = img1.shape
roi = img1[0:rows,0:cols]

#cv2.imshow("roi",roi)
#cv2.waitKey(0)

img1gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img1gray, 70 , 255 ,cv2.THRESH_BINARY_INV)
#görüntü bozuk olduğu zaman threshold uygulayıp binary yapıyoruz ve alttaki gaus uyguyayıp görüntü düzeltilebilir
#gaus = cv2.adaptiveThreshold(img1gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 115 , 1 )
cv2.imshow("Mask" , mask)

cv2.waitKey(0)
cv2.destroyAllWindows()