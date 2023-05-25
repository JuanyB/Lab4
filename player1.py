import socket
import gameboard
def creating_socket(host, port):
    try:
        address = (host, port)
        socketTunnel = socket.socket(AF_INET, SOCK_STREAM)
        socketTunnel.connect(address)
    except:
        print('Connection failed. Try again?\n')
        try_again = input()
        if try_again.lower() == 'n':
            return 'Goodbye!'   
    return socketTunnel

def main_func():
    #Attempting Connection and sending/receiving usernames
    clientCall = creating_socket(HOST, PORT)
    player1_username = input('What is your name Player 1?\n')
    clientCall.send(player1_username.encode())
    player2_username = clientCall.recv(1024).decode()
    

    
    
if __name__ == '__main__':
    print('Welcome! Please provide host and port below:\n')
    HOST = input('Please provide host address:\n')
    print('Please provide port:\n')
    PORT = int(input())
    main_func()
