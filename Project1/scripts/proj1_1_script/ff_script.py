from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import shutil

ff_prof = webdriver.FirefoxProfile()
fp_ext = 'C:\\Users\\Dichha Chamling\\Documents\\fourthparty-master\\fourthparty-master\\extension\\fourthparty-jetpack.1.13.2.xpi'
ff_prof.add_extension(fp_ext)
driver = webdriver.Firefox(ff_prof)
temp_folder = (driver.firefox_profile.path)
print(temp_folder)

#opening an alexa file
alexa_f = open('C:\\Users\\Dichha Chamling\\Documents\\top-1m.csv\\top-1m.csv', 'r')
for i in range(500):
    #print(alexa_f.readline())
    line = alexa_f.readline()
    url_list = [url.strip() for url in line.split(',')]
    #print(url_list[1])
    try:
        
        visit_url = "http://www."+ str(url_list[1])
        driver.set_page_load_timeout(20)
        driver.get(visit_url)
        
    except TimeoutException:
        #pass
        print("timeout url : " + str(url_list[1]))
    driver.implicitly_wait(30)
    
shutil.copy2(temp_folder + '\\cookies.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\cookies_main_v30.sqlite')#test.sqlite')
shutil.copy2(temp_folder + '\\fourthparty.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\fourthparty_main_v30.sqlite')#fp_test.sqlite')
alexa_f.close()
try:
    driver.get("http://www.kakaku.com")#facebook wait, worked fine later
    driver.set_page_load_timeout(20)
    shutil.copy2(temp_folder + '\\cookies.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\cookies_main_v30.sqlite')#test.sqlite')
    shutil.copy2(temp_folder + '\\fourthparty.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\fourthparty_main_v30.sqlite')#fp_test.sqlite')
except TimeoutException:
    print("http://www.kakaku.com")
    
driver.implicitly_wait(30)
try:
    driver.get("http://www.wp.pl")#modal asking for redirection causes crash
    driver.set_page_load_timeout(20)
    shutil.copy2(temp_folder + '\\cookies.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\cookies_main_v30.sqlite')#test.sqlite')
    shutil.copy2(temp_folder + '\\fourthparty.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\fourthparty_main_v30.sqlite')#fp_test.sqlite')
except TimeoutException:
    print("http://www.wp.pl.com")
    
driver.implicitly_wait(30)
try:
    driver.get("http://www.globo.com")#webdriver crashes
    driver.set_page_load_timeout(20)
    shutil.copy2(temp_folder + '\\cookies.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\cookies_main_v30.sqlite')
    shutil.copy2(temp_folder + '\\fourthparty.sqlite', 'C:\\Users\\Dichha Chamling\\Documents\\fourthparty_main_v30.sqlite')
except TimeoutException:
    print("http://www.globo.com")
    
    
driver.close()
    
