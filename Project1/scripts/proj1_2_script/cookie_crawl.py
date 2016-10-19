from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import shutil
import time
import datetime

ff_prof = webdriver.FirefoxProfile()
fp_ext = 'C:\\Users\\Dichha Chamling\\Documents\\fourthparty-master\\fourthparty-master\\extension\\fourthparty-jetpack.1.13.2.xpi'
ff_prof.add_extension(fp_ext)
driver = webdriver.Firefox(ff_prof)
temp_folder = (driver.firefox_profile.path)
print(temp_folder)
visit_time_f = open("../test_visit_time.txt", 'w')

#opening an alexa file
alexa_f = open('..\\alexa_top500_cookie.txt', 'r')
for i in range(497):
    #print(alexa_f.readline())
    current_url = alexa_f.readline().strip()
    begin_time = ''
    
    #print(url_list[1])
    try:
        
        visit_url = "http://www."+current_url+"/"
        driver.set_page_load_timeout(20)
        '''getting current timestamp for knowing when a cookie was setup'''
        time_stamp = time.time()
        begin_time = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
        print("%s time begins " %current_url)
        #visit_time_f.write(current_url+" begins: "+ human_readable_ts +"\n")
        driver.get(visit_url)
        
    except TimeoutException:
        #pass
        print("timeout url : " + str(visit_url))
    driver.implicitly_wait(30)
    '''getting current timestamp for knowing when a cookei was setup'''
    time_stamp = time.time()
    end_time = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    visit_time_f.write(str(current_url)+" , "+ begin_time + " , " + end_time + "\n")
    print("%s time ends "%current_url)
    
shutil.copy2(temp_folder + '\\cookies.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\cookies_eval.sqlite')
shutil.copy2(temp_folder + '\\fourthparty.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\fourthparty_cookies_eval.sqlite')
visit_time_f.close()
alexa_f.close()        
driver.close()
    
