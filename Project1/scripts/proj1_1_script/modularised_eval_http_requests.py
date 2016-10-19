
import re
from urlparse import urlparse


def dist_tp_http_req(alexa_urls, eval_f):
    '''Keepng track of total number of fp and tp http requests'''
    total_fp_count = 0
    total_tp_count = 0
    
    '''website and number of tp http requests'''
    count_tp_dict = dict()
    
    '''dictionary to keep track of tp requests in all alexa's websites'''
    tp_popularity_dict = dict()

    ''' dictionary for keeping track of alexa_url and tp url called on its visit'''
    fp_res_tp_http_req = dict()
    
    
    for a_url in alexa_urls:
        #print("Evaluating for file %s"%a_url.strip())
        fp_count = 0
        tp_count = 0

        '''opening an individualt txt file to evaluate'''
        content_urls = open("../individual_site_url/%s.txt" %a_url.strip(), 'r')

        '''making a full url of alexa_website so that we can check with urls in txt file'''
        full_a_url = re.compile(r'https?://www.'+str(a_url.strip())+(r'/'))


        ''' keeps track of all 3rd http requests made in a domain '''
        third_party_dict = dict()
        
        for c_url in content_urls:
            match = bool(re.search(full_a_url,c_url))
            #print("Content URL: %s" %str(c_url))
            #print("Check Match: %s"% str(match))
            if(match):
                '''count number of fp requests'''
                fp_count += 1
                total_fp_count += 1
                #print("Matching URL: %s" %c_url)
                #print(first_party
            else:
                '''domain name will be used as a key to keep track of their appearance '''
                parsed_uri = urlparse(c_url.strip())
                domain = '{uri.netloc}'.format(uri=parsed_uri)
                #print(third_party_dict[domain]

                ''' for individual site's numner of tp request '''
                if domain in third_party_dict:
                    third_party_dict[domain] += 1
                else:
                    third_party_dict[domain] = 1

                ''' for overall popularity of third party url '''
                if domain in tp_popularity_dict:
                    tp_popularity_dict[domain] += 1
                else:
                    tp_popularity_dict[domain] = 1

                '''count number of tp requests'''
                tp_count += 1
                total_tp_count += 1

        '''a dictionary for keeping total number to tp call in a alexa url'''
        count_tp_dict[a_url.strip()] = tp_count
                

        eval_f.write("Domain: %s Total first-party: %s Total third-party: %s" %(a_url.strip(),str(fp_count),str(tp_count)+"\n"))           
        
        '''writing count of respective tp url calls of a url in alexa'''
        for key, value in third_party_dict.items():
            #print("%s : %s" %(key, str(value)))
            eval_f.write("%s : %s" %(key, str(value))+"\n")

        ''' closing respective alexa's url txt file'''
        content_urls.close()
                          
    return count_tp_dict, total_fp_count, total_tp_count
       
def data_for_tp_graph(count_tp_dict):
    ''' write to a csv file to make a graph '''
    dist_tp = open("..\\dist_tp_requests.csv", 'w')
    
    for fp_domain, tp_requests in sorted(count_tp_dict.iteritems(), key=lambda(k,v):(v,k)):
        #print("%s: %s" %(fp_domain, tp_requests))
        dist_tp.write("%s , %s" %(fp_domain, tp_requests)+"\n")
    dist_tp.close()
            

            

def make_tp_domain_list(tp_domain_f):
    ''' write file to list all tp domain'''
    tp_domain_file = open("..\\unique_tp_domain.txt", 'w')
    
    tp_domain_list = []
    for line in tp_domain_f:
        domain_list = line.split(',')
        domain = domain_list[0].strip()
        #print(domain)
        tp_domain_list.append(domain)
        tp_domain_file.write(domain + "\n")
        
    #for domain in tp_domain_list:
        #print(domain)
    tp_domain_file.close()
    return tp_domain_list


