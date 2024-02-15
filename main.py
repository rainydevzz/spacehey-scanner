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
                    with open('cool.txt', 'a') as f:
                        f.write(f'https://spacehey.com{link} - {w}\n')
                    break
            print("keywords not found! next...")
        p += 1

get_links()
