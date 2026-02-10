# Level 1 - Basic

nama = input("Nama kamu:")
umur = int(input("Umur kamu:"))

if umur >= 18:
    status = "Dewasa"
else:
    status = "Nikah"

print(f"Halo {nama}, kamu {status}")

print("\nHitung 1-5:")
for i in range(1, 6):
    print(i)
