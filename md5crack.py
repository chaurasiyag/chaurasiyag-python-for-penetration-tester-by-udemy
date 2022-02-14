import hashlib
import sys
import argparse

parser = argparse.ArgumentParser(description="MD% Cracker")
parser.add_argument("-md5", dest="hash", help="md5 hash", required=True)
parser.add_argument("-w", dest="wordlist", help="wordlist", required=True)

parsed_args=parser.parse_args()

def main():
    hash_cracked=""
    with open(parsed_args.wordlist) as file:
        for line in file:
            line=line.strip()
            if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest()==parsed_args.hash:
                hash_cracked=line
                print("Hash is cracked succesfully : ",line)
                break
    if hash_cracked=="":
        print("\n Failed to crack the hash ,Try using more word to wordlists")

if __name__=="__main__":
    main()
                
     