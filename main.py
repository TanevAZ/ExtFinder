import os
import platform
from colorama import Fore

pm = platform.system()
if pm == "Windows":
    os.system("cls")
elif pm == "Linux":
    os.system("clear")
elif pm == "Darwin":
    os.system("clear")
banner = Fore.RED + f"""
                             _____     _  ______ _           _           
                            |  ___|   | | |  ___(_)         | |          
                            | |____  _| |_| |_   _ _ __   __| | ___ _ __ 
                            |  __\ \/ / __|  _| | | '_ \ / _` |/ _ \ '__|
                            | |___>  <| |_| |   | | | | | (_| |  __/ |   
                            \____/_/\_\\__ \_|   |_|_| |_|\__,_|\___|_|   

                                Github : https://github.com/TanevAZ

"""

print(banner)

def main():
    # ask user for directory to search
    directory = input(f'\n{Fore.RESET}Enter the directory to search : ')
    # ask user for extension to search 
    extension = input(f'Enter the extension to search for : {Fore.LIGHTGREEN_EX}')
    # search for file in directory and all subdirectories
    found = False
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(extension):
                print(f'{Fore.RESET}File {Fore.LIGHTGREEN_EX}found(s){Fore.RESET} in : {root}')
                found = True
    if not found:
        print(f'{Fore.RESET}Extension not {Fore.LIGHTRED_EX}found{Fore.RESET}')
    input(f"\n{Fore.LIGHTGREEN_EX}Scan Terminated. {Fore.WHITE}Press Enter to Exit...")
    exit()

main()