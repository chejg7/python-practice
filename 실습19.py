from bs4 import BeautifulSoup
import urllib.request as req

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")

#1. css 선택자 더 자세히 작성하는 방법으로 내가 원하는 것만 출력
#price = soup.select("ul#exchangeList span.value")
#for i in price:
#   print(i.string)

#2. 데이터 가공
# price = soup.select("span.value")
# for i in price:
#     print(i.string)
#     if price.index(i) == 3:
#         break

print("==== 국가 선택 ====")
print("1. 미국")
print("2. 일본")
print("3. 유럽")
print("4. 중국")
menu = int(input("선택 >> "))
unit = ["달러", "엔", "유로", "위안"]
user_price = int(input("금액 입력(단위 : {}) >> ".format(unit[menu-1])))
price = soup.select("span.value")
print(float(price[menu-1].string.replace(",", "")) * user_price)
print("환전 결과 : {} 원".format(float(price[menu-1].string.replace(",","")) * user_price))