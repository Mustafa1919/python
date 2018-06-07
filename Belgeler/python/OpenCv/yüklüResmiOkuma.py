#-*-coding:utf-8-*-
import numpy as np
import cv2

def main():
    try:
        image = cv2.imread("C:\\Users\\SpooK\\Documents\\image.jpg")
        print(image)
    except Exception as e:
        print("Hata oluştu")
        
if __name__== "__main__":
    main()