import socket
import sys
import threading
import time
from collections import defaultdict

# Log file location
LOG_FILE = "connections_log.txt"

# Connection limit constants
CONNECTION_LIMIT = 5  # Max connections per IP in a time window
TIME_WINDOW = 60  # Time window in seconds to track connections (1 minute)
DATA_THRESHOLD = 10240  # 10 KB of data threshold before we suspect DoS or attack

# Create a dictionary to track connection attempts per IP
connection_attempts = defaultdict(list)  # Tracks timestamps of connection attempts per IP

# Blacklist to store IPs that exceed the limit
blacklist = set()

# Create a TCP/IP socket
def create_server_socket(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('0.0.0.0', port)
        server_socket.bind(server_address)
        server_socket.listen(5)
        print(f"Listening for incoming connections on port {port}...")
        return server_socket
    except socket.error as e:
        print(f"Error creating or binding socket: {e}")
        sys.exit(1)

# Log connection and keystrokes to a file
def log_connection_and_keystrokes(client_address, keystrokes):
    try:
        with open(LOG_FILE, "a") as log_file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - Connection from {client_address}:\n")
            log_file.write(f"Keystrokes: {keystrokes}\n")
            log_file.write("-" * 50 + "\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Check if the IP is blacklisted
def is_blacklisted(ip):
    return ip in blacklist

# Add the IP to the blacklist
def add_to_blacklist(ip):
    blacklist.add(ip)
    print(f"IP {ip} added to blacklist.")

# Limit connection attempts
def check_connection_limit(client_address):
    ip = client_address[0]
    current_time = time.time()
    connection_attempts[ip] = [timestamp for timestamp in connection_attempts[ip] if current_time - timestamp < TIME_WINDOW]

    # If number of attempts exceeds the connection limit, block the IP
    if len(connection_attempts[ip]) >= CONNECTION_LIMIT:
        add_to_blacklist(ip)
        return True

    connection_attempts[ip].append(current_time)
    return False

# Handle client connection in a new thread
def handle_client_connection(connection, client_address):
    try:
        if is_blacklisted(client_address[0]):
            print(f"Connection from {client_address[0]} denied (blacklisted).")
            connection.close()
            return
        
        print(f"Connection received from {client_address}")
        
        # Initialize keystrokes capture
        keystrokes = ""
        data_received = 0  # To track the amount of data received

        # Set a timeout for reading data from client (optional)
        connection.settimeout(60)  # 60 seconds timeout for reading data
        
        while True:
            # Receive data from the client
            data = connection.recv(1024)  # Buffer size of 1024 bytes
            if data:
                # Capture keystrokes
                keystrokes += data.decode("utf-8", errors="ignore")  # Decode bytes to string
                print(f"Keystrokes from {client_address}: {data.decode('utf-8', errors='ignore')}")
                
                data_received += len(data)
                
                # If the data threshold is exceeded, consider this a possible attack
                if data_received > DATA_THRESHOLD:
                    print(f"Suspicious data volume detected from {client_address}, closing connection.")
                    connection.close()
                    return
            else:
                # No data (client may have closed connection)
                break
        
        # Log connection and keystrokes to file
        log_connection_and_keystrokes(client_address, keystrokes)
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        try:
            connection.close()
            print(f"Connection to {client_address} closed.")
        except socket.error as e:
            print(f"Error closing connection to {client_address}: {e}")

# Main server function
def main():
    port = 22  # Port 22 (SSH port), requires root access on many systems
    server_socket = create_server_socket(port)

    try:
        while True:
            try:
                # Accept a new incoming connection
                connection, client_address = server_socket.accept()

                # Check if the connection should be limited or blocked
                if check_connection_limit(client_address):
                    print(f"Too many connection attempts from {client_address[0]}, blocking IP.")
                    connection.close()
                    continue

                # Start a new thread to handle the client connection
                client_thread = threading.Thread(target=handle_client_connection, args=(connection, client_address))
                client_thread.daemon = True  # Allow thread to exit when main program ends
                client_thread.start()

            except socket.error as e:
                print(f"Error accepting connection: {e}")
            except KeyboardInterrupt:
                print("\nServer interrupted, shutting down...")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
    finally:
        # Close the server socket when shutting down
        print("Server is shutting down...")
        try:
            server_socket.close()
        except socket.error as e:
            print(f"Error closing the server socket: {e}")
        sys.exit(0)

if __name__ == "__main__":
    main()
