#!/usr/bin/env python3
import socket 
import sys 
import time

HOST = '127.0.0.1' # IP do Servidor 
PORT = 40001 # Porta que o Servidor escuta 

lista_comandos = {      # Lista de comandos que o usuário pode escolher
    "pedra": "PEDRA",
    "tesoura": "TESOURA",
    "papel": "PAPEL",
}

lista_de_erros = {        # Lista de erros possíveis
    "404": "Comando errado, verifique se foi escrito corretamente",
    "406": "Comando incompleto",
    "409": "campo vazio",
}

if len(sys.argv) > 1:  # Pega o endereço IP do servidor digitado pelo cliente
    HOST = sys.argv[1]

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definindo o socket como TCP stream    
sock.connect(serv)  #Conectando com o socket

print('Servidor: ', (HOST, PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
sock.connect(dest)


jogador1 = 1
jogador2 = 2

while True:    # Menu de escolhas do usuário
    print()
    print("*=" * 40, "\n")
    print('Escolha um comando PEDRA/PAPEL/TESOURA', "\n")
    print("-" * 40, "\n")
    
    
    cmd_usr = input("Digite algum comando: ").split()
    tamanho_comando = len(cmd_usr)


    try:
       comando = lista_comandos.get(cmd_usr[0].lower())
       print(comando)
       if comando == "PEDRA":
         #if tamanho_comando == 1:

        sock.send(str.encode(comando + " " + cmd_usr[1]))     # Vai enviar para o servidor o comando com o nome do arquivo
        dados = sock.recv(1024)
        msg_status = dados.decode()
        if lista_de_erros.get(msg_status):        # Se tiver algum erro ele exibe o erro na tela
          print(lista_de_erros.get(msg_status))
        else:
          print(lista_de_erros.get("406"))
       elif comando == "PAPEL":
        sock.send(str.encode(comando + " " + cmd_usr[1]))     # Vai enviar para o servidor o comando com o nome do arquivo
        dados = sock.recv(1024)
        msg_status = dados.decode()
        if lista_de_erros.get(msg_status):        # Se tiver algum erro ele exibe o erro na tela
          print(lista_de_erros.get(msg_status))
        else:
          print(lista_de_erros.get("406"))
       elif comando == "TESOURA":
         #
        sock.send(str.encode(comando + " " + cmd_usr[1]))     # Vai enviar para o servidor o comando com o nome do arquivo
        dados = sock.recv(1024)
        msg_status = dados.decode()
        if lista_de_erros.get(msg_status):        # Se tiver algum erro ele exibe o erro na tela
          print(lista_de_erros.get(msg_status))
        else:
          print(lista_de_erros.get("406"))
         
    except IndexError:
      print(lista_de_erros.get("409"))  
        
sock.close() 

