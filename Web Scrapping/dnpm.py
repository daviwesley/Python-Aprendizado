from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import cv2
import os
import requests

url_base = "https://sistemas.dnpm.gov.br/SCM/Extra/site/admin/pesquisarProcessos.aspx"
erro = "o código digitado não confere com o código da imagem."

def processarImagem():
    """
    Aplica um tom de cinza na imagem e depois borra o fundo para facilitar
    na leitura das letras. Retorna uma string com o resultado da leitura do
    texto
    """
    image = cv2.imread("CaptchaImage.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text

url = r"asdfasd.html"
page = open(url, encoding="utf8")
soup = BeautifulSoup(page.read(), "html.parser")

table = soup.find('table', id="ctl00_conteudo_gridProcessos")
print(processarImagem())
linhas = table.find_all("tr")
#linhas[3].find_all("td")[2].get_text().split()[0]

for i in range(1,len(linhas)):
    #print("tamanho = {}".format(len(dados)))
    #print(len(linhas[i].find_all("td")))
    valor = linhas[i].find_all("td")[2]
    valorcampo = " ".join(valor.get_text().split())
    #print("valor campo = {}".format(valorcampo))
    if valorcampo == "Licenciamento":
        #print("if verdadeiro")
        texto = " ".join(linhas[i].get_text().split())
        with open("lista.txt", "a") as arquivo:
            arquivo.write(texto + "\n")
        #print(dados.get_text())
