import requests
import json

api_key = "0e116f2b1751d8eb63979606a1870a03"
city = "Seoul"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
data = requests.get(url)
# print(data.text["name"])
# 던져주는 데이터가 딕셔너리처럼 보이는데 왜 딕셔너리 자료 형태로 출력이 안되나?
# [데이터 표현 형식]
# 1. csv(Comma Seperated Values)
# 포도,배,사과
# 100,200,300
#
# 2. json
# {"포도":100, "배":200, "사과":300}
result = json.loads(data.text) #json -> 딕셔너리형
print(result["name"])
print(result["weather"][0]["main"])