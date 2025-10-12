from bs4 import BeautifulSoup
import requests
import pandas as pd


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url=url, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

titles = soup.select("h3.c-title.a-font-basic")

titles = [title.get_text(strip=True) for title in titles]
titles = titles[2:]

df = pd.DataFrame({
    "Name of Song": titles
})

df.to_csv("songs.csv", index=True)