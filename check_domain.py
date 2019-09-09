#!/usr/bin/env python3
import dns.resolver


class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

TYPES = ['MX', 'A', 'AAAA']
active = {}
blacklist = "disposable_email_blocklist.conf"
with open(blacklist, 'r') as blacklist:
    blacklist_content = [line.rstrip() for line in blacklist.readlines()]

    for domain in blacklist_content:
        try:
            print(bcolors.OKBLUE + "[!]" + bcolors.ENDC + 
                  " Checking email records (MX, A, and AAAA) for  " +
                  domain)
            for record_type in TYPES:
                if not active.get(domain, False):
                    for record in dns.resolver.query(domain, record_type):
                        print(bcolors.OKGREEN + "[+] " + bcolors.ENDC +
                              record.to_text())
                        active[domain] = True
        except:
            print(bcolors.FAIL + "[-]" + bcolors.ENDC +
                  " No MX, A, or AAAA record found for " + domain)

with open('valid_domains.txt', 'w') as valid:
    for domain in active.keys():
        valid.write(domain + "\n")
