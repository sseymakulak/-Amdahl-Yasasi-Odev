from multiprocessing import Process
import threading
import time

# Paralel hesaplama fonksiyonu
def kare_hesapla(sayi):
    print(f"Hesaplanıyor (Thread/Process ID: {threading.get_ident()}): {sayi} -> {sayi * sayi}")
    time.sleep(1)

# Çoklu programlama (threads)
def coklu_programlama():
    sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nÇoklu Programlama Başladı (Thread)...\n")
    threads = []
    for sayi in sayilar:
        t = threading.Thread(target=kare_hesapla, args=(sayi,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print("\nÇoklu Programlama Tamamlandı!")

# Çoklu işlemci (processes)
def coklu_islemci():
    sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nÇoklu İşlemci Başladı (Process)...\n")
    processes = []
    for sayi in sayilar:
        p = Process(target=kare_hesapla, args=(sayi,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    print("\nÇoklu İşlemci Tamamlandı!")
    

if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()
