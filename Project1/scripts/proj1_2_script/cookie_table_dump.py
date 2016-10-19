#!/usr/bin/python

import sqlite3
import json
import datetime


conn = sqlite3.connect('C:\\Users\\Dichha Chamling\\Documents\\fourthparty_cookies_eval.sqlite')
#print("Opened database successfully")
cookie_time_f = open("../cookie_time.txt", 'w')

cursors = conn.execute("SELECT raw_host, last_accessed from cookies")
for cur in cursors:
    raw_host = cur[0]
    last_accessed = cur[1]
    
    #print(last_accessed)
    '''converting to human readable form'''
    
    to_sec = datetime.datetime.fromtimestamp(float(last_accessed)/1000000.)
    #print(to_sec)
    human_readable = to_sec.strftime('%Y-%m-%d %H:%M:%S')
    #print(human_readable)
    print("Writing for %s"%raw_host)
    cookie_time_f.write("%s=%s"%(raw_host, str(human_readable))+"\n")
    
    
    
cookie_time_f.close()
conn.close()
