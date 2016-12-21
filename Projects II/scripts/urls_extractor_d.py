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
'''
file = open('../test_extractor_d.txt', 'r')
twitter_urls = open('twitter_urls_d.txt','w')
adfly_urls = open('adfly_urls_d.txt','w')
bitly_urls = open('bitly_urls_d.txt','w')
'''
google_urls = open('google_urls_d.txt','w')
#string_url = "https:\/\/t.co\/E5FlddUsRm"
#pattern = r'https:\\/\\/t.co\\/\w{10}'
#match = re.search(pattern, string_url)
#print(match)

'''
for match in re.finditer(r'https:\\/\\/t\.co\\/\w{10}',content, re.S):
    print(match.group(1))
'''

twitter_short_urls = []
adfly_short_urls = []
bitly_short_urls = []
google_short_urls = []
'''
regex = re.compile(r'https:\\/\\/t\.co\\/\w{10}')
regex_a = re.compile(r'http:\\/\\/adf\.ly\\/\?id=\d{7}')
regex_b = re.compile(r'http:\\/\\/bit\.ly\\/\w{7}')
'''
regex_g = re.compile(r'http:\\/\\/goo\.gl\\/\w{5}')
#with open('../test_extractor.txt') as infile:
count=0
with open('../donaldtrump_1478304000/donaldtrump_1478304000.txt') as infile:
    for line in infile:
        #urls = regex.findall(line)
        #print(urls)
        count+=1
        print(count)
        '''
        for url in urls:
            if url not in twitter_short_urls:
                twitter_short_urls.append(url)
        urls_a = regex_a.findall(line)
        for url in urls_a:
            if url not in adfly_short_urls:
                adfly_short_urls.append(url)
                #print("A: %s"%url)
        urls_b = regex_b.findall(line)
        for url in urls_b:
            if url not in bitly_short_urls:
                bitly_short_urls.append(url)
                #print("B: %s"%url)
        '''
        urls_g = regex_g.findall(line)
        for url in urls_g:
            if url not in google_short_urls:
                google_short_urls.append(url)
                #print("G: %s"%url)
        
   
'''
regex_t = re.compile(r'https:\\/\\/t\.co\\/\w{10}')
regex_a = re.compile(r'http:\\/\\/adf\.ly\\/\?id=\d{7}')
regex_b = re.compile(r'http:\\/\\/bit\.ly\\/\w{7}')
regex_g = re.compile(r'http:\\/\\/goo\.gl\\/\w{5}')

for line in file:
    urls_t = regex_t.findall(line)
    for url in urls_t:
        if url not in twitter_short_urls:
            twitter_short_urls.append(url)
            print("T: %s" %url)
    urls_a = regex_a.findall(line)
    for url in urls_a:
        if url not in adfly_short_urls:
            adfly_short_urls.append(url)
            print("A: %s"%url)
    urls_b = regex_b.findall(line)
    for url in urls_b:
        if url not in bitly_short_urls:
            bitly_short_urls.append(url)
            print("B: %s"%url)
    urls_g = regex_g.findall(line)
    for url in urls_g:
        if url not in bitly_short_urls:
            google_short_urls.append(url)
            print("G: %s"%url)
'''  
'''
for url in twitter_short_urls:
    twitter_urls.write(url+'\n')
for url in adfly_short_urls:
    adfly_urls.write(url+'\n')
for url in bitly_short_urls:
    bitly_urls.write(url+'\n')
'''
for url in google_short_urls:
    google_urls.write(url+'\n')

'''
twitter_urls.close()
adfly_urls.close()
bitly_urls.close()
'''
google_urls.close()
            
#file.close()







