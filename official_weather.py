from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
import xmltodict
from pprint import pprint

# url for request
url = 'http://data.kma.go.kr/apiData/getData'

params = '?' + urlencode({
    quote_plus("type"): "json",
    quote_plus("dataCd"): "ASOS",
    quote_plus("dateCd"): "HR",
    quote_plus("startDt"): "20220208",
    quote_plus("startHh"): "00",
    quote_plus("endDt"): "20220208",
    quote_plus("endHh"): "23",
    quote_plus("stnIds"): "108",
    quote_plus("schListCnt"): "500",
    quote_plus("pageIndex"): "1",
    quote_plus("apiKey"): "yL4PaclXcPNtnNq%2Bt2ZrR9PatWUGAL2JhHPVpa44EIBbxkL424Y8Dw%2FNzZAtJCQ3LQoYpCLNeTzKHvzjAaG7%2Bw%3D%3D"})
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=LZEpO87Hbn58Wh%2BBr44bkZiMwes8%2BJTs6EGhHEvdfch5enUB65lUpuIKCXC4RuupO5hPgriWSv29bRnIYxhmhg%3D%3D&pageNo=1&numOfRows=10&dataType=XML&base_date=20220209&base_time=0500&nx=55&ny=127"
req = urllib.request.Request(url)
print(req)


# response_body = urlopen(req, timeout=60).read()  # get bytes data
# print(response_body)
# Get Data from API
response_body = urlopen(req, timeout=60).read()  # get bytes data
# Convert bytes to json

decode_data = response_body.decode('utf-8')
print(type(decode_data))

xml_parse = xmltodict.parse(decode_data)     # string인 xml 파싱
xml_dict = json.loads(json.dumps(xml_parse))


pprint(xml_dict)
