#-*-coding:utf-8-*-
import cv2
import numpy as np

cap = cv2.imread("ferrari.jpeg")

#min ve max renk uzayını ayarlarken mantık tespit edilecek rengin aralığını düşürüp kalanı komple alıyoruz mesela kırmızı için mavi
#ve yeşil rengin tamamını seçtik ve resimdeki bu renkleri siyah yaptık kırmızıda da tonuna göre bir rek aralığı seçerek
#kırmızı rengi belirginleştiriyoruz ve bu kısımda maske de beyaz kalıyor
min_renk=np.array([170,0,0])
max_renk=np.array([180,255,255])
hsvResim = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV) #hsv renk uzayına çeviriyoruz
mask = cv2.inRange(hsvResim,min_renk,max_renk) #imRange metodu resmimizin belirlenen aralıkta olanları siyah diğerlerini beyaz yapar
print(mask)
cv2.erode(mask,np.array([5,5]))
cv2.dilate(mask,np.array([5,5]))
cv2.dilate(mask, np.array([5, 5]))
cv2.erode(mask, np.array([5, 5]))
out = cv2.bitwise_and(cap,cap,mask=mask) #oluşturduğumuz maske ile and işlemi gerçekleştirip istenen renk dışındakileri siyah yapar
cv2.imshow("mask",mask)
cv2.imshow("pencere",cap)
cv2.imshow("Out",out)
#ikilikResim = cv2.inRange()

cv2.waitKey(0)