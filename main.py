import socket
import time
acikPortlar = []
def port_taramasi(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(taramaHizi)  # Bağlantı zaman aşımını belirleyebilirsiniz
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} açık.")
            acikPortlar.append(port)

        else:
            print(f"Port {port} kapalı.")
        sock.close()
    except socket.error:
        print("Bağlantı hatası.")

ip_adresi = input("Enter IP address: ")
sik_kullanilan_portlar = [21,22,23,25,53,80,110,115,139,143,161,443,445,514,3306,3389,8080]
sik_kullanilan_portlar2 = [11,12,13,21]
print(f"Sık kullanılan {len(sik_kullanilan_portlar)} port için 1'i tuşlayınız.")
print("Sık kullanılan portlar(seviye2) için 2'yi tuşlayınız.")
print("Tarama aralığı vermek için 3 ü tıklayınız.")

girilenPortlar = input("Sayıları girin (virgülle ayırarak): ")

if girilenPortlar == "1":
    portlar = sik_kullanilan_portlar
    print("Sık kullanılan portlar taranıyor...")
elif girilenPortlar == "2":
    portlar = sik_kullanilan_portlar2
    print("Sık kullanılan portlar (seviye2) taranıyor")
elif girilenPortlar == "3":
    print("Port aralığı seçin(seçtikleriniz dahil).")
    baslangic = input("Kaçtan başlayacak? ")
    bitis = input("Kaçta bitecek? ")
    portlar = list(range(int(baslangic),int(bitis) + 1))
else:
    portlar = list(map(int, girilenPortlar.split(","))) # Taramak istediğiniz portları listeye ekleyin
taramaHizi = int(input("Port başına düşen tarama saniyesini yazınız(Örneğin 3): "))
for port in portlar:
    port_taramasi(ip_adresi, port)
print(f"Açık Portlar {acikPortlar}")
input("İşlemi sonlandırmak için entere basın.")
