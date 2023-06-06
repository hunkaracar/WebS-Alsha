import requests
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup

"""
In general, the robots.txt file is the files created by the developers to prevent the robots of the browsers from seeing it, 
we can get detailed information about the website by looking at it.

"""

def query_robots_file(url):
    robots_url = url + "/robots.txt"

    #verifiy=True for https site
    response = requests.get(robots_url,verify=True)

    if response.status_code == 200:
        print(Fore.GREEN + "\n^^^^Detect Robots.txt^^^^\n" + Fore.RESET)
        print("=========================================================")
        soup = BeautifulSoup(response.text,"html.parser")
        print(soup.get_text())
        print("=========================================================")


    else:
        print(Fore.RED + "\n!!! Not Detect Robots.txt !!!\n" + Fore.RESET)
