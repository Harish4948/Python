import mechanize
from BeautifulSoup import BeautifulSoup as bs
import re
chrome = mechanize.Browser()
chrome.set_handle_robots(False)
chrome.addheaders = [('User-agent', 
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]
base_url = 'https://www.google.co.in/search?q='
proxies=["46.52.164.204","195.55.233.135","103.102.218.225","103.99.161.9","89.218.5.106"]
f=open("email.txt","r")
test_file=f.readlines()
valid=[]
for i in test_file:
      i=i.strip()
      search_url = base_url +'"'+i.replace(' ', '+')+'"'
      htmltext = chrome.open(search_url).read()
      tag="<em>"+i+"</em>"
      l=len(re.findall(tag,htmltext))
      #print(l)
      if(l>0):
            print(i)
            valid.append(i)
