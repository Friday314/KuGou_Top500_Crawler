import requests
import time
from bs4 import BeautifulSoup

_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}


def get_info(url):

    #print(url)

    # 请求网址
    wb_data = requests.get(url, headers=_headers)

    # 解析网址
    soup = BeautifulSoup(wb_data.text, "lxml")

    times = soup.select("span.pc_temp_tips_r > span")
    # print(times)

    ranks = soup.select("span.pc_temp_num")
    # print(ranks)

    titles = soup.select("div.pc_temp_songlist > ul > li > a")
    # print(titles)

    for time, rank, title in zip(times, ranks, titles):
        data = {
            "歌名" : title.get_text().split("-")[1],
            "歌手" : title.get_text().split("-")[0],
            "时长" : time.get_text().strip(),
            "排行" : rank.get_text().strip()
        }

        print(data)


# main 函数
if __name__ == "__main__":

    # url 集合
    urls = ["http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(number) for number in range(1, 11)]

    # 遍历 url
    for url in urls:

        get_info(url)

        time.sleep(2)
