# '//*[@id="content-container"]/div[2]/main/div/table/tbody'
# https://www.op.gg/champions?region=global&tier=platinum_plus&position=top
import json
# import requests
# from bs4 import BeautifulSoup
# import time
# from urllib import request
# # url = 'https://lol.ps/ko/statistics/#section_allchamp'
# url = 'https://lol.ps/lol/get_lane_champion_tier_list/?region=0&version=58&tier=2&lane=4&region=0&order_by=-op_score'
# html = request.urlopen(url).read()
# soup =BeautifulSoup(html)

# site_json=json.loads(soup.text)
# # print(site_json)
# file_path = "./support_tire_talbe.json"
# with open(file_path, 'w', encoding='utf-8') as outfile:
#     json.dump(site_json, outfile, indent=4 , ensure_ascii=False)

with open("bottom_tire_table.json", "r", encoding='utf-8') as b_json:
    b_result = json.load(b_json)
    # print(json.dumps(b_result,indent="\t",ensure_ascii=False))
    # champion_name = b_result['results'][0] # test
    # print(champion_name)
    b_champion_names = list()
    for el in b_result['results']:
        # print(el['champion__name'])
        champion_name = el['champion__name']
        # ['champion__data_key']['champion__name_us']['lan__lane_id']
        b_champion_names.append(champion_name)
    print(b_champion_names)
    print(len(b_champion_names))
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