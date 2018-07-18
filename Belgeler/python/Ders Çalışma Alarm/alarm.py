#-*-coding:utf-8-*-
"""
	@Mustafa Şenyurt
	16.07.2018
"""
import os 
import tkinter as tk 
from time import sleep

def pomodoro(secim):
	try:
		tekrar = int(input('Kaç tekrar çalışacaksınız.'))
	except ValueError as e:
		print('Lütfen rakam giriniz.')
	except Exception as e:
		print('Beklenmedik bir hata oluştu.')
	tur = 1
	if secim == 1:
		while tur <= tekrar:
			sleep(1500)
			os.system('mpg321 Tehlike_Alarm_Sesi[MP3.support].mp3')
			if tur % 3 == 0 and tur != tekrar:
				sleep(1200)
				os.system('mpg321 Tehlike_Alarm_Sesi[MP3.support].mp3')
			elif tur != tekrar:
				sleep(300)
				os.system('mpg321 Tehlike_Alarm_Sesi[MP3.support].mp3')
			else:
				break
			tur += 1
	elif secim == 2:
		while tur <= tekrar :
			sleep(1500)
			os.system('mpg321 Tehlike_Alarm_Sesi[MP3.support].mp3')
			if tur % 4 == 0 and tur != tekrar:
				window = tk.Tk()
				etiket = 'Lütfen Çalışırken Aldığın \nNotları Tekrar Et'
				lbl = tk.Label(window , text=etiket , fg='black' , bg='white' , font='Helvetica 16 bold italic').pack()
				window.mainloop(50)
				sleep(1200)
				os.system('mpg321 Tehlike_Alarm_Sesi[MP3.support].mp3')
			elif tur != tekrar:
				sleep(300)
				os.system('mpg321 Tehlike_Alarm_Sesi[MP3.support].mp3')
			else:
				break
			tur += 1

	else:
		print('Metoda hatalı bir seçim gönderildi.')



