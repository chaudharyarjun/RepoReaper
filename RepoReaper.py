#!/usr/bin/env python3
import requests
from termcolor import colored, cprint
import os

def print_banner():
    os.system('clear')
    banner = """
8888888b.                            8888888b.                                             
888   Y88b                           888   Y88b                                            
888    888                           888    888                                            
888   d88P .d88b.  88888b.   .d88b.  888   d88P .d88b.   8888b.  88888b.   .d88b.  888d888 
8888888P" d8P  Y8b 888 "88b d88""88b 8888888P" d8P  Y8b     "88b 888 "88b d8P  Y8b 888P"   
888 T88b  88888888 888  888 888  888 888 T88b  88888888 .d888888 888  888 88888888 888     
888  T88b Y8b.     888 d88P Y88..88P 888  T88b Y8b.     888  888 888 d88P Y8b.     888     
888   T88b "Y8888  88888P"   "Y88P"  888   T88b "Y8888  "Y888888 88888P"   "Y8888  888     
                   888                                           888                       
                   888                                           888       by: Chaudhary_S4h4b               
                   888                                           888                       
    """
    cprint(banner, 'green')
    cprint("RepoReaper: The relentless seeker of hidden treasures", 'cyan', attrs=["bold"])
    cprint("-------------------------------------------------------------------------------------------", 'yellow')
    cprint("Hunting down exposed .git repositories one URL at a time.", 'red', attrs=["bold"])

print_banner()

def check_git_exposed(url):
    # Ensuring the URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url + '/.git/HEAD', timeout=5)
        
        if response.status_code == 200 and 'ref: ' in response.text:
            return True
    except requests.exceptions.RequestException as e:
        print(colored(f"[Skipping] Request Failed for {url}", 'yellow'))
    
    return False

def main():
    filename = input("Enter the path of the file containing domains: ")
    with open(filename, 'r') as file:
        urls = file.read().splitlines()

    exposed_count = 0
    for url in urls:
        if check_git_exposed(url):
           
            print(colored(f"[+] {url} exposes .git file.", 'green'))
            exposed_count += 1
        else:
            print(colored(f"[-] {url} does not expose .git file.", 'red'))

    print("\n")
    cprint(f"RepoReaper has finished its scan. {exposed_count} out of {len(urls)} domains exposed .git files.", 'cyan')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cprint("\n\nInterrupt received! Stopping RepoReaper...", "magenta", attrs=["bold", "blink"])
        exit()
