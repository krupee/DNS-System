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
    rsport = int(sys.argv[2])
  # Defining hostname for RS server
    #rs_hostName = mysoc.gethostbyname(sys.argv[1])
    
    ## For testing purposes
    rs_hostName = mysoc.gethostbyname(mysoc.gethostname())
    #print(rs_hostName)

  # Defining the port on which you want to connect to the TS server
    tsport = int(sys.argv[3])

  # Connecting to the RS server
    server_binding=(rs_hostName,rsport)
    cs.connect(server_binding)

    rmsgs = []
    hns = []
    try:
      css=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
      print("[C]: Client socket 2 created")
    except mysoc.error as err:
      print(format("socket open error ",err))
    
    server_binding2=(rs_hostName,tsport)
    css.connect(server_binding2)
    

  # Reading PROJI-HNS.txt file and storing each line as an element in the Hostnames list
    hns = [line.rstrip('\n') for line in open('test.txt')]
    i=0
  # Writing returned records to RESOLVED.txt file
    f = open("RESOLVED.txt","w+")

    while i in range(len(hns)):
    # Creating a header in order to specify number of characters in each line to server
      full = ("{:<10}".format(len(hns[i]))+hns[i])
      print(full)
    # Sending the word to server
      print("[C]: Client sending hostname:: ",hns[i])
      cs.send(full.encode())
      
    # Receiving data back from the server
      data_from_server = cs.recv(1024).decode('utf-8')
    # Splitting data into a list
      data_list = data_from_server.split(" ")

    # Checking if data recieved is an A record or NS record
      if (data_list[2] == "A"):
        # Is A record, can write data to output file
        f.write(str(data_from_server)+"\n")
      else:
        # Is NS record, must check with TLS server
        ### Add TLS check here
        f.write(str(data_from_server)+"\n")
        '''
        css.send(full.encode())
        data_from_server2 = css.recv(1024).decode('utf-8')
        f.write(str(data_from_server2)+"\n")
        '''
        #print("[C]: Data received from server::",data_from_server)

   
      i = i+1

# closing the client socket
    cs.close()
    css.close()
    exit()

#def tlsSocketConnections():



client()