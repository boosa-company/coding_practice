import requests
from bs4 import BeautifulSoup
year = 2021
month = 5
day = 2


def scrape_weather():
    print("서울 날씨")
    # url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=2022년+2월+7일+날씨"
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}년+{}월+{}일+날씨%".format(year, month, day)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    cast = soup.find("p", attrs={"class": "dsc"}).get_text()
    # 구름 많음
    temp = soup.find("p", attrs={"class": "temp"}).get_text()
    # min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    # max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    print(cast)
    print(temp)
    # print(" {} ( {} / {} )".format(curr_temp, min_temp, max_temp))
    # 현재 00도씨 (최저 00도씨/ 최고 00도씨)


if name == "main":
    scrape_weather()  # 오늘의 날씨 정보 가져오기
