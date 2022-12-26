from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
url_last = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/32'
driver_path = "./chromedriver.exe"

ch_op = Options()
ch_op.add_experimental_option('detach', True)
ser = Service(driver_path)

driver = webdriver.Chrome(service=ser, options=ch_op)


driver.get(url)


def next_page():

    try:
        driver.find_element(
            By.CSS_SELECTOR, '.pagination__btn.pagination__next-btn.pagination__btn--off')
        return False
    except:
        btn = driver.find_element(
            By.CSS_SELECTOR, '.pagination__btn--inner .icon-right-open')
        ''' btn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.pagination__btn--inner .icon-right-open')))'''
        if btn:
            btn.click()

            return True
        else:
            print('something went wrong!')
            return False


major = []
d_t = []
e_c_p = []
m_c_p = []
h_m = []
dic = {}
while next_page():
    rows = driver.find_elements(By.CLASS_NAME, 'data-table__row')
    # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)

    rank = None
    for row in rows:

        items = row.find_elements(By.CSS_SELECTOR, 'td .data-table__value')
        for i in items:
            if items.index(i) == 0:

                continue
            elif items.index(i) == 1:
                print(i.text)
                major.append(i.text)
            elif items.index(i) == 2:
                text = i.get_attribute("innerHTML")
                d_t.append(text)

            elif items.index(i) == 3:
                e_c_p.append(i.text)
            elif items.index(i) == 4:
                m_c_p.append(i.text)
            elif items.index(i) == 5:

                h_m.append(i.text)
    time.sleep(.6)
driver.quit()
dic['Major'] = major
dic['Degree Type'] = d_t
dic['Early Career Pay'] = e_c_p
dic['Mid Career Pay'] = m_c_p
dic['High Meaning'] = h_m

dframe = pd.DataFrame(dic)
dframe.to_csv('data.csv', encoding='utf-8')
print(dframe)
