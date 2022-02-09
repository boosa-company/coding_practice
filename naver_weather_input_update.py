from bs4 import BeautifulSoup
from urllib import request
import pandas as pd
import xmltodict
from pprint import pprint
import json


def get_weather_data(date, data_name):
    # 서울의 오늘부터 1주일 동안의 데이터 리턴
    response_body = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108").read()

    # xml format -> python dict 형태처리

    decode_data = response_body.decode('utf-8')
    xml_parse = xmltodict.parse(decode_data)  # string인 xml 파싱
    xml_dict = json.loads(json.dumps(xml_parse))

    # 필요한 데이터 접근 및 축약
    weather_data_list = xml_dict["rss"]["channel"]["item"]["description"]["body"]["location"][0]["data"]

    df = pd.DataFrame(weather_data_list, columns=["mode", "tmEf", "wf", "tmn", "tmx", "reliability", "rnSt"])
    df.columns = ["mode", "날짜", "날씨", "최저기온", "최고기온", "신뢰도", "rnSt"]
    print(df)

    locaion_list = ['서울', '서울', '서울', '서울', '서울', '인천', '인천', '인천', '인천', '인천', '가평', '가평', '가평']
    print(len(locaion_list))

    df.insert(3, '지역', locaion_list)
    print(df)
    df[['최저기온', '최고기온']] = df[['최저기온', '최고기온']].apply(pd.to_numeric)

    df_new = df[(df["날짜"] == date)]

    df_low = df[(df["최저기온"] < -3)]

    print(df_low)

    df_low = df_low[(df_low["지역"] != "가평")]

    print(df_low)
    if data_name == "날씨":
        result = df_new["날씨"].iloc[0]
    elif data_name == "최저기온":
        result = df_new["최저기온"].iloc[0]
    elif data_name == "최고기온":
        result = df_new["최고기온"].iloc[0]
    else:
        result = ""

    return result


def main():
    # while True:
    # target_date = str(input("날짜를 입력해주세요 : \n"))
    # weather = get_weather_data(target_date)
    weather = get_weather_data("2022-02-13 12:00", "최저기온")
    print(weather)
    '''
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추
    송종이 꼬추 3cm 안깐 포경꼬추


    '''
    # print("")


main()
