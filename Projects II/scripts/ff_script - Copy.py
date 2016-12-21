from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException

ff_profile = webdriver.FirefoxProfile()
binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
har_exprt_tri = 'C:\\Users\\dichha\\Documents\\Graduate\\NetworkPrivacyAndSecurity\\ProjectII\\driver\\har_export_trigger-0.5.0-beta.10-fx.xpi'
#firebug_ext = 'C:\\Users\\dichha\\Documents\\Graduate\\NetworkPrivacyAndSecurity\\ProjectII\\firebug-2.0.18-fx.xpi'
#ff_profile.add_extension(firebug_ext)
#ff_profile.set_preference('devtools.netmonitor.har.enableAutoExportToFile', True)
ff_profile.add_extension(har_exprt_tri)

''' set firefox preferences '''
ff_profile.set_preference("app.update.enabled", 0)
ff_profile.set_preference("http.response.timeout",5)
ff_profile.set_preference("dom.max_script_run_time",5)
domain = 'devtools.netmonitor.har.'

''' set the preference for the trigger '''
ff_profile.set_preference("extensions.netmonitor.har.contentAPIToken", "test")
ff_profile.set_preference("extensions.netmonitor.har.enableAutmation", True)
ff_profile.set_preference("extensions.netmonitor.har.autoConnect", True)
ff_profile.set_preference(domain + "enableAutoExportToFile", True)
'''for testing 500 urls to atleast 10 appearance urls'''
ff_profile.set_preference(domain + "defaultLogDir", "C:\\Users\\dichha\\Documents\\Graduate\\NetworkPrivacyAndSecurity\\ProjectII\\HarFiles\\hillary\\bitly")
ff_profile.set_preference('webdriver.load.strategy','unstable')
time.sleep(2)

'''create ff driver'''

driver = webdriver.Firefox(firefox_binary=binary,firefox_profile = ff_profile)
'''
driver.get("https://t.co/5uuHz24Wst")
driver.get("https://t.co/vxK6L549ky")
driver.get("https://t.co/Trgh1CTMAE")
'''
count_timeout=0
count = 0
urls = open('urls_h\\bitly_visit_urls_h.txt', 'r', encoding='utf-8')
for url in urls:
    url = url.strip()
    count+=1
    #print(url)
    try:
        driver.set_page_load_timeout(5)  
        driver.get(url)
    except TimeoutException:
        print("timeout url: %s"%str(url))
        count_timeout+=1
    print(url)
    print(count)
    print("Time out %s"%count_timeout)
print("Total number of timeout: %s"%str(count_timeout))
    

driver.close()
driver.quit()
