# Web_Pen_Tool_FSE

A simple command line web pentesting tool.

## Supports: -
* Brute Forcing Login
* Finding Hidden Sub-Directories
* Discovering Sub-Domains
* Cross Site Scripting (XSS) Detection

# How to setup

Requires Python to run.
Simply, clone the git repository and once in the directory run
```
git clone git@github.com:DEVMYTH123/Web_Pen_Tool_FSE.git
pip install -r requirements.txt
```
This will install the required python modules

To start the command line utility in menu mode run main.py using either
```
python3 main.py
OR
python main.py
```

![image](https://github.com/DEVMYTH123/Web_Pen_Tool_FSE/blob/main/SS.jpg)

OR

To use it as a command see the options with
```
python3 main.py -h
```
or
```
python main.py -h
```

The word lists used in the utility can be found in certain Linux OS using the ```locate``` command
Examples:-
* ```locate common```
* ```locate password```
* ```locate subdomains```

# How to use

## Brute Forcing login
Give the login page URL and the username. The program will attempt to brute force the password using a dictionary attack.

The passwords list is stored in ```passwordlist.txt ```. This file can be updated to increase the number of passwords to try.

## Finding Hidden Sub-Directories
Give the website URL. The program attempts to fuzz this URL to find a response back.

The sub-directory names that will be attempted are stored in ```common.txt``` which can be modified to add or remove sub-directory names.

## Discovering Sub-Domains
Give the domain URL. The program attempts to find any existing URL by appending sub-domain names to the front of it.

The sub-domain words that will be attempted are stored in ```subdomains.txt``` which can be modified to add or remove sub-domain words.

## Cross-Site Scripting (XSS) Detection
Give the website URL. The program attempts to send an XSS alert payload to the website and awaits a response to confirm vulnerability.
