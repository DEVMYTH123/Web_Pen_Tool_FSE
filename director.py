#!/usr/bin/python

import requests
from termcolor import colored

def request(url):
	try:
		return requests.get("http://"+ url)
	except requests.exceptions.ConnectionError:
		pass

def directory(target_url):
	
	file = open("common.txt", 'r')
	for line in file:
		word = line.strip()
		url = target_url + '/' + word
		response = request(url)
		if response:
			print("[!!] Discovered Directory: "+colored(url, 'green'))
	print("[-] No one other subdirectories found. ")
