import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "irc.libera.chat"
PORT = 6667
NICK = "nicky2023"
CHAN = "#test"

s.connect((HOST, PORT))

nick_data = ('NICK ' + NICK + '\r\n')
s.send(nick_data.encode())

username_data = ('USER ' + NICK + '1 ' + NICK + '2 ' + NICK + '3 :' + NICK + '4 \r\n')
s.send(username_data.encode())

s.send(('JOIN ' + CHAN + ' \r\n').encode())

while True:
    result = s.recv(1024).decode('utf-8')
    print(result)

    #s.send(('PRIVMSG ' + CHAN + ' ' + input() + '\r\n').encode())

    if result[0:4] == "PING":
        s.send(("PONG" + result[4:] + "\r\n").encode())

    if len(result) == 0:
        print("breh")
        break
