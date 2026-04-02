import sys

name = input("Masukkan nama anda: ")
height = float(input("Masukkan tinggi anda (dalam meter, contoh 1.70): "))

while True:
    try:
        age = int(input("Masukkan umur anda: "))
        if age <= 0:
            print("Masukkan nombor yang sah")
        elif age < 18:
            print("Maaf, anda perlu berumur 18 tahun ke atas untuk menggunakan program ini.")
            sys.exit()
        else:
            break
    except ValueError:
        print("Masukkan nombor yang sah")

weight = float(input("Masukkan berat badan anda (dalam kg): "))

# Pengiraan BMI
bmi = weight / (height ** 2)

print("\n" + "="*30)
print("       KEPUTUSAN ANDA       ")
print("="*30)
print(f"Nama      : {name}")
print(f"Umur      : {age} tahun")
print(f"Tinggi    : {height} meter")
print(f"Berat     : {weight} kg")
print(f"Kiraan BMI: {bmi:.2f}")

# Menentukan kategori BMI
if bmi < 18.5:
    print("Kategori  : Kurang berat badan")
elif 18.5 <= bmi < 24.9:
    print("Kategori  : Berat badan normal")
elif 25 <= bmi < 29.9:
    print("Kategori  : Berat badan berlebihan")
else:
    print("Kategori  : Obesiti")
print("="*30)
