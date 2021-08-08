from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par # 한글 사용하기 위해
import os # 폴더 생성하기 위해

if not os.path.exists("./이미지수집"):
    os.mkdir("./이미지수집")

keyword = input("키워드 입력 >> ")

if not os.path.exists(f"./이미지수집/{keyword}"):
    os.mkdir(f"./이미지수집/{keyword}")

encoded = par.quote(keyword) # 한글 -> 특수한 문자열
code = req.urlopen(f"https://images.search.yahoo.com/search/images;_ylt=Awr9DWun8w1hnBUAOBaLuLkF;_ylc=X1MDOTYwNTc0ODMEX3IDMgRmcgN5ZnAtdARncHJpZANheUV1dTE2YVFiRzRaQXRRejdqOHlBBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMjcEcXVlcnkDJUVDJTk1JTg0JUVDJTlEJUI0JUVEJThGJUIwBHRfc3RtcAMxNjI4MzA0Mjk5?p={encoded}&ei=UTF-8&iscqry=&fr=yfp-t&fr2=sb-top-images.search")
soup = BeautifulSoup(code, "html.parser")
img = soup.select("a > img")
for i in img:
    print(i.attrs) # .attrs : 요소의 속성
    img_url = i.attrs["data-src"]
    req.urlretrieve(img_url, f"./이미지수집/{keyword}/{img.index(i) + 1}.png")
    print(f"{keyword} 이미지 크롤링 완료 {img.index(i) + 1}")