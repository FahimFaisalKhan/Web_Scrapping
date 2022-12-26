# from seleniumwire import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# import json
# opts = Options()
#
# path="E:/development/chromedriver.exe"
# driver = webdriver.Chrome(options=opts,executable_path=path)
#
# #url of map location
# driver.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/")
# time.sleep(2)
# count=1
# for request in driver.requests:
#     print("a")
#     if request.url.startswith("https://www.zillow.com/search/GetSearchPageState.htm?"):
#             responseBody=json.loads(request.response.body)
#             for home in responseBody["cat1"]["searchResults"]["mapResults"]:
#                 print('b')
#                 print(count)
#                 try:
#
#                  print(home["hdpData"]["homeInfo"])
#                  print('c')
#                 except:
#                  print("No home info "+home["price"])
#                 count+=1
#             break
#


import json
import requests
from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url="https://www.youtube.com/"
zillow="https://www.zillow.com/homes/San-Francisco,-CA_rb/"

path="E:/development/geckodriver.exe"
opt=Options()

header={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
opt.add_argument("'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'")

opt.binary_location='C:/Program Files/WindowsApps/Mozilla.Firefox_96.0.3.0_x64__n80bbvh6b1yt2/VFS/ProgramFiles/Firefox Package Root/firefox.exe'
driver =webdriver.Firefox(executable_path=path,options=opt)
driver.get(url)
# driver.set_window_size(810,1080)


loop=True


html = driver.find_element_by_tag_name('html')

last_height = driver.execute_script("return document.documentElement.scrollHeight")
print(last_height)

while loop:
    # driver.execute_script(
    #     # 'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
    #     "arguments[0].scrollTop = arguments[0].scrollHeight",
    #     html)


    # driver.execute_script(f"window.scrollTo(0,document.documentElement.scrollHeight);")
    driver.execute_script(f"window.scrollTo(0,{last_height});")
    # t = driver.find_elements_by_css_selector('script[type="application/ld+json"]')
    # prices = driver.find_elements_by_class_name("list-card-price")
    # addresses = driver.find_elements_by_class_name("list-card-addr")
    # links = driver.find_elements_by_class_name("list-card-link")
    time.sleep(3)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    # print(new_height)
    if new_height == last_height:
        t = driver.find_elements_by_id('video-title')
        for i in t:
            print(i.get_attribute('innerHTML'))

        # time.sleep(1.5)
        break
    last_height = new_height

soup=BeautifulSoup(driver.page_source,'html.parser')
lists=soup.find_all("a", class_="zsg-photo-card-overlay-link")
print(len(lists))






# driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', side_bar)

# res=requests.get(url=url,headers=header)
# soup=BeautifulSoup(res.text,'lxml')
# print(soup.find('yt-formatted-string',id='video-title'))