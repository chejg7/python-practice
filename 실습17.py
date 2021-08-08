from bs4 import BeautifulSoup
import urllib.request as req

# 서버한테 html 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
#print(code.read())

#html 코드 예쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
#print(soup)

# 내가 원하는 요소 가져오게 하기
title = soup.select_one("strong.title")
#print(title)

# 요소 내용 출력하기
print(title.string)