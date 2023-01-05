#知乎热榜热榜 (首页热榜栏)
#time interval : 1h everyday
#output : txt
#website : https://www.zhihu.com/hot

import datetime
import requests
import os
import sys


os.chdir(sys.path[0])

url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true"
headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}


now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day
hour = now_time.hour


sess = requests.Session()
res = sess.get(url, headers=headers)
data = res.json()["data"]
#print(data)
hot_list = []
for item in data:
    item_id = item["target"]["id"]
    item_title = item["target"]["title"]
    item_url = item["target"]["url"]  
    hot_list.append("{}: {}".format(item_id, item_title,item_url))

output = "\n".join(hot_list)
if os.path.exists("./hotquestion/{}_{}_{}".format(year, month, day))==False:
    os.mkdir(r"./hotquestion/{}_{}_{}".format(year, month, day))

with open("./hotquestion/{}_{}_{}/{}_{}_{}_{}.txt".format(year, month, day, year, month, day, hour), mode="w") as f:
    f.write(output)

#log
with open("../log/{}_{}_{}.txt".format(year, month, day), "a",encoding="utf8") as f:
    f.write("{}_{}_{}_{} zhihu hotquestion list rec. \n".format(year, month, day, hour))