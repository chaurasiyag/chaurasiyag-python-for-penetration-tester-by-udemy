import socket

host=socket.gethostname()

port=9337

sock_=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock_.bind((host, port))
sock_.listen(1)
print('\n Server started')

conn,addr=sock_.accept()


print('Connection established with :',str(addr))

message="\n Thank you for connecting "+str(addr)

conn.send(message.encode('ascii'))
conn.close()