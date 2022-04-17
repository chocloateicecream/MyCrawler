import json 
import requests 

url='https://movie.douban.com/j/chart/top_list'

param={
    'type': '24',
    'interval_id': '100:90',
    'action':'' ,
    'start': '1',#从数据库中第i部电影取
    'limit': '20' #一次取20
}
#ua
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}

response=requests.get(url=url,params=param,headers=headers)

list_data=response.json()

fp=open('./doban.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)

print('done.')