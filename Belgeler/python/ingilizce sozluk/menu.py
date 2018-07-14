# -*- coding: utf-8 -*-  
"""
	@Mustafa Şenyurt
	14.07.2018
"""
import os 
import secimler


def menu():
	os.system('cls' if os.name=='nt' else 'clear')
	kontrol = True
	print('1.Kelime Ekle\n'+
		  '2.Sözlükte Kelime Kontrol\n'+
		  '3.Sözlükteki Kelimeleri Tekrar Et\n'+
		  '4.Çıkış')
	while kontrol:
		try:
			secim = int(input('Seçiminiz nedir : '))
			if secim > 4 or secim < 1 : 
				print('		Menüde bulunmayan bir seçim seçtiniz. Lütfen menüden bir seçim yapınız.')
			else:
				kontrol = False
		except ValueError:
			print('		Hatalı veri girdiniz. Lütfen menüdeki sayılardan birini giriniz.')
	if secim == 4:
		os.system('cls' if os.name=='nt' else 'clear')
		quit()
	else:
		return secim

while True:
	sec = menu()
	secimler.secimler(sec)


