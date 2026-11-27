import socket

# สร้าง Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 65432)

# เชื่อมต่อกับ Server
client_socket.connect(server_address)

# ส่งข้อมูล
message = "Hello Server!"
client_socket.send(message.encode('utf-8'))

# รับข้อมูลจาก Server
response = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {response}")

# ปิดการเชื่อมต่อ
client_socket.close()