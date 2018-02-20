from bs4 import BeautifulSoup
import re


url = r"main.html"
page = open(url, encoding="utf8")
soup = BeautifulSoup(page.read(), "html.parser")

data = []
table = soup.find('table', id="ctl00_conteudo_gridProcessos")

linhas = table.find_all("tr")

for dados in linhas:
    if dados.get_text().split()[6] == "Licenciamento":
        texto = " ".join(dados.get_text().split())
        with open("lista.txt", "a") as arquivo:
            arquivo.write(texto + "\n")
        #print(dados.get_text())
