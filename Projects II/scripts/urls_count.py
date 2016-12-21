urls = open("urls_d_h/donald/google_urls_d.txt", 'r', encoding='utf-8')
#urls = open('urls_d_h/hillary/google_urls_h.txt', 'r', encoding='utf-8')
count=0
for url in urls:
    count+=1
print("Total urls: %s"%str(count))

              
