import socket
import threading
import time

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

def parseMSG(msg):
    return msg
    try:
        return msg.split(":")[1].split("!")[0] + ": " + msg.split("PRIVMSG " + CHAN + " :")[1]
    except IndexError:
        return ""

def checkChat():
    #print("test")
    while True:
        result = s.recv(1024).decode('utf-8')
        print(parseMSG(result))
        
        if result[0:4] == "PING":
            s.send(("PONG" + result[4:] + "\r\n").encode())
            
        if len(result) == 0:
            print("breh")
            break
def sendChat():
    while True:
        s.send(('PRIVMSG ' + CHAN + ' ' + input() + '\r\n').encode())


def test1():
    time.sleep(2)
    print("Done!")


#sendThread = threading.Thread(target=sendChat)
#sendThread.daemon = True
#sendThread.start()

checkThread = threading.Thread(target=checkChat)
checkThread.daemon = True
checkThread.start()
#sendChat()
#sendThread.join()
checkThread.join()
