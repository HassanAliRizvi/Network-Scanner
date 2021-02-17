# Python Network Scanner

A simple network scanner built in python to find local IP and MAC addresses. 

## Table of contents
- [General info](https://github.com/HassanAliRizvi/Network-Scanner#general-info)
- [Technologies](https://github.com/HassanAliRizvi/Network-Scanner#technologies)
- [Features](https://github.com/HassanAliRizvi/Network-Scanner#features)
- [Setup](https://github.com/HassanAliRizvi/Network-Scanner#setup)
- [Usage](https://github.com/HassanAliRizvi/Network-Scanner#usage)

## General Info
Even though you can use "netdiscover" command from the terminal to get the IP and MACs of the local computers, a better way is to understand how it runs and ultimately build a program like this which could detect which IPs and MACs are connected to your network. Therefore, the program was built on that motivation. 

## Technologies

Project is created with:

-   Python 3.8
-   VM Virtual Box
-   PyCharm

Python 3.8 Libraries-   Scapy
-   ipaddress
-  optparse
- re

## Features
- detecting the IP and MAC addresses of local computers
- check if the IP address is valid

### TO-DO: 
- Detect the type of OS once IP and MAC address has been received. 
 
## Setup

After naviagting to the directory you want to save the project to save into, do a simple clone of the project through  `git clone https://github.com/HassanAliRizvi/Network-Scanner.git`.

## Usage
Once you navigate to the project file location, you can type in the following command from the terminal:-
`sudo python3 network_scanner2.py --target [ip-address]`
### NOTE: Please replace ip-address with the IP address you want to target!
