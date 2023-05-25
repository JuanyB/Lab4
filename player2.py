import socket
import gameboard
def socketConnection(host, port):
    address = (host, port)
    socketTunnel = socket.socket(AF_INET, SOCK_STREAM)
    return socketTunnel
def mainFunction():
    server = socketConnection (HOST, PORT)
    server.bind(address)
    server.listen(5)
    print('What is your name Player 2?')
    player2_username = input()
    while True:
        client, clientAddress = server.accept()
    player1_username = client.recv(1024)
    
if __name__ == '__main__':
    print('Welcome! Please provide host and port below:\n')
    HOST = input('Please provide host address:\n')
    print('Please provide port:\n')
    PORT = int(input())
    mainFunction()
