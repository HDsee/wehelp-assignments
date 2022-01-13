# 串接、擷取公開資料
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) # 利用json 模組處理 json 資料格式

#資料列表建立
list=data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for target in list:
        file.write(target["stitle"]+ ',')
        file.write(target["address"][5:8]+ ',')
        file.write(target["longitude"]+ ',')
        file.write(target["latitude"]+ ',')
        url=target["file"].split("jpg")
        file.write(url[0]+ 'jpg' + '\n')
