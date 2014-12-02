import sys, getopt
import socket

import string
import random

from time import sleep

def random_string( pktSize ):

	# Just alphanumeric characters
	chars = string.letters + string.digits

	# Alphanumeric + special characters
	chars = string.letters + string.digits + string.punctuation

	if int(pktSize) <= 0:
		print 'packet size cannot be zero'
		sys.exit(2)

	return ''.join((random.choice(chars)) for x in range(int(pktSize)))



def main(argv):
   #print random_string()
   port = ''
   interface = ''
   numberofpackets = ''
   size = ''
   try:
      opts, args = getopt.getopt(argv,"hp:i:n:s:d",["port=","interface=", "numberofpackets=","size="])
   except getopt.GetoptError:
      print 'test.py -p <port> -i <interface> -n <numberofpackets> -s <size>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -p <port> -i <interface> -n <numberofpackets> -s <size>'
         sys.exit()
      elif opt in ("-p", "--port"):
         port = arg
      elif opt in ("-i", "--interface"):
         interface = arg
      elif opt in ("-n", "--numberofpackets"):
         numberofpackets = arg
      elif opt in ("-s", "--size"):
         size = arg
      else:
         print 'test.py -p <port> -i <interface> -n <numberofpackets> -s <size>'
         sys.exit(2)
		 
  #For debugging
  #print 'The port "', port 
  #print 'The interface "', interface
  #print 'The numberofpacktes"', int(numberofpackets)
  #print 'The packet size"', int(size)


	#Validate the parsed data
   if port == '' or interface == '' or numberofpackets == '' or size == '':
		print 'test.py -p <port> -i <interface> -n <numberofpackets> -s <size>'
		sys.exit(2)

   #enter the data content of the UDP packet as hex
   #PACKETDATA='f1a525da11f6'.decode ('hex')
   
   #initialize a socket, think of it as a cable
   #SOCK_DGRAM specifies that this is UDP
   s=socket.socket (socket.AF_INET, socket.SOCK_DGRAM, 0)
   #connect the socket, think of it as connecting the cable to the address location
   s.connect ((interface, int(port)))
   #send the command
   for i in range(0,int(numberofpackets)):
		#sleep(0.001) #sleep during 1ms
		PACKETDATA=random_string(size)
		#print PACKETDATA
		s.send (PACKETDATA)
   #close the socket
   s.close ()

if __name__ == "__main__":
   main(sys.argv[1:])
