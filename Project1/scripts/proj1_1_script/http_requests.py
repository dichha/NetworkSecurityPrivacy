#!/usr/bin/python
import sqlite3
import json

conn = sqlite3.connect('C:\\Users\\Dichha Chamling\\Documents\\fourthparty_main_v30.sqlite')
print("Opened database successfully")
cursor = conn.execute("SELECT url FROM http_requests")
write_f = open("http_requests.txt", 'w')
for row in cursor:
    write_f.write(json.dumps(row))
    #print(type(row))

        
write_f.close()

conn.close()
