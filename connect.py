import sys
from xss import xss
from director import directory
from domain import domain
from brutesite import bruteforce

def menu() :
    while(1):
        print("Pick an option :")
        print("1. Brute Force any Login Page")
        print("2. Find Hidden Sub-Directories")
        print("3. Discover Sub-Domains")
        print("4. Cross Site Scripting(XSS) Detection")

        choice = int(input())

        match choice:
            case 1:
                page_url = input(colored("Enter Page URL: ",'blue'))
                username = input(colored("Enter Username for Specified Page: ",'blue'))
                bruteforce(username,page_url)
                break
            case 2:
                target_url = input(colored("Enter Target URL: ",'blue'))
                directory(target_url)
                break
            case 3:
                target_url = input(colored("Enter Target URL: ",'blue'))
                domain(target_url)
                break
            case 4:
                print("XSS")
                target = input(colored("Enter Target URL: ",'blue'))
                xss(target)
                break
            case _:
                print("Not a valid option")

if(len(sys.argv) > 1):
    match sys.argv[1]:
        case "-bf":
            print("bf")
            bruteforce(sys.argv[3],sys.argv[2])
        case "-dir":
            print("dir")
            directory(sys.argv[2])
        case "-sub":
            print("sub")
            domain(sys.argv[2])
        case "-xss":
            print("xss")
            xss(sys.argv[2])
        case "-h":
            print("The available options are :")
            print("-bf URL username")
            print("-dir URL")
            print("-sub URL")
            print("-xss URL")
        case _:
            print("Invalid Parameters")
            print("Use -h for help")
else:
    menu()
