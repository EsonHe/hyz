import requests
import re

url = 'https://www.qiushibaike.com/text/page/'
for i in range(20):
    countent = requests.get(url+'i/').text
    text1 = re.findall(r'<div\sclass="content">(.*?)<span>(.*?)</span>',countent,re.S)

def qiushi(text1):
    duanzi = []
    for i in text1:
        for j in i:
            x = re.sub(r'<.*?>', '', j).strip()
            duanzi.append(x)
    for i in duanzi:
        with open('段子.txt','a+',encoding='utf-8') as f:
            f.write(i+'\n')


for i in range(20):
    countent = requests.get(url + 'i/').text
    text1 = re.findall(r'<div\sclass="content">(.*?)<span>(.*?)</span>', countent, re.S)
    qiushi(text1)