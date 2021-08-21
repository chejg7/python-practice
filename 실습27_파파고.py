import os
import sys
import urllib.request
import json

import urllib.request as req
from bs4 import BeautifulSoup
import re

keyword = input("영어로 키워드 입력 >> ")
page_num = 1
while True:
    url = "http://www.koreaherald.com/search/index.php?q={}&sort=1&mode=list&np={}&mp=1".format(keyword, page_num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    articles = soup.select("ul.main_sec_li > li > a")
    if len(articles) == 0:
        break
    for i in articles:
        title = i.select_one("div.main_l_t1")
        print("제목 :", title.text)
        link = "http://www.koreaherald.com" + i.attrs["href"]
        code_news = req.urlopen(link)
        # html 코드에서 html 문법에 위배되는 것 같은 부분들을 수정 및 삭제해줌.
        code_news = str(code_news.read()).replace("<center>", "").replace("</center>", "").replace('</div><img alt=""',
                                                                                                   '<img alt="').replace(
            '<div class="view_con_t"></td>', '<div class="view_con_t"></div></td>')
        soup_news = BeautifulSoup(code_news, "html.parser")
        contents = soup_news.select_one("div#articleText")
        # 데이터 가공
        result = re.sub(r'(\\[x]..)|(\\r)|(\\n)|(\\t)|(\(Yonhap\))', "", contents.text.strip())

        # 한글로 번역(파파고 API 사용)

        client_id = "Yf48Db0_ZWAcwv2GZKDX"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "ZxtxI3tj82"  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(result)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))  # json->딕셔너리
            print(result["message"]["result"]["translatedText"])
        else:
            print("Error Code:" + rescode)


        print()
    page_num += 1
