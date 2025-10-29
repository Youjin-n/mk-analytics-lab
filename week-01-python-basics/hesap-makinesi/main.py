while True:
  giris = input('4 işlem hesap makinasına hoş geldiniz. Giriş için "ENTER" tuşuna tıklayın. Çıkmak için "q" yazıp "ENTER" tuşuna tıklayın.: ')
  if giris == "":
    first_number = float(input("İlk sayıyı giriniz(): "))
    second_number = float(input("İkinci sayıyı giriniz: "))
    islem = input("Yapmak istediğiniz işlem hangisi? (Çarpma için(*), Toplama için(+), Çıkarma için(-), Bölme için(/)): ")
    if islem == "+":
      sonuc = first_number + second_number
    elif islem == "-":
      sonuc = first_number - second_number
    elif islem == "*":
      sonuc = first_number * second_number
    elif islem == "/":
      sonuc = first_number / second_number
    else:
      print("Hatalı giriş yaptınız. Tekrar deneyin")
  elif giris == "q":
    break
  else:
    print('Lütfen gereksiz değer girmeyin. Giriş yapmak için ya boş bırakarak "ENTER" tuşuna basın ya da çıkmak için "q" yazıp "ENTER" tuşuna basın.')
