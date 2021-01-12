import random
import multiprocessing
import requests
import argparse
import random
import sys
import time

parse = argparse.ArgumentParser()
parse.add_argument("-w","--wordlist", help="To specify the wordlist", required=True)
parse.add_argument("-u", "--url", help="To specify the URL", required=True)
parse.add_argument("-t", "--threads", help="Number of workers (<64)", required=True, type=int)
parse.add_argument("-b", "--bytechange", help="Detect a byte change [initial size]", required=False, type=int)
args = parse.parse_args()

def chunks(myList, parts):
    return [myList[(i*len(myList))//parts:((i+1)*len(myList))//parts] for i in range(parts)]

def fuzzer(part,threads):
    with open(args.wordlist,"r") as file:
        global wordlist
        wordlist = file.read().split("\n")
    wordlists = chunks(wordlist,threads)
    session = requests.Session()
    try:
        for i in wordlists[int(part)]:
            response = session.get(args.url.replace('NINJA',i),headers={'Cache-Control': 'no-cache',"Pragma": "no-cache"})
            if response.status_code == 200:
                if args.bytechange != None:
                    if len(response.content) != args.bytechange:
                        print('\033[92m' + f"[KATANA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
                else:
                    print('\033[92m' + f"[KATANA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
            elif response.status_code == 403:
                if args.bytechange != None:
                    if len(response.content) != args.bytechange:
                        print('\033[93m' + f"[KATANA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
                else:
                    print('\033[93m' + f"[KATANA] Response : {i} ({response.status_code})[Size : {len(response.content)}]"+'\033[0m')
            elif response.status_code == 401:
                if args.bytechange != None:
                    if len(response.content) != args.bytechange:
                        print('\033[93m' + f"[KATANA] Response : {i} ({response.status_code})[Size : {len(response.content)}] --> Authentication Panel"+'\033[0m')
                else:
                    print('\033[93m' + f"[KATANA] Response : {i} ({response.status_code})[Size : {len(response.content)}] --> Authentication Panel"+'\033[0m')
    except KeyboardInterrupt:
        print("[-] Interrupted by User !")
class multi_fuzz():
    def __init__(self,threads):
        self.threads = threads
    def start(self):
        jobs = []
        for i in range(self.threads):
            process = multiprocessing.Process(target=fuzzer,args=(str(i),threads))
            jobs.append(process)
            process = None

        for j in jobs:
            try:
                j.start()
            except KeyboardInterrupt:
                print("[-] Interrupted by User !")

        for j in jobs:
            j.join()

if __name__ == "__main__":
    threads = args.threads
    if threads > 64:
        reponse = input(f"Are you sure you want to use {threads} process (May be Dangerous) Y/N ? :").upper()
        if reponse == 'N':
            sys.exit()
        elif reponse != 'Y':
            sys.exit()
        else:
            pass
    start = time.time()
    proc = multi_fuzz(threads)
    proc.start()
    stop = time.time()
    print(f"[+] Parsed wordlist in {stop-start} seconds")
