file = open('twitter_scan_h.txt', 'r')
count = 0
#dlist= []

d={}
for line in file:
    url  = line.strip()
    if url not in d.keys():
        d[url] = 1
        #dlist.append(d)
    else:
        d[url] = d[url]+1
print(d.values())

for key, val in d.items():
    if (val == 5): #r val == 6 or val == 8):
        print("%s : %s"%(key, val))



'''
count = 0
for line in file:
    url = line.strip()
    #print(url)
    if url == 'https://twitter.com/account/suspended':
        count+=1
print(count)
'''

        
file.close()
