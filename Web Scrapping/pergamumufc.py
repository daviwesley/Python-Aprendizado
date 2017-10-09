import requests

with requests.Session() as c:
  url = "https://pergamum.ufc.br/pergamum/biblioteca_s/php/login_usu.php"
  USUARIO = 381097
  SENHA = 947312
  c.get(url)
  login_data = dict()
