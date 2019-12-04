from selenium import webdriver
from pygame import mixer
import sys
import os
import time

os.system('clear')

mixer.init()
alert = mixer.Sound('alert.wav')

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
print('status')
print()
flag = 0

while True:
    try:
        status = driver.find_element_by_class_name('_315-i').get_attribute('title')
        usr = driver.find_element_by_class_name('_19RFN').get_attribute('title')
        #os.system('clear')
        #print(status)
        if status == 'online':
            time.sleep(0.5)
            if flag == 0:
                alert.play()
                print(usr+' :: '+str(time.ctime()))
                flag = 1
        else:
            flag = 0
            alert.stop()
    except:
        status = None
        flag = 0
        alert.stop()