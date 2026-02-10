import json
import requests
from datetime import datetime

# ===== Simpan Catatan ke File =====
catatan = input("Tulis catatan kamu: ")

data = {
    "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "catatan": catatan
}

with open("catatan.json", "w") as f:
    json.dump(data, f, indent=2)

print("Catatan disimpan ke catatan.json 📁")

# ===== Baca Lagi File JSON =====
with open("catatan.json", "r") as f:
    isi = json.load(f)

print("\nIsi file:")
print(isi)

# ===== Ambil Data API =====
print("\nAmbil data dari API GitHub...")

try:
    r = requests.get("https://api.github.com")
    print("Status:", r.status_code)

    if r.status_code == 200:
        api_data = r.json()
        print("Current user URL:", api_data["current_user_url"])
    else:
        print("Gagal ambil data API")

except Exception as e:
    print("Error:", e)
