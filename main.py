import bs4
import requests
import time
import dotenv
import os
import pick

if not os.path.isfile('cool.txt'):
    with open('cool.txt', 'w'):
        pass

def interface():
    print("Welcome to Spacehey Scanner!!")
    time.sleep(2)
    options = ["edit .env", "run scanner", "exit"]
    _, i = pick.pick(options, indicator=">")

    if i == 0:
        input_words = input("type your key words and phrases here, seperating them with a comma then a space. (i.e: music, fighting games, friends)\n")
        with open('.env', 'w') as f:
            f.write(f"WORDS=\"{input_words}\"")
            f.close()
            print("file written successfully")
            time.sleep(1)
            interface()
    
    if i == 1:
        print("scanner will begin now, use Ctrl+C to exit.")
        get_links()

    if i == 2:
        exit(0)

dotenv.load_dotenv()

words = os.environ["WORDS"].split(", ")

def get_links():
    # set the loop and initialize basic setup
    while True:
        p = 1
        links = []
        r = requests.get(f'https://spacehey.com/browse?page={p}')
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        results = soup.find("div", class_="inner").find_all("a")

        # checks for all profile links from the extracted page
        for res in results:
            if "profile?id" in res["href"]:
                links.append(res["href"])

        # checks for keywords on each page, and if present, writes the profile link to a file
        for link in links:
            time.sleep(5)
            r = requests.get(f'https://spacehey.com{link}').text
            for w in words:
                found = r.lower().find(w)
                if found != -1:
                    print(link)
                    print(w)
                    with open('cool.txt', 'r') as f:
                        if link in f.read():
                            break
                    with open('cool.txt', 'a') as f:
                        f.write(f'https://spacehey.com{link} - {w}\n')
                    break
            print("keywords not found! next...")
        p += 1

interface()
