from scapy.all import *
import time
import sys
from colorama import init, Fore, Back, Style


def detect_portScan(target_ip):

    print("Port Scanning...")
    print(f"Scanning {target_ip} [35 Ports]")
    print("------------------------------------------------------------")
    time.sleep(7)
    ports = {
        21: "TCP Port 21 (FTP)",
        22: "TCP Port 22 (SSH)",
        23: "TCP Port 23 (Telnet)",
        25: "TCP Port 25 (SMTP)",
        53: "TCP Port 53 (DNS)",
        80: "TCP Port 80 (HTTP)",
        110: "TCP Port 110 (POP3)",
        143: "TCP Port 143 (IMAP)",
        443: "TCP Port 443 (HTTPS)",
        445: "TCP Port 445 (SMB)",
        3389: "TCP Port 3389 (RDP)",
        53: "UDP Port 53 (DNS)",
        69: "UDP Port 69 (TFTP)",
        123: "UDP Port 123 (NTP)",
        139: "TCP Port 139 (NetBIOS)",
        161: "TCP Port 161 (SNMP)",
        443: "TCP Port 443 (HTTPS)",
        587: "TCP Port 587 (SMTP SSL)",
        993: "TCP Port 993 (IMAP SSL)",
        995: "TCP Port 995 (POP3 SSL)",
        1433: "TCP Port 1433 (Microsoft SQL Server)",
        1723: "TCP Port 1723 (PPTP)",
        3306: "TCP Port 3306 (MySQL)",
        5900: "TCP Port 5900 (VNC)",
        8080: "TCP Port 8080 (HTTP Proxy)",
        8443: "TCP Port 8443 (HTTPS-alt)",
        1194: "TCP Port 1194 (OpenVPN)",
        1521: "TCP Port 1521 (Oracle Database)",
        3306: "TCP Port 3306 (MySQL)",
        5432: "TCP Port 5432 (PostgreSQL)",
        5900: "TCP Port 5900 (VNC)",
        8000: "TCP Port 8000 (HTTP Alt)",
        9000: "TCP Port 9000 (Elasticsearch)",
        9100: "TCP Port 9100 (Printer)",
        27017: "TCP Port 27017 (MongoDB)",
    }

    try:

        #Send small TCP SYN packets to target IP
        for port in ports:

            packets = IP(dst=target_ip) / TCP(dport=port, flags="S")

            #This function waits and responds to receive the response of the transaction packet.
            #The timeout value refers to the specified time to wait for the packet's response.
            syn_response = sr1(packets,timeout=17,verbose=0)

            if syn_response and syn_response.haslayer(TCP) and syn_response[TCP].flags == "SA":
                print(Fore.GREEN+f"\n[+]Discovery open {port}/{ports[port]} on {target_ip}" + Fore.RESET)

                # Get SYN/ACK response
                synack_packet = IP(dst=target_ip) / TCP(dport=port, sport=syn_response[TCP].dport, seq=syn_response[TCP].ack, ack=syn_response[TCP].seq + 1, flags="S")
                synack_response = sr1(synack_packet, timeout=15, verbose=0)

                #Get Banner info
                if synack_response and synack_response.haslayer(TCP):
                    banner_v = synack_response[TCP].payload.load.decode('utf-8')
                    print(f"Target port Version Information -->> {banner_v}\n")

            else:
                print(f"\n[-]Discovery closed or filtered! {port}/{ports[port]} on {target_ip}")


        print("\nCompleted Connect Scan... (35 total ports) => Most Used ")

    except KeyboardInterrupt:
        print("\nProgram Terminated:::")
        sys.exit(0)


    except Exception as e:
        print(f"\nERROR => {e}")
