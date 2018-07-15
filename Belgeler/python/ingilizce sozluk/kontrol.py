# -*- coding: utf-8 -*- 
"""
	@Mustafa Şenyurt
	14.07.2018
""" 
import random 
import os


def kelimeKontrol():
	"""
		Kaydedilecek kelime sözlükte var mı yok mu kontrol edilmektedir.
		eğer kelime sözlükte yoksa true
		varsa false döndürmektedir.
	"""
	os.system('cls' if os.name == 'nt' else 'clear')
	kelime , anlam = sozlukDüzenle()
	kontrol = input('Kontrol edilecek kelime : ')
	if kontrol in kelime:
		print('		Bu kelime zaten sozlüğünüzde mevcut.')
		return False
	else:
		print('		Bu kelime sözlüğünüzde mevcut değil.')
		return True


def sozlukDüzenle():
	"""
		Bu metod ile text dosyası okunarak kelimeler ve anlamları 
		ayrı dizilere ayrılmıştır. Daha sonra shuffle edilerek 
		karıştırılarak her defasında farklı düzende gösterilmektedir.
		Bu yöntemle ezberin önüne geçilmektedir.
	"""
	kelimeler , anlamlar = [] , []
	try:
		with open('sozluk.txt' , 'r') as sozluk:
			sozlukVeri = sozluk.read().split('\n')
			if '' in sozlukVeri:
				sozlukVeri.pop(len(sozlukVeri)-1)

			random.shuffle(sozlukVeri)

			for i in sozlukVeri:
				i = i.split('->')
				kelimeler.append(i[0].strip())
				anlamlar.append(i[1])
		return kelimeler , anlamlar

	except Exception as e:
		print('Beklenmedik bir hata oluştu. Oluşan hata : {}'.format(e))



