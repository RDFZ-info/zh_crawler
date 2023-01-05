#知乎热搜 
#time interval : 1h everyday
#output : txt

import datetime
import requests
import os
import sys

os.chdir(sys.path[0])
url = "https://www.zhihu.com/api/v4/search/top_search"
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
topsearch=res.json()["top_search"]

data = topsearch["words"]
#print(data)
hot_list = []
for item in data:
    item_query = item["query"]
    item_display_query= item["display_query"]
    hot_list.append("{}: {}".format(item_query, item_query))

output = "\n".join(hot_list)
if os.path.exists("./hotresearch/{}_{}_{}".format(year, month, day))==False:
    os.mkdir(r"./hotresearch/{}_{}_{}".format(year, month, day))

with open("./hotresearch/{}_{}_{}/{}_{}_{}_{}.txt".format(year, month, day, year, month, day, hour), mode="w") as f:
    f.write(output)


#log
with open("../log/{}_{}_{}.txt".format(year, month, day), "a",encoding="utf8") as f:
    f.write("{}_{}_{}_{} zhihu hot research list rec. \n".format(year, month, day, hour))