def make_dict_fp_values(alexa_urls):

    '''dictionary storing values of unique tp call in fp'''
    fp_values_dict = dict()
    '''list for storing unique tp domain'''
    tp_list = []

    ''' write file to list all tp domain'''
    tp_domain_file = open("..\\unique_tp_domain.txt", 'w')

    for a_url in alexa_urls:
        a_url = a_url.strip()
        print("Evaluating for file %s" %a_url)

        '''opening an individual txt file to evaluate'''
        content_urls = open("..\\individual_site_url\\%s.txt" %a_url, 'r')
        
        '''making a full url of alexa_website so that we can check with urls in txt file'''
        full_a_url = re.compile(r'https?://www.'+str(a_url.strip())+(r'/'))

        for c_url in content_urls:
            match = bool(re.search(full_a_url,c_url))   
            if (match):
                #pass
                #print("Alexa url %s" %a_url)
                #print("Content url %s" %c_url.strip())
                if a_url in fp_values_dict.keys():
                    pass
                else:
                    fp_values_dict[a_url] = []
            else:
                #print("Match %s" %(str(match)))
                '''domain name will be used as a value to keep track of their
                appearance in fp domain'''
                parsed_uri = urlparse(c_url.strip())
                tp_domain = '{uri.netloc}'.format(uri=parsed_uri)
                #print(tp_domain)

                ''' check if tp domain is present in fp dictinory
                    if present ignore the tp domain else add. If a_url key
                    is not present then make one'''
                if a_url in fp_values_dict and (tp_domain in fp_values_dict[a_url]):
                    pass
                elif a_url not in fp_values_dict:
                    fp_values_dict[a_url] = [tp_domain]
                    if(tp_domain not in tp_list):
                        tp_list.append(tp_domain)
                    
                        tp_domain_file.write(tp_domain + '\n')
                else:
                    fp_values_dict[a_url].append(tp_domain)
                    if(tp_domain not in tp_list):
                        tp_list.append(tp_domain)
                        print("%s calls %s" %(a_url, tp_domain))
                        tp_domain_file.write(tp_domain + '\n')
                        tp_list.append(tp_domain)
                    
    '''checking if dictionary have correct values '''
    fp_values = open("..\\fp_values.txt", 'w')
    for key, values in fp_values_dict.items():
        fp_values.write("%s:%s"%(key, [val for val in values])+"\n")
        #print("%s:%s"%(key, [val for val in values]))
    fp_values.close()
    tp_domain_file.close()
    return fp_values_dict, tp_list
                    


def eval_popular_tp_domain(tp_domain_list, fp_values_dict):
    ''' i) make a list of third party domain
        ii) make a tp dict where keys are tp domain and value its presence in
        different fp '''
    ''' write to presence tp a file '''
    tp_presence_file = open("..\\tp_presence.txt", 'w')
    
    
    
    tp_presence_dict = dict()
    for tp_domain in tp_domain_list:
        tp_domain = tp_domain.strip()
        #print(tp_domain)
        
        '''iterating over all fp values to measure tp presence'''
        for key,values in fp_values_dict.items():
            #print("what's up")
            #print("%s:%s"%(key,str([val for val in values])))
            #print("Checking presence of %s in %s" %(tp_domain, [val for val in values]))
            '''checking presence of tp in values list'''
            print("Checking presence of %s in %s fp" %(tp_domain,key))
            
            presence = bool(tp_domain in [val for val in values])
            if(presence):
                if tp_domain in tp_presence_dict.keys():
                    tp_presence_dict[tp_domain] += 1
                else:
                    tp_presence_dict[tp_domain] = 1
        tp_presence_file.write("%s = %s"%(tp_domain, str(tp_presence_dict[tp_domain])+"\n"))

                    
    #for key, val in tp_presence_dict.items(): 
        #print("%s:%s"%(key, str(val)))
    tp_presence_file.close()
    return tp_presence_dict

def order_tp_presence(tp_presence_dict):
    ''' write to a csv file to make a graph '''
    tp_pre = open("..\\tp_presence.txt", 'w')
    
    for tp_domain, presence in sorted(tp_presence_dict.iteritems(), key=lambda (k,v):(v,k)):
        #print("%s: %s" %(fp_domain, tp_requests))
        tp_pre.write("%s , %s" %(tp_domain, presence)+"\n")
    tp_pre.close()
    



if __name__ == '__main__':
    alexa_urls = open("..\\alexa_top500_http.txt", 'r')
    eval_f = open("..\\request_eval.txt", 'w')

    count_tp_dict, total_fp_count, total_tp_count = dist_tp_http_req(alexa_urls, eval_f)
    print("Total First Party HTTP request %s" %(total_fp_count))
    print("Total Third Party HTTP request %s" %(total_tp_count))
    alexa_urls.close()
    eval_f.close()    

    
    '''csv file for graph of distribution of tp http request'''
    data_for_tp_graph(count_tp_dict)    
    
    ''' make a dictionary of fp values of tp call  and all unique tp domain'''
    alexa_urls = open("..\\alexa_top500_http.txt", 'r')
    fp_values_dict, tp_list = make_dict_fp_values(alexa_urls)
    alexa_urls.close()
    tp_domain_list = open("..\\unique_tp_domain.txt")
    
    ''' evaluating popular tp domain'''
    tp_presence_dict = eval_popular_tp_domain(tp_domain_list, fp_values_dict)


    #for domain in tp_domain_list:
        #print(domain)
    #tp_domain_list.close()

    ''' order tp_presence_dict in descending order'''
    order_tp_presence(tp_presence_dict)
    
    
    
    
        




    
