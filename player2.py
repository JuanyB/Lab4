import socket
from gameboard import BoardClass
HOST = '127.0.0.1'
PORT = 5066
RECV_SIZE = 1024

def run_server(boardClass):
    socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tunnel.bind((HOST,PORT))
    print(f"Desktop Name: {socket.gethostname()}")
    print(f'Connection made \n Host name:{HOST}\nPort: {PORT}')
    socket_tunnel.listen(5)
    
    clientSocket, clientAddress = socket_tunnel.accept()
    
    p1_name = clientSocket.recv(2048).decode()
    print('A new fighter has entered the area:', p1_name)
    game_board = boardClass(p1_name)
    while True:
        p1_move_welcome = clientSocket.recv(2048)
        p1_move = int(p1_move_welcome.decode())
        print(p1_move)
        game_board.updateGameBoard(p1_move)
        print(game_board.display_board())
        
        print("What is your move player 2?")
        p2_move = input("What is your move:\n")
        
        clientSocket.send(p2_move.encode())
        
        if game_board.boardIsFull() == True:
            conn.close()
if __name__ == "__main__":
    run_server(BoardClass)
