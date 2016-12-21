import json
import os

def eval_req(harfile_json):
    
    main_dictReq  = dict()
    main_key=""

    ''' get just the first json'''
    for key,val in harfile_json['log']['entries'][0].items():
        #print(key)
        #print(val)
        
        if key == "request":
            #print("In request dictionary")
            #print(type(val))
            req_dict = val
            #print("longURL %s" %req_dict['url'])
            req_headers = req_dict['headers']
            '''headers is a list'''
            #print(type(headers))
            referrer_dict = req_headers[5]
            ''' referrer is a dictionary '''
            #print(type(referrer))
            for key, val in referrer_dict.items():
                #print("%s %s" %(key,val))
                if(key == 'value'):
                    dict_key = val
                    main_key = dict_key
                    #print(dict_key)
                    main_dictReq[dict_key]=[]
                    #print(val)
                    long_url = req_dict['url']
                    main_dictReq[val].append(long_url)
    
    return (main_dictReq,main_key)

    

def eval_res(main_dictReq, main_key, harfile_json):
    main_dictRes = main_dictReq
    '''list required for putting chains of redirect if present'''
    redi_url_list = []
    ''' get just the first json'''
    for key,val in harfile_json['log']['entries'][0].items():
        if key == "response":
            #print("In response")
            res_dict = val
            #print(type(res_dict))
            status_check = res_dict['status']
            main_dictRes[main_key].append(status_check)
            #print(status_check)
            
            redirectURL = res_dict['redirectURL']
            redi_url_list.append(redirectURL)
            #print("redirectURL %s" %redirectURL)
            main_dictRes[main_key].append(redi_url_list)
        
        
    return main_dictRes

if __name__ == '__main__':
    file_num=0
    json_par = open('json_har_parse/har_json_d_google.txt','w')
    #json_10_par = open('json_har_parse/json_10_test2.txt','w')

    dir_path = 'HarFiles/hillary/google'
    for har_files in os.listdir(dir_path):
        harfile = open(os.path.join(dir_path, har_files),'r',encoding='utf-8')
        file_num += 1
        harfile_json = json.loads(harfile.read())
        main_dictReq, main_key = eval_req(harfile_json)
        #print("Main key: %s" %main_key)
        main_dict = eval_res(main_dictReq, main_key, harfile_json)
        '''iterate over dictionary and write to file'''
        for key, values in main_dict.items():
            #print("%s: %s"%(key, [val for val in values]))
            json_par.write("%s: %s"%(key, [val for val in values])+"\n")
    print("Number of har files read %s"%str(file_num))
    json_par.close()
    harfile.close()
        

'''    
    json_10_par = open('json_har_parse/har_json_donald.txt', 'w')
    for i in range(1,11):
        dir_path = "HarFiles/donald/d"+str(i)
        #dir_path="HarFiles/test2/"
        for har_files in os.listdir(dir_path):
            harfile = open(os.path.join(dir_path, har_files),'r',encoding='utf-8')
            file_num+=1
            print("File name: %s"%(har_files))
            #harfiles = open('HarFiles/Archive.har','r', encoding='utf-8')
            #for file in harfiles:
                #print(file)       
            harfile_json = json.loads(harfile.read())
            main_dictReq, main_key = eval_req(harfile_json)
            #print("Main key: %s" %main_key)
            main_dict = eval_res(main_dictReq, main_key, harfile_json)

            
            #iterate over dictionary and write to file
            for key, values in main_dict.items():
                #print("%s: %s"%(key, [val for val in values]))
                json_10_par.write("%s: %s"%(key, [val for val in values])+"\n")
        print("Number of har files read %s"%str(file_num))
    json_10_par.close()
    harfile.close()
'''


