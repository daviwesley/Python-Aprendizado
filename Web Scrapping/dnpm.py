from bs4 import BeautifulSoup
import sys

#url = r"main.html"


for n in sys.argv[1:]:
    page = open(n, encoding="utf8")
    print(n)
    soup = BeautifulSoup(page.read(), "html.parser")
    table = soup.find('table', id="ctl00_conteudo_gridProcessos")

    linhas = table.find_all("tr")
    for dados in linhas:
        print("passando aqui")
        try:
            if dados.get_text().split()[6] == "Licenciamento":
                texto = " ".join(dados.get_text().split())
                with open("lista.txt", "a") as arquivo:
                    arquivo.write(texto + "\n")
        except Exception:
            pass
        #print(dados.get_text())
