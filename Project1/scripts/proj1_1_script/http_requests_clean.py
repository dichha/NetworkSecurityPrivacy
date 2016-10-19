#!/usr/bin/python
import re

urls_file = open("http_requests.txt", 'r')
#print(type(str(url_string)))

all_clean_urls = open("urls.txt", 'w')
urls_string = urls_file.read()
#print(url_strings)
#url_string = '["http://www.google.com/"]["https://www.google.com/?gws_rd=ssl"]["http://clients1.google.com/ocsp"]["https://www.google.com/images/nav_logo242.png"]["https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"]["https://www.google.com/images/branding/product/ico/googleg_lodp.ico"]["https://s.ytimg.com/yts/cssbin/www-core-vflNM1YVQ.css"]["https://s.ytimg.com/yts/cssbin/www-pageframe-vflYc4phB.css"]["https://s.ytimg.com/yts/cssbin/www-the-rest-vflDnl7Oj.css"]["https://s.ytimg.com/yts/cssbin/www-marketing-vflavtkOk.css"]["https://s.ytimg.com/yts/img/marketing/browsers/mr-meh-vflAEr4Cy.png"]["https://s.ytimg.com/yts/img/marketing/browsers/chrome-vflbrSn5t.png"]["https://s.ytimg.com/yts/img/marketing/browsers/firefox-vfleOda-S.png"]["https://s.ytimg.com/yts/img/marketing/browsers/ie8-vflwnFMag.png"]["https://s.ytimg.com/yts/jsbin/www-core-vflzVbasr/www-core.js"]["https://s.ytimg.com/yts/jsbin/spf-vflUtE3mW/spf.js"]["https://s.ytimg.com/yts/img/favicon-vflz7uhzw.ico"]["https://s.ytimg.com/yts/img/favicon-vflz7uhzw.ico"]'
#a = '["apple"]["ball"]'
#url = re.search(r"\[([^\"A-Za-z0-9_://$\"]+)\]", url_string)
#url = re.search(r"\[\"([a-z]+)\"\]",a)
#print(url.group(1))
for match in re.finditer("\[\"([a-zA-Z0-9:/%.!#$&-;=?-\[\]\(\)_]*)\"\]",urls_string, re.S):
#for match in re.finditer("\[\"([!#$&-;=?-[]_a-z~]|%[0-9a-fA-F]{2})+$/\"\]",urls_string, re.S):    
    #print(match.group(1))
    all_clean_urls.write(match.group(1)+"\n")
all_clean_urls.close()
urls_file.close()




#url_list = []
#for line in url_file:
    #print(type(line))

