file = open('twitter_scan_d.txt', 'r')
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
#print(d.values())

for key, val in d.items():
    if (val ==  6):#8 or val == 4 or val == 6):
        print("%s : %s"%(key, val))


        
'''
for line in file:
    url = line.strip()
    if url == 'https://twitter.com/account/suspended':
        count+=1
print(count)
'''
        
file.close()
