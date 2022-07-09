
import sys
import socket
from threading import Thread

HOST = '0.0.0.0'
PORT = 40001

TAMANHO_MENSAGEM = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(2)



sockets = []
jogadas = []
jogadores = []
contador = 0
    
def processa_cliente(con, cliente): #Metodo para processar mensagem do cliente
    while True: #Enquanto for verdadeiro
        msg = con.recv(1024) #Ler o tamanho da mensagem do cliente
        print("msg",msg.decode()) 
        if not msg or processa_mensagem(msg, con, cliente): break

    con.close() #Fecha a conexão e informa qual cliente foi desconecatado
    print("Cliente desconectado:", cliente)

def jogador_ganhador(coneccao):
    if len(jogadas) == 2:
        if jogadas[0]== 'papel':
            if jogadas[1] == 'pedra':
                sockets[0].send(str.encode("Jogador 1 ganhou"))
                sockets[1].send(str.encode("Jogador 1 ganhou"))
                 #ajustat os comandos no array para funcionar o send
        #verificar se é para usar assim;
            elif jogadas[1] == 'tesoura':
                sockets[0].send(str.encode('jogador 2 ganhou'))
                sockets[1].send(str.encode('jogador 2 ganhou'))
                
            else:
                sockets[0].send(str.encode('empate'))
                sockets[1].send(str.encode('empate'))
                
        elif jogadas[0]== 'pedra':
            if jogadas[1] == 'papel':
                sockets[0].send(str.encode('jogador dois ganhou'))
                sockets[1].send(str.encode('jogador dois ganhou'))
                

            elif jogadas[1] == 'pedra':
                sockets[0].send(str.encode('Empate'))
                sockets[1].send(str.encode('Empate'))
                
                
            else:
                sockets[0].send(str.encode('jogador 1 ganhou'))
                sockets[1].send(str.encode('jogador 1 ganhou'))
                
                

        elif jogadas[0]== 'tesoura':
            if jogadas[1] == 'papel':
                sockets[0].send(str.encode('jogador um ganhou'))
                sockets[1].send(str.encode('jogador 1 ganhou'))

                

            elif jogadas[1] == 'pedra':
                sockets[0].send(str.encode('jogador dois ganhou'))
                sockets[1].send(str.encode('jogador dois ganhou'))
                
                
            else:
                sockets[0].send(str.encode('Empate'))
                sockets[1].send(str.encode('empate'))
        jogadas.clear()

    else:
        sockets[0].send(str.encode("esperando a resposta do outro jogador..."))


def processa_mensagem(mensagem, coneccao, cliente): # Metodo que faz o processamento da mensagem
    mensagem_decodificada = mensagem.decode() #Decodifica a mensagem e coloca dentro da variável, mensagem_decodificada
    print("mensagem_decodificada", mensagem_decodificada)
    
    mensagem_decodificada = mensagem_decodificada.split()
    global contador


    while True:

        if cliente == jogadores[contador]:
            jogadas.append(mensagem_decodificada[1:])
            contador += 1
            if contador == 2:
                contador = 0
            
            jogador_ganhador(coneccao)

        


while True:
    try:
        con, cliente = sock.accept() #Inicia uma conexão com o cliente
        jogadores.append(cliente)
        sockets.append(con)

    except: break
    thread = Thread(target=processa_cliente, args=(con, cliente)) 

    thread.start() #Dá início a uma thread, para cada cliente criado

sock.close()

                

        