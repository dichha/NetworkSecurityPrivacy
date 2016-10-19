#!/usr/bin/python

alexa_f = open('C:\\Users\\Dichha Chamling\\Documents\\top-1m.csv\\top-1m.csv', 'r')
alexa_top500 = open("alexa_top500.txt", 'w')
for i in range(500):
    line = alexa_f.readline()
    url_list = [url.strip() for url in line.split(',')]
    #print(str(url_list))
    alexa_top500.write(str(url_list[1])+"\n")
alexa_top500.close()
alexa_f.close()
    
