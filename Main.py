import requests
from bs4 import BeautifulSoup

url = "https://toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,"html.parser")

    titulos = soup.find_all('h1')

    for titulo in titulos:
        print(titulo.text.strip())
else:
    print("Falha ao acessar o site.")
