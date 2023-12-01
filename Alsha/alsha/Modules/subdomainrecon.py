import requests
import time
import sys
import os
from colorama import init, Fore, Back, Style
import argparse

def discovery_subdomain_target(target_domain, protocol):

    print("Discovery Subdomain....")
    print(f"Target Site => {target_domain}")
    print(f"Protocol => {protocol}")
    print("----------------------------------------------------\n")

    current_working_directory = os.getcwd()
    #print("Current Working Directory:", current_working_directory)

    file_path = os.path.join(current_working_directory, "Modules", "Subdomain.txt")

    try:
        with open (file_path,'r') as file:
            file_read = file.readlines()
            for sub_word in file_read:
                clear_subdomain = sub_word.strip()

                target_request = f"{protocol}://{clear_subdomain}.{target_domain}"

                try:
                    response_site = requests.get(target_request, verify=True)

                    if response_site.status_code == 200:
                        print(Fore.GREEN + f"[+]Discovery {clear_subdomain} in {target_domain}   Subdomain:[{clear_subdomain}]  Status Code[200]\n" + Fore.RESET)
                        time.sleep(0.5)

                    elif response_site.status_code == 403:
                        print(f"Return Forbidden 403 and {clear_subdomain} is not in {target_domain} Subdomain:[{clear_subdomain}]  Status Code[403]\n")

                    else:
                        print(f"Failed to retrieve {clear_subdomain} in {target_domain}. Status Code: {response_site.status_code}")

                except requests.ConnectionError as e:
                    #print(f"Connection Error for {clear_subdomain}.{target_domain}: {e}")
                    pass

                except requests.ConnectionError as e:
                    #print(f"Connection Error for {clear_subdomain}.{target_domain}: {e}")
                    pass

    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram Terminated:::" + Fore.RESET)
        sys.exit(0)

    except Exception as e:
        print(f"Error => {e}")