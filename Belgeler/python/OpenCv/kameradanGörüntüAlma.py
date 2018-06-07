#-*-coding:utf-8-*-
import numpy as np
import cv2


def main():
    try:
        screen = cv2.VideoCapture(0)
        while True:  
            kontrol , frame = screen.read()
            cv2.imshow("frame",frame)
            array=np.array(frame)
            print("{} ass {}".format(frame,array))
            if cv2.waitKey(1) & 0xff == ord("q"):
                screen.release()
                cv2.destroyAllWindows()
    except Exception as e:
        print("hata")
if __name__ == "__main__":
    main()