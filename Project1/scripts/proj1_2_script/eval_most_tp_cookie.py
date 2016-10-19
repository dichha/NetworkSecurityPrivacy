import re

''' i) make a dictionary of fp_respec_tp_cookie_set from fp_tp_dict.txt file
    ii) iterate over each value of the key and see if it is present in rest of
    fp domain url
    iii) make another dictionary where num_tp_cookie_set domain will be a key and
    its number of presence in other fp domain will be value
    iv) sort this num_tp_cookie_set for most popular tp domain that sets
'''
def make_dict_fp_tp_cookie(fp_tp_cookie_f):
    '''dictionary to keep first-party and its resoective third-party cookie'''
    dict_fp_respec_tp_cookie = dict()
    
    for line in fp_tp_cookie_f:
        #print(line.strip())
        cookie_list = line.split('=')
        #print("First party domain: %s Its cookie: %s"%(cookie_list[0], cookie_list[1]))
        key = cookie_list[0].strip()
        dict_fp_respec_tp_cookie[key] = []
        ''' regex for putting clean values '''
        values = cookie_list[1].replace('[','').replace(']','').replace('""','').split(',')
        for val in values:
            #print(val.replace("'", '').strip())
            val = val.replace("'", '').strip()
            dict_fp_respec_tp_cookie[key].append(val)
    
    #for key, values in dict_fp_respec_tp_cookie.items():
        #print("%s:%s"%(key, [val for val in values]))
    return dict_fp_respec_tp_cookie

def count_tp_cookie_set(dict_fp_respec_tp_cookie):
    #print("Printing values...")
    values = dict_fp_respec_tp_cookie.values()
    dict_tp_num = dict()
    for vals in values:
        for val in vals:
            if val in dict_tp_num:
                dict_tp_num[val] += 1
            else:
                dict_tp_num[val] = 1
                
    #for key,value in dict_tp_num.items():
        #print("%s:%s"%(key, str(value)))
    return dict_tp_num
def sort_tp_cookie_num(dict_tp_num, sort_cookie_set_f):
    for tp_domain, num in sorted(dict_tp_num.items(), key=lambda(k,v):(v,k), reverse=True):
        sort_cookie_set_f.write("%s , %s"%(tp_domain, num)+"\n")



if __name__ == '__main__':

    '''making a dictionary to for fp_tp_cookie'''
    fp_respec_tp_cookie_set_f = open("..\\fp_tp_dict.txt")
    dict_fp_respec_tp_cookie = make_dict_fp_tp_cookie(fp_respec_tp_cookie_set_f)
    fp_respec_tp_cookie_set_f.close()

    '''count number of appearance of tp domain dict_fp_respec_tp_cookie
    has no duplicate values'''
    dict_tp_num = count_tp_cookie_set(dict_fp_respec_tp_cookie)
            

    ''' csv file to write tp cookie set domain and its presence in different
    alexa websites'''
    sort_cookie_set_f = open("..\\dist_tp_cookie_set_domain.csv", 'w')
    sort_tp_cookie_num(dict_tp_num, sort_cookie_set_f)
    sort_cookie_set_f.close()
       
   
