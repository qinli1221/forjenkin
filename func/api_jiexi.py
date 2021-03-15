import requests
import json

def get_Asc(res):
    dic = res.json()
    arry = dic["apiResult"]['data']
    good_list=[]
    # print(arry)
    for i in arry[0:2]:
        id = i['id']
        sold = i['soldNum']
        good_list.append((id,sold))
    a = good_list[0][1]
    b = good_list[1][1]
    return a,b

