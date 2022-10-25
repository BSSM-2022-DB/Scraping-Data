# '//*[@id="content-container"]/div[2]/main/div/table/tbody'
# https://www.op.gg/champions?region=global&tier=platinum_plus&position=top
import json
import requests
from bs4 import BeautifulSoup
import time
from urllib import request
# url = 'https://lol.ps/ko/statistics/#section_allchamp'
url = 'https://lol.ps/lol/get_lane_champion_tier_list/?region=0&version=58&tier=2&lane=4&region=0&order_by=-op_score'
html = request.urlopen(url).read()
soup =BeautifulSoup(html)

site_json=json.loads(soup.text)
# print(site_json)
file_path = "./support_tire_talbe.json"
with open(file_path, 'w', encoding='utf-8') as outfile:
    json.dump(site_json, outfile, indent=4 , ensure_ascii=False)

# print([d.get('entrezgene') for d in site_json['hits'] if d.get('entrezgene')])

# response =requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     jsonObject = json.loads(soup)
#     print(jsonObject)
    
#     print(response.status_code)
# else : 
#     print(response.status_code)