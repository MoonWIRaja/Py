# ==========================================
# Latihan daripada 06_lists.pdf
# Topik: Senarai (Lists)
# ==========================================

print("=== Latihan 1: Grocery List (CRUD Operations) ===")

# 1. CREATE (Mencipta)
# List (Senarai) adalah himpunan data yang diletakkan dalam kurungan siku [...]
grocery_list = ["Beras", "Ayam", "Sayur", "Telur"]
print("Asal:", grocery_list)

# 2. READ (Membaca)
# Kita boleh membaca nilai dari senarai melalui 'index' (bermula dari 0)
item_pertama = grocery_list[0]
print("Barang pertama:", item_pertama) # Output: Beras

# 3. UPDATE (Mengemaskini/Menambah)
# a. Menambah item baru di hujung senarai (append)
grocery_list.append("Roti")
print("Selepas tambah 'Roti':", grocery_list)

# b. Mengubah/Mengemaskini item pada index tertentu
# Tukar "Ayam" (index 1) kepada "Ikan"
grocery_list[1] = "Ikan"
print("Selepas tukar Ayam kepada Ikan:", grocery_list)

# 4. DELETE (Memadam)
# Mengeluarkan item daripada senarai (remove)
grocery_list.remove("Sayur")
print("Selepas buang 'Sayur':", grocery_list)

# Boleh juga padam menggunakan index dengan fungsi pop()
# pop() akan buang dan memulangkan elemen terakhir jika tak diberi index
dibuang = grocery_list.pop() # Buang 'Roti'
print(f"Selepas pop() ({dibuang} dikeluarkan):", grocery_list)


print("\n=== Latihan 2: Largest and Smallest Number ===")
# Diberikan satu senarai nombor
nombor_list = [45, 12, 89, 5, 100, 33, 7]
print("Senarai nombor:", nombor_list)

# Cara Pertama: Menggunakan Built-in function Python (Paling mudah)
nombor_terbesar = max(nombor_list)
nombor_terkecil = min(nombor_list)

print(f"Cara 1 - Terbesar: {nombor_terbesar}, Terkecil: {nombor_terkecil}")

# Cara Kedua: Menggunakan Loop (Untuk praktik konsep sebelumnya)
paling_besar = nombor_list[0] # Kita andaikan nombor pertama ialah yang paling besar dahulu
paling_kecil = nombor_list[0] # Kita andaikan nombor pertama ialah yang paling kecil dahulu

for nombor in nombor_list:
    # Semak largest
    if nombor > paling_besar:
        paling_besar = nombor
    
    # Semak smallest
    if nombor < paling_kecil:
        paling_kecil = nombor

print(f"Cara 2 (Guna Loop) - Terbesar: {paling_besar}, Terkecil: {paling_kecil}")
