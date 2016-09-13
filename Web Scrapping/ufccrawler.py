import requests
from bs4 import BeautifulSoup

url = "http://www.campusrussas.ufc.br/corpo-docente.php"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("div", {"class": "col-md-9"})

for nomes in data:
    try:
        fo = open("corpodocente.txt", "a+")
        fo.write(nomes.text);
        fo.close()
    except:
        pass
        
