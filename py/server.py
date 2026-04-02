import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

# Tambahkan baris ini untuk menyimpan siapa yang masuk:
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tambah baris ini. Ia ibarat "Master Key" untuk paksa komputer buka pintu 5555.
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

print(f"Server kini sedang mendengar di alamat {HOST}:{PORT}")

# Gantikan fungsi broadcast yang lama dengan ini:
def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client: # Jika dia BUKAN penghantar, baru hantar mesej
            client.send(message)

# Gantikan fungsi handle yang lama dengan ini:
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client) # Tambah 'client' di belakang 'message'
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Koneksi baru dari {address}")
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Tambahkan ini di bawah sekali supaya server mula bekerja
receive()
