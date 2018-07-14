# -*- coding: utf-8 -*-  
"""
	@Mustafa Şenyurt
	14.07.2018
"""
import os 
from kontrol import sozlukDüzenle

os.system('cls' if os.name == 'nt' else 'clear')

def listele():
	"""
		Bu metod ile sözlüğümüzden bulunan kelimeler tekrar etmek amacıyla 
		sırayla listelenmektedir.
		İlk önce kelime görüntülenmektedir.
		Enter'a basarak anlamıda görüntülenmektedir.
		Kelime ve anlamı aynı anda görüntülenmeyerek tahmin için süre
		oluşturulmaktadır.
	"""
	kelimeler , anlamlar = sozlukDüzenle()
	os.system('cls' if os.name == 'nt' else 'clear')
	for i in range(len(kelimeler)):
		print(kelimeler[i] + ' -->')
		input()
		anlam = anlamlar[i].split('BJK')
		for j in range(len(anlam)):
			print('	{}. {}'.format(j+1 , anlam[j]))
		print('\n')

