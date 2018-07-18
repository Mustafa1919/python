#-*-coding:utf-8-*-
"""
	@Mustafa Şenyurt
	16.07.2018
"""
import os 
from alarm import pomodoro
from time import sleep
def menuOlustur():
	os.system('clr' if os.name == 'nt' else 'clear')

	print('		Ders Çalışma Çizelgesi \n' + 
		  'Pomoro metoduna göre zaman çizelgesi oluşturmaktadır.\n' + 
		  '25 dk çalışma + 5 dk mola şeklinde çizelge oluşturulmaktadır.\n' +
		  'Bu perioddan kaç sefer uygulanacağı sizin seçiminize kalmıştır.\n' + 
		  '2 mod mevcuttur. İlk mod kod yazmak için 3. perioddan sonra 20 dk mola vermekte.\n' + 
		  'İkinci mode ise 4. perioddan sonra 20 dk. lık mola vermektedir.')

	print('\n')
	print('1. Kod yazman modu.\n2. Araştırma modu')
	kontrol = False
	while not kontrol: 
		try:
			secim = int(input('Seçiminiz: '))
			if  secim >= 3 or secim <= 0:
				print('Lütfen menüdeki seçeneklerden birini giriniz.')
			else:
				kontrol = True
				
		except Exception as e:
			print('Lütfen menüdeki seçeneklerden birini giriniz.')

	pomodoro(secim)

	print('Uygulamayı yeniden çalıştırmak istermisiniz?')
	karar = input('Yeniden başlatmak için e / sonlandırmak için h : ')
	if karar.lower() == 'e':
		menuOlustur()
	elif karar.lower() == 'h':
		quit()
	else:
		print('Hatalı giriş yaptınız uygulama kapatılıyor.')
		sleep(5)
		quit()

if __name__ == '__main__':
	menuOlustur()

