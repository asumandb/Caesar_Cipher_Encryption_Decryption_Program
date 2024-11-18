print("Sezar Şifreleme/Çözme Programı")
print("1.Şifreleme")
print("2.Çöz")
print("3. Çıkış")

while True:
    secim = input("Bir Seçenek Girin(1/2/3):")
    if secim == "1":
        metin = input("Şİfrelenecek Metni Girin:")
        kaydirma = int(input("Kaydırma Miktarını Girin:"))

        sifreli_metin = []
        for karakter in metin:
            if karakter.isalpha():
                kaydirma_egik = kaydirma%26
                base = ord("a") if karakter.islower() else ord("A")
                sifreli_karakter = chr((ord(karakter) - base + kaydirma_egik) % 26 + base)
                sifreli_metin.append(sifreli_karakter)

            else: 
                sifreli_metin.append(sifreli_karakter)
        print(f"Şifreli Metin: {sifreli_metin}")

    elif secim == "2":
        metin = input("Çözülecek Metni Girin:")
        kaydirma = int(input("Kaydırma Miktarını Girin:"))

        cozulmus_metin = []
        for karakter in metin:
            if karakter.isalpha():
                kaydirma_egik = -kaydirma%26
                base = ord("a") if karakter.islower() else ord("A")
                cozulmus_karakter = chr((ord(karakter) - base + kaydirma_egik) % 26 + base)
                cozulmus_metin.append(cozulmus_karakter)
            else:
                cozulmus_metin.append(cozulmus_karakter)
        print(f"Çözülen Metin: {cozulmus_metin}")

    elif secim == "3":
        print("Çıkış Yapılıyor...")
        break
