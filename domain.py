#!/usr/bin/python

import requests
from termcolor import colored

def request(url):
	try:
		return requests.get("http://"+ url)
	except requests.exceptions.ConnectionError:
		pass

def domain(target_url):
	file = open("subdomains.txt", 'r')
	for line in file:
		word = line.strip()
		url = word+ "."+ target_url
		response = request(url)
		if response:
			print("[!!] Discovered Subdomains: "+colored(url, 'green'))
	print("[-] No one other subdomains found. ")
