import socket
import time


def pinging(url):

    print("\nPinging...")
    print("------------------------------------------------\n")
    time.sleep(3)

    try:
        ip = socket.gethostbyname(url)
        print(f" Target IP Address => {ip}")

    except socket.error as error:
        print(f"ERROR => {error}")
