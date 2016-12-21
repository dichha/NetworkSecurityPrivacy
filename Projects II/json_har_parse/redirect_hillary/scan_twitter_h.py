file = open('google_redirect_hillary.txt', 'r')
file_w = open('google_scan_h.txt', 'w')
for line in file:
    line_list = line.split('||')
    print(line_list[1])
    url = line_list[1].strip()
    file_w.write(url+'\n')
    #clean_url = url[2:-4]
    #print(clean_url)
    #file_w.write(clean_url+'\n')
file_w.close()
file.close()
