import re
import datetime

''' i) program for making dictionary of time for alexa top 500 urls.
    ii) identify first party and third party cookie
    iii) check when was that cookie called
    iv) Make a list of Alexa top 500 urls to check for 1st party cookie setting
    '''
def make_time_range(visit_time_f):
    ''' make a dictionary of 500 different alexa urls with respective begin and \n
    and end time'''
    browse_time = dict()

    for line in visit_time_f:
        list_time = line.split(',')
        url = list_time[0]
        time_begin = list_time[1]
        time_end = list_time[2]
        time_tuple = (time_begin, time_end)
        browse_time[url] = time_tuple
        #print("URL: %s Begin: %s End: %s" %(url, time_begin, time_end))

        
    '''checking if browse_time dictionary works
    for key, value in browse_time.items():
        print("%s : %s - %s"%(key, str(value[0]), str(value[1])))'''
    return browse_time




def make_alexa_list(alexa_f):
    '''make a list of alexa urls '''
    alexa_list = []
    for line in alexa_f:
        alexa_list.append(str(line.strip()))
    return alexa_list
     

def check_parties_cookies(alexa_list, cookies):
    '''i)check if a cookie is a first party or third party '''
    count_first_party_cookie = 0
    count_third_party_cookie = 0
    count_all_cookie = 0

    '''dictionary for first party cookie'''
    first_party_cookie_dict = dict()

    '''dictionary for third party cookie'''
    third_party_cookie_dict = dict()

    '''file to write tp and their time of setting cookie '''
    tp_cookie_time = open("..\\tp_cookie_time.txt", 'w')

    '''file to write fp and their time of setting cookie '''
    fp_cookie_time = open("..\\fp_cookie_time.txt", 'w')

    
    for cookie in cookies:
        count_all_cookie += 1
        cookie_list = cookie.split('=')
        domain = cookie_list[0]
        time_access = cookie_list[1]
        pattern = re.compile(r'^www$.')
        #print("Domain is %s" %domain)
        #print(bool(domain.strip() in alexa_list))
        #print(type(alexa_list))
        #for url in alexa_list:
        
        
        #print("Checking cookie type for url %s" %domain)
        '''removing www as alexa's url does not have www'''
        if (bool(re.search(pattern, domain))):
            print("original url: %s"%domain)
            domain_split = domain.split('www.')
            
            domain = domain_split[1]
            print("splitted url: %s"%domain)
           
        '''checking if a domain is first or third party and putting them in
            respective dict with their access time '''
        
        if(domain in alexa_list):
            if domain in first_party_cookie_dict:
                first_party_cookie_dict[domain] += 1
            else:
                first_party_cookie_dict[domain] = 1
                print("%s is a fp cookie" %(domain))
                fp_cookie_time.write("%s = %s" %(domain, time_access))
            count_first_party_cookie += 1
        else:
            if domain in third_party_cookie_dict:
                third_party_cookie_dict[domain] += 1
                print("%s is a tp cookie" %(domain))
                tp_cookie_time.write("%s = %s" %(domain, time_access))
                
            else:
                third_party_cookie_dict[domain] = 1
                print("%s is a tp cookie" %(domain))
                tp_cookie_time.write("%s = %s" %(domain, time_access))
            count_third_party_cookie += 1
    tp_cookie_time.close()
    fp_cookie_time.close()

                
    return (first_party_cookie_dict, third_party_cookie_dict, count_first_party_cookie, count_third_party_cookie, count_all_cookie)
def make_time_range(visit_time_f):
    ''' make a dictionary of 500 different alexa urls with respective begin and \n
    and end time'''
    browse_time = dict()

    for line in visit_time_f:
        list_time = line.split(',')
        url = list_time[0]
        time_begin = list_time[1]
        time_end = list_time[2]
        time_tuple = (time_begin, time_end)
        browse_time[url] = time_tuple
        #print("URL: %s Begin: %s End: %s" %(url, time_begin, time_end))

        
    '''checking if browse_time dictionary works
    for key, value in browse_time.items():
        print("%s : %s - %s"%(key, str(value[0]), str(value[1])))'''
    return browse_time

