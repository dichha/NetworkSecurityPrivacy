file = open('twitter_scan_d.txt', 'r')
url_list = []
for line in file:
    url = line.strip()
    if url not in url_list:
        url_list.append(url)
print(len(url_list))
file.close()
