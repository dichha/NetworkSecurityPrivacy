#!/usr/bin/python
import re

alexa_f = open("../alexa_top500.txt", 'r')
fp_f = open("../urls.txt", 'r')

'''for first iteration needs this to prevent skipping'''

a_url = alexa_f.readline().strip()


for i in range(460):
    '''readline from alexa file and make a complete url'''
    full_a_url = re.compile(r'https?://www.'+ str(a_url)+(r'/$'))
    print("Full Alexa URL: %s " %full_a_url.pattern)

    '''open file to write for specific alexa file'''
    specific_f = open("%s.txt"%a_url, 'w')

    '''read from fp file'''
    fp_url = fp_f.readline().strip()

    ''' check if two urls are same and if same write to file'''        
    url_match = bool(full_a_url.match(fp_url))
    if(url_match):
        specific_f.write(fp_url+"\n")
    '''copy of a_url to write file'''

    a_url = alexa_f.readline().strip()
    
    ''' go to next alexa url and next fp url. if not same write to file until fp
        encounters matching url '''
     
    next_a_url = re.compile(r'https?://www.'+ str(a_url)+(r'/$'))

    print("Next Alexa URL: %s" %next_a_url.pattern)
    next_fp_url = fp_f.readline().strip()
    print("Next FP URL: %s" %next_fp_url)

    check_next_match = bool(next_a_url.match(next_fp_url))
    while(check_next_match == False):
        specific_f.write(next_fp_url +"\n")
        next_fp_url = fp_f.readline().strip()
        check_next_match = bool(next_a_url.match(next_fp_url))
        #print(bool(check_next_match))
        if(check_next_match == True):
            print("Matched 4th party URL: %s" %next_fp_url)
            print("Matched with Alexa URL: %s" %next_a_url.pattern)
        
    

    print("Check url: %s" %a_url)
    specific_f.close()
                                
            

fp_f.close()
alexa_f.close()

