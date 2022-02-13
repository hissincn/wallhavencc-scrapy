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
    r = requests.get(url,stream=True)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close


def downpics(search, pagenum, path,threadnum):
    if not os.path.isdir(path):
        os.makedirs(path)
    threads = []
    for one in geturls(search, pagenum):
        threads.append(threading.Thread(
            target=downpic, args=(one[0], path+one[1])))
    splitThread=int(len(threads)/threadnum)
    for onethread in range(1,splitThread+1):
        for t in threads[(onethread-1)*threadnum:onethread*threadnum]:
            t.start()          # 开启线程
        for t in threads[(onethread-1)*threadnum:onethread*threadnum]:
            t.join()           # 等待所有线程终止



#downpics('sky', 1, "D:/pic/",48)
#第一个参数为搜索关键词
#第二个参数为图片页数，每24张图片为1.若要下载96张壁纸，则输入4
#第三个参数为保存路径，末尾要有"/",如果文件夹不存在则自动创建文件夹
#第四个参数是线程数量，建议24-48，多了容易出错

downpics('sky', 5, "D:/pic/",48)