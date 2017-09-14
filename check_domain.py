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

active = []
blacklist = "disposable_email_blacklist.conf"
with open(blacklist, 'r') as blacklist:
    blacklist_content = [line.rstrip() for line in blacklist.readlines()]

    for domain in blacklist_content:
        try:
            validated = False
            print(bcolors.OKBLUE + "[!]" + bcolors.ENDC + " MX records for  " +
                  domain)
            for mx in dns.resolver.query(domain, 'MX'):
                print(bcolors.OKGREEN + "[+] " + bcolors.ENDC + mx.to_text())
                if not validated:
                    active.append(domain)
                    validated = True
        except:
            print(bcolors.FAIL + "[-]" + bcolors.ENDC +
                  " No MX record found for " + domain)

with open('valid_domains.txt', 'w') as valid:
    for domain in active:
        valid.write(domain + "\n")
