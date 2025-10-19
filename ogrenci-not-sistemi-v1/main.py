isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali"]
notlar = [85, 90, 78, 92, 88]

def liste_yazdir(isimler, notlar):
    print("\n=== ÖĞRENCİ LİSTESİ ===")
    for i, (isim, not_) in enumerate(zip(isimler, notlar), 1):
        print(f"{i}. {isim}: {not_}")

def ortalama_hesapla(notlar):
    return sum(notlar) / len(notlar)

def en_yuksek_and_dusuk_not(notlar, isimler):
    max_not = max(notlar)
    min_not = min(notlar)
    
    max_not_index = notlar.index(max_not)
    min_not_index = notlar.index(min_not)
    
    max_not_isim = isimler[max_not_index]
    min_not_isim = isimler[min_not_index]
    
    return (max_not, max_not_isim), (min_not, min_not_isim)

def gecen_kalan(notlar):
    gecen = sum(1 for not_ in notlar if not_ >= 70)
    kalan = len(notlar) - gecen
    return gecen, kalan

def main():
    print("=== SINIF İSTATİSTİKLERİ ===")
    
    liste_yazdir(isimler, notlar)
    
    ort = ortalama_hesapla(notlar)
    print(f"\nSınıf Ortalaması: {ort:.1f}")
    
    (max_not, max_isim), (min_not, min_isim) = en_yuksek_and_dusuk_not(notlar, isimler)
    print(f"En Yüksek Not: {max_not} ({max_isim})")
    print(f"En Düşük Not: {min_not} ({min_isim})")
    
    gecen, kalan = gecen_kalan(notlar)
    print(f"Geçen: {gecen}, Kalan: {kalan}")

if __name__ == "__main__":
    main()