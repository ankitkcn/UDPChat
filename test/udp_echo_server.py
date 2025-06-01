import socket

SERVER_HOST = '127.0.0.1' #Allow connections from all interfaces LAN, WAN etc
SERVER_PORT = 9999

def run_udp_echo_server():
	print("running")
	#create a UDP Socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#Bind to Socket: Tell OS about it
	try:
		sock.bind((SERVER_HOST, SERVER_PORT))
	except OSError as e:
		print(f"error binding socket: {e}")
	
	print(f"[+] UDP Echo Server listening on {SERVER_HOST}: {SERVER_PORT}")
	
	while True:
		data, client_addr = sock.recvfrom(4096)
		## client_addr is a tuple (client_ip: str, client_port: int)
		print(f"[Recieved]{data!r} from {client_addr}")
		
		#Echo data back
		sent_bytes = sock.sendto(data, client_addr)
		print(f"[Sent back] {sent_bytes} bytes to {client_addr}")
	
if __name__ == '__main__':
	run_udp_echo_server()
	
