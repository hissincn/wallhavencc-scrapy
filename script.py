import requests
from bs4 import BeautifulSoup
import threading
import os


def geturls(search, pageall):
    searchlist = []
    for pagenum in range(1, pageall+1):
        res = requests.get('https://wallhaven.cc/search', params=(
            ('q', search),
            ('page', pagenum),
        ))
        for i in BeautifulSoup(res.text, "html.parser").find_all('figure'):
            if (i.div.find_all("span", "png")):
                searchlist.append(["https://w.wallhaven.cc/full/" + i['data-wallpaper-id'][0:2] +
                                  "/wallhaven-"+i['data-wallpaper-id']+".png", i['data-wallpaper-id']+".png"])
            else:
                searchlist.append(["https://w.wallhaven.cc/full/" + i['data-wallpaper-id'][0:2] +
                                  "/wallhaven-"+i['data-wallpaper-id']+".jpg", i['data-wallpaper-id']+".jpg"])

    return searchlist


def downpic(url, path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close


def downpics(search, pagenum, path):
    if not os.path.isdir(path):
        os.makedirs(path)
    threads = []
    for one in geturls(search, pagenum):
        threads.append(threading.Thread(
            target=downpic, args=(one[0], path+one[1])))
    for onethread in range(1,pagenum):
        for t in threads[(onethread-1)*24:onethread*24]:
            t.start()          # 开启线程
        for t in threads[(onethread-1)*24:onethread*24]:
            t.join()           # 等待所有线程终止


#downpics('sky', 1, "D:/pic/")
#第一个参数为搜索关键词
#第二个参数为图片页数，每24张图片为1.若要下载96张壁纸，则输入4
#第三个参数为保存路径，末尾要有"/",如果文件夹不存在则自动创建文件夹

downpics('sky', 20, "D:/pic/")