#!/usr/bin/python

import argparse
from socket import *



def ShowBanner(ports,sock):
                           try:
                             if ports == "80":
		                    sock.send("GET HTTP/1.1  \r\n")
		             else:
		                sock.send(" \r\n ")
		                results = sock.recv(4096)
                                print "[+] Service: " + str(results) + "\n"
                           except:
                                print "[+] svc name unavail\n"



#TCP scan function
def tcpScan(targetIp,targetPort):
                         print "Port Scan Initiated on: " + targetIp + "\n"

                         try:
		            sock = socket(AF_INET,SOCK_STREAM)
		            sock.connect((targetIp,int(targetPort)))
                            print "[+] TCP Port: " +str(targetPort) + " Open"
                            ShowBanner(targetPort,sock)

                         except:
                             print "[+] TCP Port: " +str(targetPort) + " CLOSED\n"

                         finally:
                               sock.close()
#UDP scan function
def udpScan(targetIp,targetPort):
       try:
	 #Connects two sockets based on the IP address and Port
          consock = socket(AF_INET,SOCK_DGRAM)
          consock.connect((targetIp,targetPort))
          print "[+] UDP Port Open: " + str(targetPort)
          ShowBanner(targetPort,consock)
       except:
          print "[+] UDP port closed: " + str(targetPort)


#Checks if the protocol used is UDP/TCP
def checkType(ip,port,isUdp,isTcp):
     for ports in port:
         if (isTcp):
            tcpScan(ip,int(ports))
         else:
            udpScan(ip,int(ports))




def main():
    print "Welcome To TCP/UDP Port Scanner!\n"
    try:
     #invokes user based parameters based on various arguments
     parser = argparse.ArgumentParser("TCP/UDP Scanner")

     parser.add_argument("-a","--address",type=str,help="Enter the ip address to scan")
     parser.add_argument("-p","--port",type=str,help="Enter The port to scan")
     parser.add_argument("--udp",action="store_true")
     parser.add_argument("--tcp",action="store_true")

     args = parser.parse_args()
     ipaddress = args.address
     port = args.port.split(',')
     isUdp = args.udp
     isTcp= args.tcp
    #checks user input based on the protocols and ip address
     checkType(ipaddress,port,isUdp,isTcp)

    except:
     print ("'Usage: ' + ' <hostname>  <protocol>  <portlow>  <porthigh>'")


main()
