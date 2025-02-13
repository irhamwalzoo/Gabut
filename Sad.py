import time
import random

pesan = [
    "Kenapa ya muka ku kayak KONTOL...",
    "Dia cantik banget...",
    "Mungkin cuma bisa ku lihat...",
    "Tapi tidak bisa dimiliki... DEAD 😭😭"
]

while True:
    print(random.choice(pesan))  # Pilih pesan random tiap loop
    time.sleep(0.2)  # Delay dikit biar gak nge-lag
