from email import message
import socket

sock_= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock_.connect((socket.gethostname(),9337))
message=sock_.recv(1024)
sock_.close()
print(message.decode("ascii"))