file = open('json_har_parse/har_json_d_google.txt', 'r')
file_w = open('json_har_parse/har_json_d_google_visit.txt', 'w')
#file = open('json_har_parse/test_google.txt', 'r')
for line in file:
    #print(line)
    url_status = line.split(': ')
    #print(url_status[1])
    check_url = url_status[1]
    #print(type(check_url))
    check_list = check_url.split(',')
    #print(check_list)
    #print(check_list[0])
    short_url = check_list[0]
    #print(short_url[2:-1])
    clean_short_url = short_url[2:-1]
    redirect_url = check_list[2]
    #print(redirect_url)
    
    if (redirect_url != '['']]'):
        clean_redirect_url = redirect_url[3:-4]
        if (clean_redirect_url != ''):
            #print("%s||%s"%(clean_short_url,clean_redirect_url))
            file_w.write("%s||%s"%(clean_short_url,clean_redirect_url)+'\n')
    

file_w.close()    
file.close()
