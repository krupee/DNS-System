import socket as mysoc
import sys


#client task
def client():
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(format("socket open error ",err))
  #python client.py rsHostname rsListenPort tsListenPort
  
  # Defining the port on which you want to connect to the RS server
    rsport = sys.argv[2]
  # Defining hostname for RS server
    rs_hostName = mysoc.gethostbyname(sys.argv[1])
    # For testing purposes
    #rs_hostName = mysoc.gethostbyname(mysoc.gethostname())
    print(rs_hostName)
    return 
  # Defining the port on which you want to connect to the TS server
    tsport = sys.argv[3]

    

  # Connecting to the RS server on local machine
    server_binding=(rs_hostName,rsport)
    cs.connect(server_binding)
    rmsgs = []
    msgs = []

  # Reading HW1test.txt file and storing each line as an element in the msgs list
    msgs = [line.rstrip('\n') for line in open('PROJI-HNS.txt')]
    i=0

    while i in range(len(msgs)):
    # Creating a header in order to specify number of characters in word to server
      full = ("{:<10}".format(len(msgs[i]))+msgs[i])
    # Sending the word to server
      print("[C]: Client sending word:: ",msgs[i])
      cs.send(full.encode())

    # receiving data back from the server
      data_from_server=cs.recv(1024)
      print("[C]: Data received from server::",data_from_server.decode('utf-8'))
    # appending recieved data to returned msgs list of ascii values
      rmsgs.append(data_from_server)
      i = i+1
    
    
    print(rmsgs)

    # # Writing returned words to HW1out.txt file
    # with open('HW1out.txt', 'w') as filehandle:
    #   for j in rmsgs:
    #     filehandle.write(j.decode('utf-8')+"\n")

# closing the client socket
    cs.close()
    exit()

client()