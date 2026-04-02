import socket
import threading

# Ini adalah alamat Server yang kita nak pergi
HOST = '127.0.0.1'
PORT = 5555

# Tambah baris ini untuk minta nama sebelum mereka berhubung ke pelayan
nama_saya = input("Sila masukkan nama (nickname) anda: ")

# 1. Bina paip soket dan pautkan (connect) ke Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# 2. Fungsi untuk sentiasa membaca (mendengar mesej kawan)
def receive():
    while True:
        try:
            # Terima mesej dan tukar kod mesin (bytes) kembali jadi tulisan (decode)
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Ralat berlaku! Terputus sambungan.")
            client.close()
            break

# Cari fungsi write() yang lama dan GANTIKAN dengan ini:
def write():
    while True:
        mesej = input("") 
        
        # Gabungkan nama dan mesej menggunakan f-string
        mesej_penuh = f"{nama_saya}: {mesej}"
        
        # Hantar mesej yang sudah digabungkan itu ke Server
        client.send(mesej_penuh.encode('utf-8'))

# 4. Mula Dua Tugas Serentak (Mendengar Mesej & Boleh Menaip Serentak)
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

print(f"Berjaya menyambung! Selamat bersembang, {nama_saya}.")
