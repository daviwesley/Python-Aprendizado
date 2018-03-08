from bs4 import BeautifulSoup
from argparse import ArgumentParser
import glob
__author__ = "Davi Wesley"
ap = ArgumentParser(prog="dnpmParser.py",epilog="""Exemplos de uso: python dpmnParser.py main.html,
                                                   python dnpmParser.py *.main.html,
                                                   python dnpmParser.py main.html -s Disponibilidade,
                                                   python dnpmParser.py main.html -s 'Atividade de Pesquisa'""")
ap.add_argument("pagina",
            help="arquivo da página html do site, para vários arquivos usar o sinal '*'", type=str,
            nargs=1)
ap.add_argument("-p", "--pesquisar",
            help="pesquisa a informação dada, use aspas simples quando tiver mais que uma palavra",
            type=str,default="Licenciamento")
ap.add_argument("-v", "--verbose",help="Explica o que tá acontecendo no momento",action="count")
args = ap.parse_args()

for fpath in glob.glob(args.pagina[0]):
    if args.verbose:
        print("Processando página {}".format(fpath))
    url = fpath
    page = open(url, encoding="utf8")
    soup = BeautifulSoup(page.read(), "html.parser")

    table = soup.find('table', id="ctl00_conteudo_gridProcessos")
    linhas = table.find_all("tr")

    for i in range(1,len(linhas)):
        valor = linhas[i].find_all("td")[2]
        valorcampo = " ".join(valor.get_text().split())
        if valorcampo == args.pesquisar:
            if args.verbose == 2:
                print("Página {}, palavra encontrada = {}".format(fpath, args.pesquisar))
            texto = " ".join(linhas[i].get_text().split())
            with open("lista.txt", "a", encoding="utf8") as arquivo:
                arquivo.write(texto + "\n")
