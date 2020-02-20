import sys
import threading
import time
import random
import socket as mysoc

# server task
def server():
    # Getting port in which rs listens to requests
    rsListenPort = sys.argv[1]
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created on port "+ str(rsListenPort))
    except mysoc.error as err:
        print(format("socket open error ",err))

    server_binding=('',rsListenPort)
    ss.bind(server_binding)
    ss.listen(2)

    # Getting hostname
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)
    
    # send a intro  message to the client.
    msg="Welcome to CS 352"
    csockid.send(msg.encode('utf-8'))

   # Close the server socket
    ss.close()
    exit()

server()