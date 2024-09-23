import socket
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))


# Enviando mensagem inicial para o servidor
message = input('digite  <')
client_socket.sendall(message.encode())

if message == "out":
    client_socket.close()

# Recebendo resposta do servidor , decode da msg do servidor
data = client_socket.recv(1024)
print(f"Resposta do servidor > {data.decode()}")

client_socket.close()
