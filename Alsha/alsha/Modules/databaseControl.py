import socket
import time
import sys
from colorama import init, Fore, Back, Style



def detect_database_Socket(ip):

    services = {

        3306: "MySQL",
        5432: "PostgreSQL",
        1521: "Oracle",
        1433: "Microsoft SQL Server",
        27017: "MongoDB",
        6379: "Redis",
        9042: "Apache Cassandra",
        5984: "CouchDB",
        50000: "IBM DB2"

    }

    print("\nTarget Scanning...")
    print("----------------------------------------------------------------------")
    time.sleep(7)

    for port, service in services.items():

        try:

            #create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(17) #Connection timeout


            # Used to try to establish a connection to the specified port number over a TCP/IP socket
            # If the connection is successfully established, the function sock.connect_ex() returns 0

            result_connect = sock.connect_ex((ip,port))

            # Receive the banner information from the server
            #banner = sock.recv(1024).decode().strip()


            if result_connect == 0:
                print("(Try against #1..)")
                print(Fore.GREEN + f"\n[+]Discovery {port} is open. {service} service is running." + Fore.RESET)

                response = b""
                while True:
                    chunk = sock.recv(1024)
                    if not chunk:
                        break
                    response += chunk
                banner = response.decode().strip()
                print(f"Target Port Version information -->> {banner}\n ")

            else:
                print(f"[-]Port {port} is closed or Filtered.The {service} service is not running here or Filtered")

            sock.close()


        except KeyboardInterrupt:
            print("Program Terminated:::")
            sys.exit(0)

        except socket.timeout:
            print(f"\nConnection to {ip}/{port} timed out.\n")

        except socket.error :
            print("\nSocket Error::: ")
