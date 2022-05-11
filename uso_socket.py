import socket 
def socket_uso(url_socket):
    puertos = socket.gethostbyname_ex(url_socket)
    print(puertos)