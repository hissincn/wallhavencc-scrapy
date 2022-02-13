# wallhavencc-scrapy
Python并发爬取wallhaven.cc壁纸，可以自定义搜索词及爬取数量

# 用法
1.下载
2.输入下方命令安装依赖库
pip install requests
pip install bs4
3.改参数，运行

第一个参数为搜索关键词
第二个参数为图片页数，每24张图片为1.若要下载96张壁纸，则输入4
第三个参数为保存路径，末尾要有"/",如果文件夹不存在则自动创建文件夹
例如：downpics('sky', 1, "D:/pic/")
