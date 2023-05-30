import socket
from gameboard import BoardClass

RECV_SIZE = 1024
host_name = '127.0.0.1'
port_key = 5066
def starter_info():
    # host_name = input()
    # port_key = input()
    
    address = (host_name,port_key)
    return tuple(address)

def socket_connection(address, user_name, boardClass):
    '''Establishes connection with socket with provided ip address and port'''
    
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    connectionSocket.connect(address)
    
    

    
    
    connectionSocket.send(user_name.encode())
    
    while True:
        move = input()
        connectionSocket.send(move.encode())
        serverResponse = connectionSocket.recv(2048).decode()
        boardClass.updateGameBoard(int(serverResponse))
        print(boardClass.display_board())
        
        
    #connectionSocket.close()

    



print("Enter username:", end=' ')

p1_user_name = input()

game_board = BoardClass(p1_user_name)

ip_addy = (host_name,port_key)

socket_connection(ip_addy, p1_user_name, game_board)
