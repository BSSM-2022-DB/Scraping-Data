import json
import pymysql
db = pymysql.connect(host='localhost',
                             user='sion',
                             password='1713',
                             database='2022_DB_PROJECT',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
with open("all_champion_list.json", "r", encoding='utf-8') as b_json:
    all_list_champion_result = json.load(b_json)
    data = list()
    # print(all_list_champion_result['results'])
    for el in all_list_champion_result['results']:
        # key name id
        c_key  = el['data_key']
        c_name = el['name']
        c_id   = el['data_id']
        sql=f'insert into all_champion_list(cham_key,cham_name,cham_id) values({c_key},"{c_name}","{c_id}")'
        print(sql)
        cursor.execute(sql)
        res = cursor.fetchall()
    
    db.commit()
    db.close()