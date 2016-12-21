file = open('redirect_donald.txt', 'r')
file_w = open('twitter_scan_d.txt', 'w')
for line in file:
    line_list = line.split('|')
    #print(line_list[1])
    url = line_list[1].strip()
    #file_w.write(url+'\n')
    clean_url = url[2:-3]
    #print(clean_url)
    file_w.write(clean_url+'\n')
file_w.close()
file.close()
