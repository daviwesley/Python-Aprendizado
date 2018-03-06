import requests
from bs4 import BeautifulSoup

with requests.Session() as c:
  url = "https://pergamum.ufc.br/pergamum/biblioteca_s/php/login_usu.php"
  USUARIO = input("Digite a Matricula")
  SENHA = input("Digite a senha")
  c.get(url)
  login_data = dict(flag='index.php', login=USUARIO,password=SENHA,button="Acessar",numero_mestre='',ifsp_categ='')
  c.post(url,data=login_data,headers={'Referer':'https://pergamum.ufc.br/pergamum/biblioteca_s/php/login_usu.php'})
  resposta = c.get('https://pergamum.ufc.br/pergamum/biblioteca_s/meu_pergamum/index.php?flag=index.php')

  soup = BeautifulSoup(resposta.content,"html.parser")
  print(" ".join(soup.find(id="nome").get_text().split()))
  livros = soup.find_all("a",{"class":"txt_azul"})
  datas = soup.find_all('td',class_='txt_cinza_10')
  multas = soup.find_all('td',class_='txt_magenta')
  #dados.find("div",{"class":"t1"}) titulos pendentes
  #dados.find_all("a",{"class":"txt_azul"}) livros
  count=3
  aux=0
  for conteudo in livros:
      print(conteudo.text.replace("\t",""))
      print("Data de Devolucao:"+" ".join(datas[count].get_text().split()))
      print("Valor da multa: "+" ".join(multas[aux].get_text().split()))
      count=count+3
      aux=aux+1
      #print(soup.find("td",{"class":"txt_cinza_10"}))
