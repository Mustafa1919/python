# -*- coding: utf-8 -*-  

"""
	@Mustafa Şenyurt
	14.07.2018
"""

import os 

def kelimeKaydet():
	"""
		Sözlüğe yeni kelimeler eklemek için oluşturulan metod
		kelimeyi ve anlamını kullanıcıdan alarak text dosyasına kaydetmektedir.
		y girerek kelime ve anlamını girme sonlandırılmaktadır. 
	"""
	os.system('cls' if os.name =='nt' else 'clear')
	kelime = input('Kelime = ').lower()
	anlam = input('Anlamı = ').lower()
	kontrol = True
	while kontrol:
		swap_anlam = input().lower()
		if swap_anlam.lower() == 'y':
			kontrol = False
		else : 
			anlam = anlam +'BJK' + swap_anlam

	if os.path.isfile('sozluk.txt'):
		sozluk = open('sozluk.txt' , 'a')
	else:
		sozluk = open('sozluk.txt' , 'w')

	sozluk.write(kelime + '->' + anlam + '\n')
	sozluk.close()


