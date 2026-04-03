# Latihan daripada 05_loops.pdf

print("=== Exercise 1: Multiplication Table Generator ===")
nombor = int(input("Masukkan nombor sifir (cth: 5): "))

# Menggunakan for loop untuk menjana sifir daripada 1 hingga 12
for i in range(1, 13):
    hasil = nombor * i
    print(f"{nombor} x {i} = {hasil}")

print("\n=== Exercise 2: Find all prime numbers up to a given number ===")
limit = 20
print(f"Nombor perdana sehingga {limit}:")

# Menggunakan nested loop untuk menyemak nombor perdana
for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            is_prime = False
            break
            
    if is_prime:
        print(num, end=" ")
print() # Menambah baris baharu
