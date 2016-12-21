import re
urls_file = open("urls/test_1001.txt", 'r')

test_10_clean_url = open("urls/test_1001_clean.txt", 'w')
urls_string = urls_file.read()

for match in re.finditer("https://t.co/\\w*",urls_string, re.S):
    #print(match.group())
    test_10_clean_url.write(match.group()+"\n")
test_10_clean_url.close()
urls_file.close()
