import socket

# สร้าง Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 65432)

# ผูก Socket กับ Address และ Port
server_socket.bind(server_address)

# เริ่มฟังการเชื่อมต่อ
server_socket.listen(5)
print("Server is listening on port 65432...")

# รอรับการเชื่อมต่อจาก Client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established.")

# รับข้อมูล
data = client_socket.recv(1024).decode('utf-8')
print(f"Received: {data}")

# ส่งข้อมูลกลับ
response = "Hello Client!"
client_socket.send(response.encode('utf-8'))

# ปิดการเชื่อมต่อ
client_socket.close()
server_socket.close()