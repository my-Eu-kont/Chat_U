import socket
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))


isOnline = input('IsOnline?')
client_socket.sendall(isOnline.encode())

while isOnline!="no":
    # Enviando mensagem para o servidor
    message = input('digite:')
    client_socket.sendall(message.encode())

    # Recebendo resposta do servidor , decode da msg do servidor
    data = client_socket.recv(1024)
    print(f"Resposta do servidor --> {data.decode()}")

    # encerrando conexao pelo cliente
    if message == "out":
        data = client_socket.recv(1024)
        print(f"servidor desconcectado > {data.decode()}")
        break


client_socket.close()
