import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 your_script.py <target> <wordlist>")
        sys.exit(1)

    target = sys.argv[1]
    wordlist_path = sys.argv[2]

    try:
        with open(wordlist_path, 'r') as wordlist_file:
            wordlist = wordlist_file.read().splitlines()
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_path}' not found.")
        sys.exit(1)

    for word in wordlist:
        url = f"http://{target}/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Found: {url}")

if __name__ == "__main__":
    main()
