from zipfile import ZipFile
import re
import json
'''
zip_f = ZipFile('..\\hillaryclinton_1478304000.zip')
for info in zip_f.infolist():
    print(info.filename)
'''

'''with ZipFile('..\\hillaryclinton_1478304000.zip','r') as myzip:
    with myzip.open('hillaryclinton_1478304000.txt','r') as myfile:
        print(myfile.read())'''
'''
file = open('','r')
content = file.read()
'''
#file = open('../test_extractor_h.txt', 'r')
twitter_urls = open('twitter_urls.txt','w')
#string_url = "https:\/\/t.co\/E5FlddUsRm"
#pattern = r'https:\\/\\/t.co\\/\w{10}'
#match = re.search(pattern, string_url)
#print(match)

'''
for match in re.finditer(r'https:\\/\\/t\.co\\/\w{10}',content, re.S):
    print(match.group(1))
'''
twitter_short_urls = []
regex = re.compile(r'https:\\/\\/t\.co\\/\w{10}')
#with open('../test_extractor.txt') as infile:
count=0
with open('../hillaryclinton_1478304000/hillaryclinton_1478304000.txt') as infile:
    for line in infile:
        urls = regex.findall(line)
        #print(urls)
        count+=1
        print(count)
        for url in urls:
            if url not in twitter_short_urls:
                twitter_short_urls.append(url)
        
    
'''
regex = re.compile(r'https:\\/\\/t\.co\\/\w{10}')
twitter_short_urls = []
for line in file:
    urls = regex.findall(line)
    for url in urls:
        if url not in twitter_short_urls:
            twitter_short_urls.append(url)
'''
for url in twitter_short_urls:
    twitter_urls.write(url+'\n')


twitter_urls.close()
            
#file.close()







