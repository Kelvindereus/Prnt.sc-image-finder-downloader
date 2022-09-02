import requests
from bs4 import BeautifulSoup
import json
import numpy as np
import time
import string    
import random 

def loop_code_img(random_numbers_result):
    URL = "https://prnt.sc/"  + str(random_numbers_result)
    getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(getURL.text, 'html.parser')
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))

    s = images
    str1 = ""
    for i in s:
        str1 += i 
    text = str1
    
    if "i.imgur.com" in str1:
        start = text.index('i.imgur.com')
        end = text.index('.png',start)
        substring = text[start:end]
        new_img_url = str ("https://"+ str(substring) + str(".png")) 

        url = new_img_url
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        print("I found a image, and downloaded it!")
    else:
        print("....")


for _ in range(200): 
    time.sleep(1.5) 
    S = 4  
    random_numbers_result = ''.join(random.choices(string.ascii_lowercase, k = S))
    loop_code_img(random_numbers_result)

for _ in range(600): 
    time.sleep(1.5)
    S = 5 
    random_numbers_result = ''.join(random.choices(string.ascii_lowercase, k = S))
    loop_code_img(random_numbers_result)

    
for _ in range(1000): 
    time.sleep(1.5)
    S = 6
    random_numbers_result = ''.join(random.choices(string.ascii_lowercase, k = S))
    loop_code_img(random_numbers_result)

# Door kelvin
