from multiprocessing import Process
import os
import time

# Paralel çalışan işlem
def islem_yap(sayi):
    print(f"İşlemci: {os.getpid()} - Sayı: {sayi}, Kare: {sayi * sayi}")
    time.sleep(2)  # Simüle edilen işlem süresi

if __name__ == "__main__":
    print("Çoklu İşlemci (Multiprocessing) Başlıyor...\n")

    sayilar = [1, 2, 3, 4, 5, 6, 7, 8]
    islemler = []

    # Her sayı için ayrı bir işlem oluştur
    for sayi in sayilar:
        islem = Process(target=islem_yap, args=(sayi,))
        islemler.append(islem)
        islem.start()

    # İşlemleri tamamlama
    for islem in islemler:
        islem.join()

    print("\nTüm İşlemler Tamamlandı!")