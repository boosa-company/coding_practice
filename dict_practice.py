import pandas as pd
from pprint import pprint


my_dict = {'mode': 123123,
           'tmEf': '2022-02-12 00:00',
           'wf': '구름많음',
           'tmn': '0',
           'tmx': '9',
           'reliability': None,
           'test': {
               '송종이 꼬추': "3cm",
               '송종이': "현욱이 친구"
           },
           'test3': [
               {'지역': "서울", '지역번호': 3},
               {'지역': "서울", '지역번호': 33},
               {'지역': "서울", '지역번호': 333},
               {'지역': "인천", '지역번호': 5},
               {'지역': "경기", '지역번호': 1}],
           'rnSt': '20'}


cand_df = my_dict["test3"]
df = pd.DataFrame(cand_df, columns=["지역", "지역번호"])
print(df)

df_seoul = df[(df["지역"] == "서울")]

print(df_seoul)
