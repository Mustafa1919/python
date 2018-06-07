
##elimizdeki bir MP4 videoyu avi formatına çevirdik. İlk önce videoyu okuduk ve yazdırdık
import cv2

videoCapture = cv2.VideoCapture("MyInputVid.MP4") #videomuzu okuduk
fps = videoCapture.get(cv2.CAP_PROP_FPS) #okuduğumuz videonun fps değerini aldık ve alttada pencere boyutlarını aldık
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cv2.CAP_PROP_FRAME_HEIGHT))
#oluşturduğumuz nesne ile yazılacak video adı ve fourcc ile formatın kodlarını fps ve size değerlerini girdik
videoWriter = cv2.VideoWriter("MyOutPutVideo.avi",cv2.VideoWriter_fourcc("I","4","2","0"),fps,size) 
success,frame = videoCapture.read() #videomuzu yazdırdık
while success: #döngü video bitene kadar devam edecek 
    videoWriter.write(frame)
    success,frame = videoCapture.read()

##NOT : Oluşturulan avi formatlı video çalışmadı 

                              