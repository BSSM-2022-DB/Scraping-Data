import json
import pymysql
db = pymysql.connect(host='localhost',
                             user=username,
                             password=password,
                             database='2022_DB_PROJECT',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

with open("bottom_tire_table.json", "r", encoding='utf-8') as b_json: # 여기서 JSON 파일만 바꿔가면서 해서 넣으면 됨
    all_list_champion_result = json.load(b_json)
    data = list()
    # print(all_list_champion_result['results'])
    for el in all_list_champion_result['results']:
        # print(el)
        # champion_data_key , line_id , 승률 , 밴률 , 픽률 , 티어 
        champion_data_key = el['champion__data_key']
        line_id = el['lane__lane_id']
        win_rate = el['win_rate']
        ban_rate = el['ban_rate']
        pick_rate = el['pick_rate']
        tier = el['op_tier']
        
        sql=f'insert into champion_info(cham_key,line_id,win_rate,ban_rate,pick_rate,tier) values({champion_data_key},{line_id},"{win_rate}","{ban_rate}","{pick_rate}","{tier}")'
        print(sql)
        cursor.execute(sql)
        res = cursor.fetchall()
    
    db.commit()
    db.close()
