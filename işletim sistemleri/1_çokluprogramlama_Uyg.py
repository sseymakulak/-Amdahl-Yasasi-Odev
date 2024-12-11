import time 

def program1():
    for i in range(9):
        print(f"Program 1 çalışıyor: {i}")
        time.sleep(2) #simüle edilen gecikme
        
    
def program2():
    for i in range(9):
        print(f"Program 2 çalışıyor: {i}")
        time.sleep(2)
        
if __name__ =="__main__":
    import threading
    
    #iki programı ayrı iş parçacıkları (threads) olarak çalıştırıyoruz
    thread1= threading.Thread(target=program1)
    thread2= threading.Thread(target=program2)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("Tüm programlar tamamandı!")
    
    
    
    
    