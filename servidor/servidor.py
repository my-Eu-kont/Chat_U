import threading
import time
import socket

# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando o socket ao endereço e porta
server_socket.bind(('localhost', 12345))

# Escutando por conexões
server_socket.listen(5)
print("Servidor escutando na porta...")


def multiplasConexoes(nome, tempo):
    print(f'Thread {nome} iniciada.')
    dialogo()
    time.sleep(tempo)
    print(f'Thread {nome} finalizada após {tempo} segundos.')


def dialogo():
    
    # Aceitando conexões de clientes
    while True:
        
        conn, addr = server_socket.accept()
        print("_________[SERVIDOR]_________")
        print(f" cliente Conectado por: <{addr}>")
        print("____________________________")

        
        
        # Recebendo 1@ mensagem do cliente, (data.decode) 
        IsOnline = conn.recv(1024)
        print(f"Cliente online: <{IsOnline.decode()}>")
        
        while IsOnline.decode()!= "no":
            data = conn.recv(1024)
            print(f"Cliente disse: <{data.decode()}>")
            msg = data.decode()
        
            if msg == "out":
                conn.sendall(b" Tchau ",msg,'  ')
                break
            if msg == 'oi':
                conn.sendall(b"ola  / hellow / hallo ")
            else :
                conn.sendall(b" Na escuta?")


        # Respondendo ao cliente
        conn.sendall(b" testeee")
        
        conn.close()

thread1 = threading.Thread(target=multiplasConexoes, args=("cliente[1]", 1000))
thread2 = threading.Thread(target=multiplasConexoes, args=("cliente[2]", 1000))
thread3 = threading.Thread(target=multiplasConexoes, args=("cliente[3]", 1000))

thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()

print("Todas as threads foram finalizadas.")