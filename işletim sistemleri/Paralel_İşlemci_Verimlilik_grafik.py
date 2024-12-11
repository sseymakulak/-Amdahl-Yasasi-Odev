import matplotlib.pyplot as plt
import numpy as np

def hizlanma_hesapla(paralel_oran, islemci_sayisi):
    
    #Amdahl Yasasına göre hızlanma faktörünü hesaplar.

    return 1 / ((1 - paralel_oran) + (paralel_oran / islemci_sayisi))

def verimlilik_hesapla(paralel_oran, islemci_sayisi):
    
    #İşlemci başına verimliliği hesaplar.
    
    hizlanma = hizlanma_hesapla(paralel_oran, islemci_sayisi)
    return hizlanma / islemci_sayisi

def verimlilik_simulatoru(paralel_oran, max_islemci):
    
    #Paralel işlemci verimliliğini simüle eder ve görselleştirir.

    islemci_sayilari = np.arange(1, max_islemci + 1)
    hizlanma_degerleri = [hizlanma_hesapla(paralel_oran, n) for n in islemci_sayilari]
    verimlilik_degerleri = [verimlilik_hesapla(paralel_oran, n) for n in islemci_sayilari]

    plt.figure(figsize=(12, 6))

    # Hızlanma grafiği
    plt.subplot(1, 2, 1)
    plt.plot(islemci_sayilari, hizlanma_degerleri, marker='o', label='Hızlanma Faktörü')
    plt.title('Hızlanma Faktörü vs İşlemci Sayısı')
    plt.xlabel('İşlemci Sayısı')
    plt.ylabel('Hızlanma Faktörü')
    plt.grid(True)
    plt.legend()

    # Verimlilik grafiği
    plt.subplot(1, 2, 2)
    plt.plot(islemci_sayilari, verimlilik_degerleri, marker='o', color='orange', label='Verimlilik')
    plt.title('Verimlilik vs İşlemci Sayısı')
    plt.xlabel('İşlemci Sayısı')
    plt.ylabel('Verimlilik')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

def ana():
    print("Paralel İşlemci Verimlilik Simülatörü")
    try:
        paralel_oran = float(input("Paralel hale getirilebilen kod oranını girin (0 ile 1 arasında): "))
        if not (0 <= paralel_oran <= 1):
            raise ValueError("Paralel oran 0 ile 1 arasında olmalıdır.")

        max_islemci = int(input("Maksimum işlemci sayısını girin: "))
        if max_islemci <= 0:
            raise ValueError("İşlemci sayısı pozitif bir sayı olmalıdır.")

        verimlilik_simulatoru(paralel_oran, max_islemci)
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    ana()