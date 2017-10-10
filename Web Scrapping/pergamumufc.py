import requests
from bs4 import BeautifulSoup

with requests.Session() as c:
  url = "https://pergamum.ufc.br/pergamum/biblioteca_s/php/login_usu.php"
  USUARIO = 381097
  SENHA = 947312
  c.get(url)
  login_data = dict(flag='index.php', login=USUARIO,password=SENHA,button="Acessar",numero_mestre='',ifsp_categ='')
  c.post(url,data=login_data,headers={'Referer':'https://pergamum.ufc.br/pergamum/biblioteca_s/php/login_usu.php'})
  resposta = c.get('https://pergamum.ufc.br/pergamum/biblioteca_s/meu_pergamum/index.php?flag=index.php')

  soup = BeautifulSoup(resposta.content,"html.parser")
  print(soup.find(id="nome").get_text())
  dados = soup.find_all("a",{"class":"txt_azul"})

  #dados.find("div",{"class":"t1"}) titulos pendentes
  #dados.find_all("a",{"class":"txt_azul"}) livros
  count=0
  for conteudo in dados:
      print(conteudo.text.replace("\t",""))
      #print(soup.find("td",{"class":"txt_cinza_10"}))
