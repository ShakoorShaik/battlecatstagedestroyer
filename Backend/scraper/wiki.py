import requests
from bs4 import BeautifulSoup
import json

def scrape_cat_data():
    url = "https://battle-cats.fandom.com/wiki/Cat_Units"  # example page
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    cats = []

    for row in soup.select("table.wikitable tr")[1:]:
        cells = row.find_all("td")
        if len(cells) > 4:
            cat = {
                "name": cells[0].text.strip(),
                "type": cells[1].text.strip(),
                "cost": cells[2].text.strip(),
                "attack": cells[3].text.strip(),
                "trait": cells[4].text.strip()
            }
            cats.append(cat)

    with open("../data/raw_data.json", "w") as f:
        json.dump(cats, f, indent=2)

if __name__ == "__main__":
    scrape_cat_data()
