import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8080))
    server_socket.listen(5)
    print("Server is listening on port 8080")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")
        client_socket.send(bytes("You have reached the server!\n", "utf-8"))
        client_socket.close()

if __name__ == "__main__":
    start_server()
