import random

randomSayi = random.randint(0,1000)
cevap = -1

tahminSayisi = 0
while cevap != randomSayi:
    tahminSayisi += 1
    cevap = int(input("tahmininin nedir: "))
    if cevap < randomSayi:
        print("�ok k���k s�yledin")
    elif cevap > randomSayi:
        print("�ok b�y�k")
    
print("Bildin! Random say� =", randomSayi)
print("Tahmin say�s�:", tahminSayisi)
