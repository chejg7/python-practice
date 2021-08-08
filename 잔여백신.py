from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

chrome_driver = 'C:/utill/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

# 잔여백신 페이지
driver.get('https://m.place.naver.com/rest/vaccine?vaccineFilter=used')

# '목록보기'가 로딩 될때까지 대기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._31ySW')))
# '목록보기' 클릭
driver.find_element_by_class_name('_31ySW').click()

# 현재 페이지 html
soup = BeautifulSoup(driver.page_source, "html.parser")

vaccin = False

# 잔여 백신을 찾는 반복문
while vaccin == False:
    no = 0

    # 잔여 백신이 있는 경우, 반복문 종료
    for hospital in soup.select('li._1mrr7'):
        status = hospital.select_one('a._46SXN > strong').get_text()
        if (status != '대기중') and (status != '마감'):
            vaccin = True
            break
        no += 1

    # 잔여 백신이 없는 경우, 새로고침 버튼 클릭
    if no == 100:
        reset_btn = driver.find_element_by_css_selector('a._1MCHh')
        reset_btn.click()

# 잔여 백신이 있는 병원의 '접종 예약 신청' 버튼 클릭
apply_btns = driver.find_elements_by_css_selector("a[class='lwEWu _1dEyY'")
apply_btns[no].click()
