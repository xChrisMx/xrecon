#!/usr/bin/env python3

########################################################################################
# Purpose: This python script consists of several attack surface mapping / recon tools to
#          identify, assess and mitigate potential attack vectors.
#          This script is work in progress and will most likely evolve.
#
# Usage:  python3 jwrecon.py
#               or
#         chmod +x xrecon.py
#         ./xrecon.py
#
# Version: v. 0.3 | modified: 09/17/2024
#
# Notice: 1. Ensure you are authorized to use this cript.
#         2. Never use this script just for curiosity/iresponsibly. Reason should be legitimate.
#         3. Script can be noisy. Avoid option #5 unless reason is legitimate.
#
# Created: 03/15/2021 | Author: Chris Miculescu | v. 0.1 | Audience: Bethel SOC
#          07/12/2024 Script ported over to python | v. 0.2
#          09/17/2024 Added DMITRY and Fierce sweeps to script | v. 0.3
########################################################################################

import subprocess

###############################
#########CONFIGURATION#########
###############################

# COLORS
BOLD = "\033[1m"
NORMAL = "\033[0m"
GREEN = "\033[1;32m"
MAGENTA = "\033[95m"
YELLOW = "\033[33m"
DEFAULT = "\033[39m"
LOLCAT = "/usr/games/lolcat -a"

##############################################
################Extra Sweep###################
##############################################

def extra_sweep():
    print(NORMAL)
    domain = input("Enter a domain (or IP): ")
    print(YELLOW + f"Running Nikto {domain}" + NORMAL)
    subprocess.run(["nikto", "-ask=no", "-host", domain])
    print("")

    print(YELLOW + f"Running Nuclei on {domain}" + NORMAL)
    subprocess.run(["nuclei", "-u", domain])
    print("")

##############################################
###############Detailed Sweep#################
##############################################

def detailed_sweep():
    print(NORMAL)
    domain = input("Enter a domain (or IP): ")
    
    print("")
    print(YELLOW + f"Checking SSH Algos on {domain}" + NORMAL)
    subprocess.run(["sudo", "nmap", "--script", "ssh2-enum-algos", "-sV", "-p", "22", domain])
    print("")

    print(YELLOW + f"Running Web App Firewall Fingerprinting on {domain}" + NORMAL)
    subprocess.run(["wafw00f", domain])
    print("")

    print(YELLOW + f"Identifying Redirects on {domain}" + NORMAL)
    subprocess.run(["curl", "-sSik", domain])
    print("")

    print(YELLOW + f"Checking for DNS/HTTP Load Balancer on {domain}" + NORMAL)
    subprocess.run(["lbd", domain])
    print("")

    print(YELLOW + f"Checking OpenSSL Cipher negotiation on {domain}" + NORMAL)
    subprocess.run(["sh", "-c", f"true | openssl s_client -connect {domain}:443 | egrep -i '(TLS|SSL|Protocol|Cipher)'"])
    print("")

    print("")
    print(YELLOW + f"Checking All Supported OpenSSL Ciphers on {domain}" + NORMAL)
    subprocess.run(["sudo", "nmap", "--script", "ssl-enum-ciphers","-p", "443", domain])
    print("")



##############################################
#################Ping Sweep###################
##############################################

def ping_sweep():
    print(NORMAL)
    domain = input("Enter a domain (or IP): ")

    print("")
    print(YELLOW + f"Running ICMP Echo Ping on {domain}" + NORMAL)
    subprocess.run(["sudo", "nmap", "-sn", "-PE", domain])
    print("")

    print(YELLOW + f"Running TCP SYN Ping on {domain}" + NORMAL)
    subprocess.run(["sudo", "nmap", "-sn", "-PS22-25,80,113,442,445,8080", domain])
    print("")

    print(YELLOW + f"Running TCP ACK Ping on {domain}" + NORMAL)
    subprocess.run(["sudo", "nmap", "-sn", "-PA", domain])
    print("")

    print(YELLOW + f"Running UDP Ping on {domain}" + NORMAL)
    subprocess.run(["sudo", "nmap", "-sn", "-PU", domain])
    print("")


##############################################
##############What Web########################
##############################################

def what_web():
    print(NORMAL)
    domain = input("Enter a domain (or IP): ")

    print("")
    print(YELLOW + f"Running a WhatWeb Technology scan on {domain}" + NORMAL)
    subprocess.run(["sudo", "whatweb", "-v", "--colour=always", domain])
    print("")


##############################################
##############Dmitry########################
##############################################

def dmitry_sweep():
    print(NORMAL)
    domain = input("Enter a domain (or IP): ")

    print("")
    print(YELLOW + f"Running DMITRY (deep magic info gather) on {domain}" + NORMAL)
    subprocess.run(["sudo", "dmitry", "-winseo", "--colour=always", domain])
    print("")


##############################################
##############Fierce########################
##############################################

def fierce_sweep():
    print(NORMAL)
    domain = input("Enter a domain (or IP): ")

    print("")
    print(YELLOW + f"Running Fierce (DNS interrogation) on {domain}" + NORMAL)
    subprocess.run(["sudo", "fierce", "--domain", domain])
    print("")


##############################################
###############MENU FUNCTION##################
##############################################
def menu():
    print(YELLOW)
    print("-------------------------------------------------------------------")
    print("xrecon - A small collection of Attack Surface Mapping / recon Tools")
    print( "v 0.3 - 09/2024")
    print("-------------------------------------------------------------------")
    print("")

    while True:
        print(GREEN + "MENU")
        print("1) What Web: Identify Web Technologies used (yields lots of info)")
        print("2) Ping Sweep: ICMP, TCP SYN, TCP ACK, UDP (~95% discovery rate)")
        print("3) Detailed: SSH Algos, Web Tech, FW Fingerprint, HTTP/DNS LB's, OpenSSL Ciphers")
        print("4) Extras: Nikto, Nuclei (detect web app vulnerabilities)")
        print("5) DMITRY: DNS Deep Info Gathering Tool (subdomains, emails, uptime info)")
        print("6) Fierce: DNS Interrogation Tool (extensive IP space lookups)")
        print("7) ALL Options: Run everything (NOISY; will take a while)")
        print("q) Exit")
        print(NORMAL)
        op = input("Choose an option: ")
        if op.startswith('1'):
            what_web()
        if op.startswith('2'):
            ping_sweep()
        elif op.startswith('3'):
            detailed_sweep()
        elif op.startswith('4'):
            extra_sweep()
        if op.startswith('5'):
            dmitry_sweep()
        if op.startswith('6'):
            fierce_sweep()
        elif op.startswith('7'):
            ping_sweep()
            detailed_sweep()
            extra_sweep()
            dmitry_sweep()
            fierce_sweep()
        elif op.lower() == 'q':
            break
        else:
            print("Choose a valid option")

# LAUNCH SCRIPT
menu()

