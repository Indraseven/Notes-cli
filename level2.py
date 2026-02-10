import random

# ===== Kalkulator =====
def kalkulator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "Tidak bisa bagi 0"
    else:
        return "Operator tidak dikenal"

print("=== Kalkulator Sederhana ===")
try:
    x = float(input("Angka 1: "))
    y = float(input("Angka 2: "))
    operasi = input("Operator (+ - * /): ")
    hasil = kalkulator(x, y, operasi)
    print("Hasil:", hasil)
except ValueError:
    print("Input harus angka!")

# ===== Password Checker =====
print("\n=== Password Checker ===")

password = input("Masukkan password: ")

kriteria = {
    "panjang": len(password) >= 8,
    "angka": any(c.isdigit() for c in password),
    "huruf": any(c.isalpha() for c in password)
}

if all(kriteria.values()):
    print("Password kuat 💪")
else:
    print("Password lemah ⚠️")

# Bonus: Password random
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
random_pass = "".join(random.choice(chars) for _ in range(10))
print("Contoh password random:", random_pass)
