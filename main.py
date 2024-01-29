import bs4
import requests
import time
import dotenv
import os

dotenv.load_dotenv()

words = os.environ["WORDS"].split(", ")

def get_links():
    # set the loop and initialize basic setup
    while True:
        p = 1
        links = []
        r = requests.get(f'https://spacehey.com/browse?page={p}')
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        res = soup.find("div", class_="inner").find_all("a")

        # checks for all profile links from the extracted page
        for i in res:
            if "profile?id" in i["href"]:
                links.append(i["href"])

        # checks for keywords on each page, and if present, writes the profile link to a file
        for i in links:
            time.sleep(5)
            r = requests.get(f'https://spacehey.com{i}').text
            for w in words:
                a = r.lower().find(w)
                if a != -1:
                    print(i)
                    with open('cool.txt', 'a') as f:
                        f.write(f'https://spacehey.com{i}\n')
                    break
            print("keywords not found! next...")
        p += 1

get_links()
