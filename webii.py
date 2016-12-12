import os
import socket

class Domain:
    def __init__(self,domain,port,start,end):
        self.domain = domain
        self.port = port
        self.start = start
        self.end = end

    def foreach(self):
        for i in range(self.start,self.end):
            try:
                s = socket.socket

                s.connect(('192.168.1.38',i))
                s.send('Primal Security \n')
                banner = s.recv(1024)
                if banner:
                    print("the port %d"%i)
                s.close()
            except:pass



if __name__ == '__main__':
    domain = Domain("192.168.1.121", 200, 1, 3000)
    domain.foreach();