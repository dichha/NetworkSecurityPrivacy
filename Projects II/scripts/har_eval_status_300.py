import re

file = open("json_har_parse/har_json_d_bitly.txt", 'r', encoding="utf-8")
redirect_file = open("json_har_parse/bitly_redirect_donald.txt", 'w')
count=0;
dict_status=dict()
dict_status['300'] = []
url_list=[]
redirect_dict = {}
empty_redirect = 0
redirect_num = 0
for line in file:
    '''
    if(count>100):
        break
    else:
    '''
        
    #print(line)
    list_url = line.split()
    '''for redirect'''
    status_val = list_url[2]
    #print(values[:-1])
    clean_val = status_val[:-1]
    if (int(clean_val)//100) == 3:
        #sprint(clean_val)
        short_url=(list_url[0])
        url = short_url[:-1]
        #print(url)
        '''for count'''
        if url not in url_list:
            url_list.append(url)

        '''for redirect url'''
        redirect_urls = list_url[3]
        redirect = redirect_urls[2:-2]
        #print("redirect: %s"%(redirect[2:-2]))
        #print("Original url:%s Redirect url:%s"%(url, redirect))
        if redirect not in redirect_dict.values() and redirect != "'":
            redirect_dict[url]=[]
            redirect_dict[url].append(redirect)
            redirect_num += 1
        elif redirect != "'" and redirect in redirect_dict[url]:
            redirect_dict[url].append(redirect)
            redirect_num += 1
        else:
            print("empty redirect")
            empty_redirect += 1
        
        #print(values)
        #count+=1
for url in url_list:
    dict_status['300'].append(url)
    
for key, values in dict_status.items():
    print("%s:%s"%(key, [val for val in values]))
    print("Total unique redirect count: %s"%str(len(url_list)))

#print(redirect_dict)   
for key, values in redirect_dict.items():
    #print(key, values)
    redirect_file.write("%s|%s"%(key,values)+"\n") 

print("Empty redirect: %s redirect %s"%(empty_redirect, redirect_num))

redirect_file.close()
file.close()
    
