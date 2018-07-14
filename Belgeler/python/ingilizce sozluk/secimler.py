# -*- coding: utf-8 -*-  
"""
	@Mustafa Şenyurt
	14.07.2018
"""
import kelimeEkle as ke
from kontrol import kelimeKontrol
import tekrar


def secimler(secim):
	if secim == 1:
		ke.kelimeKaydet()
	elif secim == 2:
		kont = kelimeKontrol()
		input('Enter basınız.')
	elif secim == 3:
		tekrar.listele()
		input('Enter basınız.')
	else:
		print('Niye buraya geldik demekki bir yerde yanlış giriş yapıldı :))')
		

