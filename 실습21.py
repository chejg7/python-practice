from selenium import webdriver
import time
import chromedriver_autoinstaller

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F")

#로그인 하기
id = browser.find_element_by_css_selector("input#id_email_2")
id.send_keys("python0308")
pw = browser.find_element_by_css_selector("input#id_password_3")
pw.send_keys("qwe123!@#")
button = browser.find_element_by_css_selector("form#login-form button.btn_g.btn_confirm.submit")
button.click()
time.sleep(3) #로그인 다 될때까지 기다려주기

#이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2) #웹페이지 다 뜰때까지 기다려주기

#이메일 제목 크롤링
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text) #셀레니움에서는 .string이 아닌 .text
browser.close()

# 왜 bs4를 먼저 배우고 셀레니움을 왜 지금 배우는가?
# 장점
# 1. 크롤링을 못하는 곳이 없다.
# 2. 코딩하기가 직관적이고 재미있다.
# 단점
# 1. 너무 느리다. (bs4의 약 5~10배)
# 2. time.sleep()의 문제(대신 암묵적 대기 라는 방법을 쓸 수도 있다)