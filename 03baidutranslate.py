from fileinput import filename
from matplotlib.pyplot import text
import json 
import requests 

post_url='https://fanyi.baidu.com/sug'

#ua
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
word=input("enter contents: ")
#post请求参数处理（同get请求一致）
data1={
    'kw':word
}

response=requests.post(url=post_url,data=data1,headers=headers)
#获取响应数据，返回的是json
dic_obj=response.json()
print(dic_obj)
filename1=word+'.json'

#cunchu
fp=open(filename1,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)
# with open(filename1,'w',encoding='utf-8') as fp:
#     fp.write(dic_obj)
print("done.")