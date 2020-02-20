import sys
import threading
import time
import random
import socket as mysoc

# server task
def server():
    # Getting port in which rs listens to requests
    rsListenPort = int(sys.argv[1])

    # Fetching and storing DNS table data
    with open("PROJI-DNSRS.txt") as file_in:
      dns_table = []
      for line in file_in:
          dns_table.append(line.strip().split(" "))

    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created on port "+ str(rsListenPort))
    except mysoc.error as err:
        print(format("socket open error ",err))

    print("DNS table: ",dns_table)


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
    
    c =[]

    while True:
      stream = ''
      # Initially setting new_msg flag to true
      new_msg = True
      while True:
      # Recieving header info of data sent from clieent
        data = csockid.recv(20).decode('utf-8')
        
        
        if new_msg:
            #print("new msg len:",data[:10])
            ###print("msglen preview:",len(data[:10]))
            try:
              # Obtaining headersize from stream
              msglen = int(data[:10])
            except ValueError:
              break
            new_msg = False

        #print(f"full message length: {msglen}")
        
        stream += data

        ###print(len(stream))


        if len(stream)-10 == msglen:
            #print("full msg recvd:")
           
            #print(stream[10:])
            recieved_hostname=stream[10:]
            print(recieved_hostname)
            new_msg = True
            stream = ""

      break



   # Close the server socket
    ss.close()
    exit()

server()