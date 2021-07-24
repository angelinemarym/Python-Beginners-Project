import time
import webbrowser
from random import choice

url = "https://www.instagram.com/angelintech/"

jumlah_istirahat = int(input('Berapa kali Lo mau istirahat? '))
counter = 0
jeda_waktu = 30*60

pesan = ["Waktunya bergerak!", "Gerak Woyy!"]

print("Menjalankan Break Scheduler!")

while(counter < jumlah_istirahat):
    time.sleep(jeda_waktu)

    # Print pesan pengingat
    print(choice(pesan))

    # Membuka window browser
    webbrowser.open(url)

    # Menambah (increment) nilai counter
    counter += 1

print("Mengakhiri Break Scheduler!")




