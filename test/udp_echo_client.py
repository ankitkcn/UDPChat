import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999
BUFFER_SIZE = 4096

def run_udp_echo_client():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	while True:
		message = input("Enter Message (or 'quit' to exit): ")
		if not message:
			continue
		if message.lower() == 'quit':
			print("[*] Exiting Client")
			break
		data = message.encode('utf-8')
		sock.sendto(data, (SERVER_HOST, SERVER_PORT))
		print(f"[Sent] {data!r} to {SERVER_HOST}:{SERVER_PORT}")
		
		data_echoed, server_addr = sock.recvfrom(BUFFER_SIZE)
		print(f"[Received] {data_echoed!r} from {server_addr}")
		print()

if __name__ == "__main__":
	run_udp_echo_client()

		
