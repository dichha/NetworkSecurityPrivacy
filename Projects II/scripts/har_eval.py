import re

file = open("json_har_parse/har_json_h_google.txt", 'r', encoding="utf-8")
count=0;
dict_status=dict()
dict_status['0'] = []
url_list=[]
for line in file:
    '''
    if(count>6):
        break
    else:
    '''
    #print(line)
    list_url = line.split()
    '''for success'''
    values = list_url[2]
    #print(values)
    #print(values[:-1])
    clean_val = values[:-1]
    
    if (int(clean_val)//100) == 0:
        #sprint(clean_val)
        short_url=(list_url[0])
        url = short_url[:-1]
        #print(url)
        if url not in url_list:
            url_list.append(url)
        
    #print(values)
    count+=1
for url in url_list:
    dict_status['0'].append(url)
    
for key, values in dict_status.items():
    print("%s:%s"%(key, [val for val in values]))
    print("Total count: %s"%str(len(url_list)))    
    
    
