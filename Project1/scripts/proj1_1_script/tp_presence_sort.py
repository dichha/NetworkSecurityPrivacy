import operator
''' program to make a dictionary of txt file with tp and their number of presence'''

def sort_tp_presence(tp_presence_f):
    
    
    
    tp_presence_dict = dict()
    for line in tp_presence_f:
        tp_list = line.split('=')
        tp_domain = tp_list[0].strip()
        tp_presence = tp_list[1].strip()
        #print("%s : %s" %(tp_domain, tp_presence))
        tp_presence_dict[tp_domain] = int(tp_presence)

    #for key, value in tp_presence_dict.items():
        #print("%s:%s"%(key,value))
    #print(tp_presence_dict)
    
        
    '''sort dictionary here'''
    for tp_domain, presence in sorted(tp_presence_dict.items(), key=lambda(k,v):(v,k), reverse=True):
        #print("%s, %s" %(tp_domain, presence))
        most_referred_tp.write("%s , %s"%(tp_domain, presence) +"\n")
    
        
    
    
        

    

if __name__ == '__main__':
    
    tp_presence_f = open("..\\tp_presence.txt",'r')
    '''csv file to write tp domain and its presence'''
    most_referred_tp = open("..//dist_referred_tp.csv", 'w')
    sort_tp_presence(tp_presence_f)
    most_referred_tp.close()
