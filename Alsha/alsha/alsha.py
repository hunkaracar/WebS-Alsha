#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup
import socket
import time
import argparse
import builtwith
import sys
from colorama import init, Fore, Back, Style
import colorama
from scapy.all import *

try:

    sys.path.append("./Modules")
    from robots import query_robots_file
    from databaseControl import detect_database_Socket
    from ping import pinging
    from portScan import detect_portScan
    from directoryDiscover import discover_directory

except Exception as e:
    print(f"ERROR => {e}")



class Scraping:

    def __init__(self):
        print("\nStarting Up...")
        init()


    def get_documentation(self):

        parser = argparse.ArgumentParser(
            prog='alsha',
            description='Detailed web browsing',
        )

        print("""
        
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$							                                 
$							                                 
$        ('-.                .-')    ('-. .-.   ('-.         $
  ( OO ).-.           ( OO ). ( OO )  /  ( OO ).-.           $
  / . --. / ,--.     (_)---\_),--. ,--.  / . --. /           $
  | \-.  \  |  |.-') /    _ | |  | |  |  | \-.  \            $
.-'-'  |  | |  | OO )\  :` `. |   .|  |.-'-'  |  |           $
 \| |_.'  | |  |`-' | '..`''.)|       | \| |_.'  |           $
  |  .-.  |(|  '---.'.-._)   \|  .-.  |  |  .-.  |           $
  |  | |  | |      | \       /|  | |  |  |  | |  |           $
  `--' `--' `------'  `-----' `--' `--'  `--' `--'           $
$							                                 
$	AUTHOR:Hünkar Acar 			                         
$	Program:Alsha				                         
$	Program Purpose: Web information and security scanning	                 
$				     			                             
$				                                             
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        
        """)

        time.sleep(2)

        parser.add_argument('-u','--url',type=str,help='general scanning and detection / parameter => http://www.example.com/')
        parser.add_argument('-uT','--usedT',type=str,help='Shows the technologies used / parameter => http://www.example.com/')
        parser.add_argument('-dbs','--database',type=str,help='shows the database used / parameter =>  <target IP> ')
        parser.add_argument('-fw','--firewall',type=str,help='detects whether there is a firewall / parameter => <target IP>')
        parser.add_argument('-R','--robots',type=str,help='Detects if robots.txt file exists  / parameter => http://www.example.com ')
        parser.add_argument('-sS','--SYN',help='Port Scanning target Web site / parameter => <target IP> ')
        parser.add_argument('-Pn','--ping',type=str,help='Ping the destination address and show the ip address / parameter => www.example.com ')
        parser.add_argument('-D','--directory',type=str,help='Detects directories and hidden directories within the website / parameter => http:// www.example.com ')


        args = parser.parse_args()

        return args

        """
        try:
            args = parser.parse_args()

            if args.url is None:
                print("You must enter the URL/U  option!")
                sys.exit()

            return args

        except AttributeError:

            print("\n-------You must enter the URL/U option!----------")
            ascii_parser = pyfiglet.figlet_format("try again")
            print(ascii_parser)


        """


    def request_web(self,url):

        print("General Scanning...")
        print(f"Target Web site {url}")
        print("-------------------------------------------------------------------------------")
        time.sleep(4)

        #by-pass SSL verify = True
        web_response = requests.get(url,verify=True)

        if web_response.status_code == 200:
            print(Fore.GREEN+f"\n[+] status code: {web_response.status_code} ")
            #print(f"\n [+] web_text: {web_response.headers} ")

            web_res = web_response.headers

            for key,value in web_res.items():
                print(key + ":")
                for line in value.split("\n"):
                    print("\t" + line)

        else:
            return None

        response_time = web_response.elapsed.total_seconds()

        print(Fore.RED + f"\nseconds => {response_time}" + Fore.RESET)


    def get_bs4(self,url):

        print("Scanning Technologies Used...")
        print(f"Target Web site {url}")
        print("-------------------------------------------------------------------------------")
        time.sleep(4)

        try:

            response = requests.get(url,verify=True)

            soup_parser = BeautifulSoup(response.content,'html.parser')
            title = soup_parser.title.string

            #We get all the links (a tag) on the web page
            links = [link.get('href') for link in soup_parser.find_all('a')]

            print("="*40)
            print(Fore.RED+"[+]Title =>", title+Fore.RESET)
            print("=" * 40)

            for lk in links:
                print("=" * 40)
                print("links: {}".format(lk))
                print("=" * 40)


            scripts = [script.get('src') for script in soup_parser.find_all('script')]

            for sc in scripts:
                print("=" * 40)
                print("Scripts File: {}".format(sc))
                print("=" * 40)


            if soup_parser.find_all("link", rel="stylesheet",href=lambda  href: href and href.startswith("wp-")):
                print(Fore.GREEN+"\n\n[+]This website is built with Wordpress"+Fore.RESET)

            else:
                print(Fore.RED+"\n\n==>[-]This web site is not built with WordPress\n\n"+Fore.RESET)


        except requests.exceptions.RequestException as e:
              print("An error occurred:", e)



    def get_used_technology(self, url):

        web_result = builtwith.parse(url)
        print("\n\nTechnologies used by the site:\n")

        print("===========================================")
        for key, value in web_result.items():
            print(key + ":")
            for line in value:
                print("\t" + line)

        print("===========================================")
        
        




    def get_detection_firewall(self,ip):

        #ping to target
        #check your ping response

        print("\nBeing detected...")
        print("----------------------------------------------------------\n")
        time.sleep(2)
        ans,uns = sr(IP(dst=ip)/ICMP(), timeout=25,verbose=0)

        if ans:
            print(Fore.RED+"[+]Firewall detect" + Fore.RESET)
        else:
            print(Fore.WHITE+"\n=>!!! Firewall not detect !!!\n" + Fore.RESET)


    def get_detect_RobotsFile(self,url):

        try:
            print(query_robots_file(url))

        except Exception as e:
            print(f"Error => {e}")



    def get_detection_database(self,ipv4):

        try:
            print(detect_database_Socket(ipv4))

        except Exception as er:
            print(f"ERROR => {er}")


        """
        
         response = requests.get(url2,verify=True)

        soup_parser = BeautifulSoup(response.content,'html.parser')

        if "mysql" in soup_parser or "mysqli" in soup_parser or "mssql" in soup_parser or "sqlite" in soup_parser:
            print(Fore.GREEN+"\n\n[+]this website uses database")
        else:
            print(Fore.RED+"\n\nb[-]this website does not use database\n")
      
        """


    def ping_ing(self,url):

        try:
            print(pinging(url))

        except Exception as error:
            print(f"ERROR => {error}")


    def port_Scan(self,target_IP):

        try:
            detect_portScan(target_IP)

        except Exception as error:
            print(f"ERROR => {error}")



    def discover_Directory(self,base_url):

        try:
            discover_directory(base_url)

        except Exception as error:
            print(f"ERROR => {error}")




if __name__ == "__main__":

    scraping = Scraping()
    args = scraping.get_documentation()


    try:

        if args.url:
            scraping.get_bs4(args.url)
            scraping.request_web(args.url)

        if args.usedT:
            scraping.get_used_technology(args.usedT)

        if args.database:
            scraping.get_detection_database(args.database)

        # scraping.get_detection_firewall(args.firewall)

        if args.firewall:
            scraping.get_detection_firewall(args.firewall)

        if args.robots:
            scraping.get_detect_RobotsFile(args.robots)

        if args.ping:
            scraping.ping_ing(args.ping)

        if args.SYN:
            scraping.port_Scan(args.SYN)

        if args.directory:
            scraping.discover_Directory(args.directory)



    except Exception as e:
        print(f"ERROR => {e}")
