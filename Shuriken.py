#!/usr/bin/python3

import requests
import sys
import argparse
import os
import random
import time
import threading

banner_ghost = """
  .-')    ('-. .-.             _  .-')          .-. .-')     ('-.       .-') _
 ( OO ). ( OO )  /            ( \( -O )         \  ( OO )  _(  OO)     ( OO ) )
(_)---\_),--. ,--. ,--. ,--.   ,------.  ,-.-') ,--. ,--. (,------.,--./ ,--,'
/    _ | |  | |  | |  | |  |   |   /`. ' |  |OO)|  .'   /  |  .---'|   \ |  |\
\  :` `. |   .|  | |  | | .-') |  /  | | |  |  \|      /,  |  |    |    \|  | )
 '..`''.)|       | |  |_|( OO )|  |_.' | |  |(_/|     ' _)(|  '--. |  .     |/
.-._)   \|  .-.  | |  | | `-' /|  .  '.',|  |_.'|  .   \   |  .--' |  |\    |
\       /|  | |  |('  '-'(_.-' |  |\  \(_|  |   |  |\   \  |  `---.|  | \   |
 `-----' `--' `--'  `-----'    `--' '--' `--'   `--' '--'  `------'`--'  `--'  Follow the project : https://github.com/Ph3nX-Z/Shuriken \n"""

shuriken = """
       --
       :hs-
       :hhhs-
       :hhhhhs:---------`
       :hhhyyyhhhhhddds:`
     `:syh-` `:ddddho-
   ./syhhh.   -ddh+.            Follow the project : https://github.com/Ph3nX-Z/Shuriken
 .+yhdddddhsoshhh:
`::://////+hdddhh:
           `/hddh:
             `+hd:
               `+-  \n """

banner = "丂卄ㄩ尺讠长🝗𝓝"
banner_big = """
-:::::::::::::::-      oyy    oys                           -////////////-     -o/          `hh+       -o:
sNNNNMMNNNNNNNNNd      dMM    mMM        ++:       ++-      oMMNNNNNNNNMMy     +NMh.        `MMs   `:smMMm:       /mmmmmmm.    .+sss:    `+sso.
    oMM`               dMM    mMM        MMy      `MMo      oMM`       NMy      -h+`        `MMs +dMMNy+.         /MM:::::`   oMhdMMMh  .NMoyMm-
   `NMd//////o:`  `::::mMM::::NMM::::`   MMy      `MMo      oMMddddddddMMy   ohhhh+         `MMs `o/.             /MM          ` mMMMMs yMm  .
   +MMNNNNNNMMM-  .MMMMMMMMMMMMMMMMMM/   MMy      `MMo      sMM+++dMN++hdo   +ssMMy       sMMMMMMMMMMMMMMMMM/sNNNNNMMNNNNh      /MM/MMM:MM+
   :++      mMd        dMM    mMM        MMy      `MMo      dMN   -MMo          MMy       .-:MMy--:mMd:-----``....oMM.....      dMh hMMNMN`
           -MM+        dMM    mMM        MMmyyyyyyhMMo     :MMo    -mMm+.       MMy.+:      `MMs   .dMN+`         /MM       -+ -MM: -MMMMs
        syyNMh         dMM    mMM        osssssssssMMo    +MMh       +dMMmy:    MMMMMo      .MMy/    /mMMdo:`     /MMmmmmm+/NMdmN+   hMMm.
        shhho          dMM    mMM                  ``    .hMo          .+yd.   -NMh/`       +MMMmhs    :smMh.     `-------`  -:-`    `:`
                       ://    ://                          `                    .`             /:`          `                                     Follow the project : https://github.com/Ph3nX-Z/Shuriken \n"""
liste_banner=[banner_ghost,banner_big,shuriken]

os.system('cls' if os.name == 'nt' else 'clear')

nombre = random.randint(0,2)

print(liste_banner[nombre])
################################################################ Args

parse = argparse.ArgumentParser()
parse.add_argument("-w","--wordlist", help="To specify the wordlist", required=True)
parse.add_argument("-u", "--url", help="To specify the URL", required=True)
parse.add_argument("-p", "--proxies", help="Add proxys", required=False)
parse.add_argument("-P", "--pattern", help="To Specify a pattern (url), keep response that are differents", required=False, type=str)
parse.add_argument("-b", "--bytechange", help="Specify a default size, kepp response that are differents (only for threads options)", required=False, type=int)
parse.add_argument("-d", "--delay", help="Delay between each requests", required=False, type=int)
parse.add_argument("-t", "--threads", help="It uses katana, proxy and delay will be ignored", required=False, type=int)
args = parse.parse_args()