def fp_with_respective_tp_cookie(browse_dict, tp_time_f):
    ''' dictionary to keep main fp url and tp url called in its browse time'''
    fp_call_tp_dict = dict()
    
    for line in tp_time_f:
        url_time_list = line.split('=')
        tp_url = url_time_list[0]
        tp_time = datetime.datetime.strptime(url_time_list[1].strip(), '%Y-%m-%d %H:%M:%S')
        
        #print("%s = %s" %(tp_url, tp_time))
        ''' search at browse dictionary to find out during which main domain
            call was tp cookie set '''
        for key, value in browse_dict.items():
            print("Checking for tp_url %s" %(tp_url))
            #print("%s : %s" %(value[0], value[1]))
            begin_t = datetime.datetime.strptime(value[0].strip(), '%Y-%m-%d %H:%M:%S')
            end_t = datetime.datetime.strptime(value[1].strip(), '%Y-%m-%d %H:%M:%S')
            #print( bool(tp_time >= begin_t and tp_time < end_t))
            ''' check if last_accessed falls in range of a fp domain time range'''       

            if(bool(tp_time >= begin_t and tp_time < end_t)):
                if key in fp_call_tp_dict and (tp_url.strip() in fp_call_tp_dict[key]):
                    pass
                elif key not in fp_call_tp_dict:
                    fp_call_tp_dict[key] = [tp_url.strip()]
                else:
                    fp_call_tp_dict[key].append(tp_url.strip())
                '''once found its  fp domain it tp can break out of for loop'''
                break   
                
            
    return fp_call_tp_dict

def eval_count_tp_cookie(fp_tp_cookie):
    
    tp_cookie_count_dict = dict()
    for key, values in fp_tp_cookie.items():
        tp_cookie_count_dict[key] = len(values)
    return tp_cookie_count_dict
        
   



def eval_dist_tp_cookie(tp_cookie_count_dict, dist_tp_cookie_f):
    ''' testing third_party_cookie '''
    #print("Printing tp cookie dict")
    print("In eval_dist_tp_cookie func")
    for key, value in sorted(tp_cookie_count_dict.items(), key=lambda(k,v):(v,k), reverse=False):
        #print("%s:%s"%(key,value ))
        dist_tp_cookie_f.write("%s,%s"%(key, str(value))+"\n")
  
    
        
if __name__ == '__main__':
    
    '''make a list of alexa urls'''
    alexa_f = open("..\\alexa_top500_cookie.txt", 'r')#test_alexa_urls.txt", 'r')
    alexa_list = make_alexa_list(alexa_f)
    #for a_url in alexa_list:
        #print(a_url)
    alexa_f.close()
    
    print("Len of alexa list is %s" %str(len(alexa_list)))

    '''making a dictionary for url timerange'''
    visit_time_f = open("..\\visit_time.txt", 'r')
    browse_time_dict = make_time_range(visit_time_f)
    visit_time_f.close()
    print("Len of browse_time_dict: %s"%str(len(browse_time_dict.keys())))


    #for key, values in browse_time_dict.items():
        #print("Browse time for %s"%(key))
        #print("%s:%s"%(key,[val for val in values]))
        
    

    '''check if a cookie is first or third party'''
    cookies = open("..\\cookie_time.txt", 'r')
    fp_cookie_dict, tp_cookie_dict, count_fp_cookie, count_tp_cookie, count_all_cookie = check_parties_cookies(alexa_list, cookies)
    cookies.close()
    


    ''' find tp cookie for a respective urls in Alexa '''
    tp_cookie_time_f = open("..\\tp_cookie_time_opt.txt", 'r')
    
    fp_tp_dict = fp_with_respective_tp_cookie(browse_time_dict, tp_cookie_time_f)

    tp_cookie_time_f.close()

    ''' write fp_tp_dict to a txt file'''
    fp_tp_dict_f = open("..\\fp_tp_dict.txt", 'w')
    for key,values in fp_tp_dict.items():
        print("writing for %s"%key)
        fp_tp_dict_f.write("%s = %s"%(key, [val for val in values])+"\n")
    fp_tp_dict_f.close()
        


    #print("In step of printing fp_tp_dict")
    #for key, values in fp_tp_dict.items():
        #print("%s:%s"%(key, [val for val in values]))


    '''count number of values in an fp_tp_dict and put it in dict for graph'''
    tp_cookie_count_dict = eval_count_tp_cookie(fp_tp_dict)
    
    
        
    

    ''' sort fp_tp_dict and write to a csv file number of cookie called in
    alexa's top 500 websites '''
    dist_tp_cookie_f = open("..\\dist_tp_cookie.csv", 'w')
    eval_dist_tp_cookie(tp_cookie_count_dict, dist_tp_cookie_f)
    dist_tp_cookie_f.close()

    
    
    
    
    ''' testing first_party_cookie '''
    #print("Printing First Party Cookie")
    #for key, value in fp_cookie_dict.items():
        #print("%s : %s" %(key, str(value)))

    ''' testing third_party_cookie '''
    #print("Printing Third Party Cookie")
    #for key, value in tp_cookie_dict.items():
        #print("%s : %s" %(key, str(value)))


    print("Total First Party Cookie %s" %str(count_fp_cookie))
    print("Total Third Party Cookie %s" %str(count_tp_cookie))
    print("Count all Cookie %s" %str(count_all_cookie))


    
    
    
    
    
    
    
    
    
