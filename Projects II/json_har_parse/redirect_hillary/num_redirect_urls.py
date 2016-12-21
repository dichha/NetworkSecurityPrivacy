file = open('twitter_scan_h.txt', 'r')
url_list = []
for line in file:
    url = line.strip()
    if url not in url_list:
        url_list.append(url)
print(len(url_list))
file.close()

    