################################################################ Args

################################################################ Functions
def verify():
    use_proxy = True
    if not "NINJA" in args.url:
        print('\033[91m'+"[-] Please specify the parameter to fuzz with : NINJA !"+'\033[0m')
        print('\033[91m'+"[-] Exemple : -u https://github.com/NINJA"+'\033[0m')
        sys.exit()
    if args.proxies != None:
        compteur_erreur = 0
        proxy_list = args.proxies.split(",")
        max_error = len(proxy_list)
        for proxy_part in proxy_list:
            if not "http" in proxy_part:
                compteur_erreur += 1
            if compteur_erreur == max_error:
                use_proxy = False
        return use_proxy

def process_proxies(proxies):
    proxies_dico_return = {}
    proxies = proxies.split(',')
    if "http" in proxies[0]:
        proxies_dico_return["http"] = proxies[0]
        return proxies_dico_return

def fuzzer(wordlist):
    for i in wordlist:
        response = session.get(args.url.replace('NINJA',i),headers={'Cache-Control': 'no-cache',"Pragma": "no-cache"})
        if response.status_code == 200:
            print('\033[92m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
        elif response.status_code == 403:
            print('\033[93m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
        elif response.status_code == 401:
            print('\033[93m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}] --> Authentication Panel"+'\033[0m')

def fuzzer_delay(wordlist):
    for i in wordlist:
        time.sleep(args.delay)
        response = session.get(args.url.replace('NINJA',i),headers={'Cache-Control': 'no-cache',"Pragma": "no-cache"})
        if response.status_code == 200:
            print('\033[92m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
        elif response.status_code == 403:
            print('\033[93m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
        elif response.status_code == 401:
            print('\033[93m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}] --> Authentication Panel"+'\033[0m')

def fuzzer_pattern(wordlist):
    pattern = session.get(args.pattern,headers={'Cache-Control': 'no-cache',"Pragma": "no-cache"})
    for i in wordlist:
        response = session.get(args.url.replace('NINJA',i),headers={'Cache-Control': 'no-cache',"Pragma": "no-cache"})
        if response.status_code == 200:
            if response.text != pattern.text:
                print('\033[92m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
        elif response.status_code == 403:
            if response.text != pattern.text:
                print('\033[93m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
        elif response.status_code == 401:
            if response.text != pattern.text:
                print('\033[93m' + f"[NINJA] Response : {i} ({response.status_code})[Size : {len(response.content)}] --> Authentication Panel"+'\033[0m')

################################################################ Functions

################################################################ Multithread
################################################################ Multithread

################################################################ Data Processing

if args.threads != None:
    if args.threads > 100:
        print('\033[91m'+"[-] Too much threads, may be dangerous for your computer, abording"+'\033[0m')
        sys.exit()
    if args.threads > 32:
        validation = input('\033[91m'+"[-] That amount of thread may cause your screen to lag, continue ? Y/N :"+'\033[0m').upper()
        if validation == "N":
            sys.exit()

use_proxy = verify()

with open(args.wordlist, 'r') as wordlist:                     # Get Wordlist
    wordlist_data = wordlist.read()
    wordlist_data = wordlist_data.split('\n')


session = requests.Session()

if args.proxies != None and use_proxy == True:
    proxies_dico = process_proxies(args.proxies)                   # Get Proxies
    for key in proxies_dico:
        if "https" in proxies_dico[key]:
            print(f"[+] Using Proxy :https : {proxies_dico[key]}")
        else:
            print(f"[+] Using Proxy :{key} : {proxies_dico[key]}")
    session.proxies = proxies_dico
else:
    if use_proxy == False:
        print('\033[91m'+"[-] Invalid Proxy Format !"+'\033[0m')
    print('\033[94m'+"[*] Fuzzing without proxy !"+'\033[0m')


################################################################ Data processing

################################################################ Fuzzing

if args.threads != None:
    print(f"[+] Workers : {args.threads} workers")
print('\033[94m'+f"[*] Fuzzing URL : {args.url}\n"+'\033[0m')
if args.threads != None:
    if args.bytechange != None:
        os.system(f"Katana -w {args.wordlist} -u {args.url} -t {args.threads} --bytechange {args.bytechange}")
    else:
        os.system(f"Katana -w {args.wordlist} -u {args.url} -t {args.threads}")
elif args.pattern != None:
    print("[-] Delay set to 0, pattern option selected")
    fuzzer_pattern(wordlist_data)
elif args.delay == None:
    print(f"[+] Requests delay set to {args.delay} seconds")
    fuzzer(wordlist_data)

else:
    fuzzer_delay(wordlist_data)
################################################################ Fuzzing
