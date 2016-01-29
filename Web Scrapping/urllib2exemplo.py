#!/usr/bin/env python

import urllib2

webUrl=urllib2.urlopen("https://www.google.com.br") #abri a url
data=webUrl.read() #ler o codigo fonte

print data


