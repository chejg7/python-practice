import json
import requests
import folium
import os
from selenium import webdriver

api_key = "61426d63716c797938326b46766767"
url = "http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/100/".format(api_key)
data = requests.get(url)
result = json.loads(data.text) # json -> 딕셔너리
# print(json.dumps(result, indent="\t")) # json 파일을 보기 좋게 만들어준다 : 탭으로 구분
bikes = result["rentBikeStatus"]["row"]
# 좌표 중심값 구하기
lat_sum = 0
lon_sum = 0
for i in bikes:
    lat_sum += float(i["stationLatitude"])
    lon_sum += float(i["stationLongitude"])
lat_avr = lat_sum/len(bikes)
lon_avr = lon_sum/len(bikes)
map = folium.Map([lat_avr, lon_avr], zoom_start=14)
for i in bikes:
    station_name = i["stationName"]
    bike_num = int(i["parkingBikeTotCnt"]) # 문자열 -> 정수형
    if bike_num < 3:
        color = "red"
    elif 3 <= bike_num < 7:
        color = "blue"
    else:
        color = "green"
    lat = float(i["stationLatitude"]) # 문자열 -> 실수형
    lon = float(i["stationLongitude"])
    folium.Marker([lat, lon], popup=station_name, tooltip=bike_num, icon=folium.Icon(color=color)).add_to(map)
map.save("./따릉이.html")

# 실행시킬 때마다 위의 파일을 찾아서 브라우저로 여는건 귀찮다. 이걸 자동화하려면 아래와 같이 하자!
path = os.path.abspath("./따릉이.html") # 따릉이.html 파일의 전체 경로를 구해주는 함수
browser = webdriver.Chrome("./chromedriver")
# 윈도우 사용자의 경우
# browser.get(path)
browser.get("file://" + path)