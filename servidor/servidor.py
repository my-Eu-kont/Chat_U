import socket
 
# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando o socket ao endereço e porta
server_socket.bind(('localhost', 12345))

# Escutando por conexões
server_socket.listen(5)
print("Servidor escutando na porta...")

# Aceitando conexões de clientes
while True:
    conn, addr = server_socket.accept()

    print(f" cliente Conectado por: <{addr}>")

    # Recebendo mensagem do cliente, (data.decode) 
    data = conn.recv(1024)
    
    print(f"Mensagem trasnmitida pelo Cliente: _<{data.decode()}>_")
    msg = data.decode()
    
    if msg == "out":
        conn.sendall(b" Tchau ",msg)
        conn.close()
    if msg == 'oi':
        conn.sendall(b"ola/hellow/hallo")
    else :
        conn.sendall(b" Na escuta?") 
                
    # Respondendo ao cliente
    conn.sendall(b"Resposta do servidor: ")
    
    conn.close()




