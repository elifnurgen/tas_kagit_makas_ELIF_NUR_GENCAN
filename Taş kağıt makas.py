import random


def tas_kagit_makas_ELIF_NUR_GENCAN():
    while True:
        # Oyundaki seçenekler ve sayaçlar:
        secenekler = ['tas', 'kagit', 'makas']
        galibiyeto1 = 0 # Sizin galibiyet sayınız
        galibiyeto2 = 0 # Rakibin galibiyet sayısı
        tur = 0
        oyun = 1

        while galibiyeto1 <= 2 and galibiyeto2 <= 2:
            oyuncu1 = input(f"Tas mı, \nkagit mi \nmakas mı yoksa oyundan cikis mi?: ")
            oyuncu2 = secenekler[random.randint(0, 2)]
            if oyuncu1 == 'kagit' or oyuncu1 == 'makas' or oyuncu1 == 'tas':
                tur += 1
                if oyuncu1 == "kagit" and oyuncu2 == "tas" or oyuncu1 == "tas" and oyuncu2 == "makas" \
                        or oyuncu1 == "makas" and oyuncu2 == "kagit":
                    galibiyeto1 += 1
                    print(f'Oyuncu2 seçim: {oyuncu2}\nTuru {isim} kazandı.'
                          f'\nTur: {tur} \n{isim}:{galibiyeto1}\nOyuncu2:{galibiyeto2}\n')
                elif oyuncu1 == oyuncu2:
                    print(f'Oyuncu2 seçim: {oyuncu2} \nBerabere kaldınız.'
                          f'\nTur: {tur} \n{isim}:{galibiyeto1}\nOyuncu2:{galibiyeto2}\n')
                else:
                    galibiyeto2 += 1
                    print(f'Oyuncu2 seçim:{oyuncu2}\nTuru oyuncu2 kazandı.'
                          f'\nTur:{tur} \n{isim}:{galibiyeto1} \nOyuncu2:{galibiyeto2}\n')
            elif oyuncu1 == "cikis":
                print("Ne oldu, kaybetmekten mi korktun!:-)")
                exit()
            else:
                print("Geçersiz değer girdiniz. Lütfen tekrar deneyin.")

            while galibiyeto1 == 2 or galibiyeto2 == 2:  # Oyunculardan birisi 2 galibiyete ulaştığında

                if galibiyeto1 == 2:
                    print(f' Oyunu {isim} kazandı.')
                    secim1 = int(input(
                        "Tekrar oynamak ister misiniz?(Seçeneğin SAYISINI giriniz.)\n1- Tekrar\n2- Yeter\nCevabınız:"))
                    secim2 = random.randint(1, 2)
                    print(f'Oyuncu2 : {secim2}')
                    if secim1 == 1 and secim2 == 1:
                        oyun += 1
                        print(f'Oyun tekrar oynanacaktır. Oyun: {oyun}')
                        tas_kagit_makas_ELIF_NUR_GENCAN()
                        return oyun
                    else:
                        print("Oyun bitti.")
                        exit()
                else:
                    print("Oyunu oyuncu2 kazandı.")
                    secim1 = int(input(
                        "Tekrar oynamak ister misiniz?(Seçeneğin SAYISINI giriniz.)\n1- Tekrar\n2- Yeter\nCevabınız:"))
                    secim2 = random.randint(1, 2)
                    print(f'Oyuncu2 : {secim2}')
                    if secim1 == 1 and secim2 == 1:
                        oyun += 1
                        print(f'Oyun tekrar oynanacaktır. Oyun: {oyun}')
                        tas_kagit_makas_ELIF_NUR_GENCAN()
                        return oyun
                    else:
                        print("Oyun bitti.")
                        exit()


# Oyun ve kuralları:
print("Taş Kağıt Makas oyununa hoşgeldiniz."
      "\n Oyunun kuralları:\n "
      "1- Oyunda 3 tane seçeneğiniz vardır:\n tas kagit ve makas \n "
      "2- Oyunun her turunda yukarıdaki seçeneklerden birisi seçebilirsiniz. \n "
      "3- 2 turu kazanan oyuncu oyunu kazanmış olur. İyi oyunlar.")

isim = input("Lütfen isminizi giriniz: ")
while True:
    tas_kagit_makas_ELIF_NUR_GENCAN()
