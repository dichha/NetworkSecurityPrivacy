from random import randint

length = 289

file = open('urls_d_h\\donald\\google_urls_d.txt','r')
tweet_h = open('google_visit_urls_d.txt', 'w')
line_visit_list = []
count = 0
while(count < 100):
    line_num = randint(1,length)
    if line_num not in line_visit_list:
        line_visit_list.append(line_num)
        count+=1

#print(line_visit_list)
for val in line_visit_list:
    file_line = file.readline(val)
    #print(file_line)
    tweet_h.write(file_line)
    
tweet_h.close()
file.close()
