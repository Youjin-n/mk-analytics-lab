ogrenciler = {
    "Ayşe": 85,
    "Mehmet": 90,
    "Ali": 78,
    "Fatma": 92,
    "Ahmet": 88
}


def ogrenci_ekleme():
    while True:
        input_ismi = input("Öğrenci ismi: ").strip()
        if input_ismi == "":
            print("❌ İsim boş olamaz.")
            continue
        if input_ismi in ogrenciler:
            print(f"⚠️ {input_ismi} zaten mevcut.")
            continue
        try:
            input_notu = int(input("Öğrenci notu: "))
            if not (0 <= input_notu <= 100):
                print("❌ Not 0 ile 100 arasında olmalıdır.")
                continue
        except ValueError:
            print("❌ Lütfen geçerli bir not girin.")
            continue
        
        ogrenciler[input_ismi] = input_notu
        print(f"✅ {input_ismi} başarıyla eklendi! (Not: {input_notu})")
        break


def ogrenci_silme():
    input_ismi = input("Silinecek öğrenci ismi: ")
    not_ = ogrenciler.pop(input_ismi, None)
    
    if not_:
        print(f"✅ {input_ismi} başarıyla silindi! (Not: {not_})")
    else:
        print(f"❌ {input_ismi} bulunamadı.")


def update_ogrenci_notu():
    while True:
        input_ismi = input("Notu güncellenecek öğrenci ismi: ")
        if input_ismi not in ogrenciler:
            print(f"❌ {input_ismi} bulunamadı.")
            continue
        
        eski_not = ogrenciler[input_ismi]
        
        try:
            input_notu = int(input("Yeni not: "))
            if not (0 <= input_notu <= 100):
                print("❌ Not 0 ile 100 arasında olmalıdır.")
                continue
        except ValueError:
            print("❌ Lütfen geçerli bir not girin.")
            continue
        
        ogrenciler[input_ismi] = input_notu
        print(f"✅ {input_ismi} notu güncellendi! ({eski_not} → {input_notu})")
        break


def ogrenci_ara():
    input_ismi = input("Aranacak öğrenci ismi: ")
    not_ = ogrenciler.get(input_ismi, None)
    
    if not_ is not None:
        print(f"📊 {input_ismi}: {not_}")
    else:
        print(f"❌ {input_ismi} bulunamadı.")


def ogrenci_listele():
    if not ogrenciler:
        print("📭 Henüz öğrenci yok!")
        return
    
    print("\n=== ÖĞRENCİ LİSTESİ ===")
    for i, (isim, not_) in enumerate(ogrenciler.items(), 1):
        print(f"{i}. {isim}: {not_}")
    print(f"\nToplam: {len(ogrenciler)} öğrenci")


def main():
    while True:
        print("\n=== ÖĞRENCİ NOT SİSTEMİ ===")
        print("1. Öğrenci Ekle")
        print("2. Öğrenci Sil")
        print("3. Not Güncelle")
        print("4. Öğrenci Ara")
        print("5. Öğrenci Listele")
        print("6. Çıkış")
        
        secim = input("Seçiminiz (1-6): ")
        
        if secim == "1":
            ogrenci_ekleme()
        elif secim == "2":
            ogrenci_silme()
        elif secim == "3":
            update_ogrenci_notu()
        elif secim == "4":
            ogrenci_ara()
        elif secim == "5":
            ogrenci_listele()
        elif secim == "6":
            print("👋 Çıkılıyor...")
            break
        else:
            print("❌ Geçersiz seçim. Lütfen 1-6 arasında bir değer girin.")


if __name__ == "__main__":
    main()