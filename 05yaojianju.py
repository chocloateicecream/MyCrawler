import requests 
url='http://scxk.nmpa.gov.cn:81/xk/'
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
page_text=requests.get(url=url,headers=headers).text

with open('./huazhuangpin.html','w',encoding='utf-8') as fp:
    fp.write(page_text)