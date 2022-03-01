# coding:utf-8
import sys

import NetControl

# 真不卡影院

reload(sys)
sys.setdefaultencoding('utf8')


# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseurl = 'http://www.zhenbuka.com/vodshow/1--------' + str(page) + '---/'
        fileUrl = 'http://www.zhenbuka.com'
        soup = NetControl.sendRequest(baseurl)
        for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
            title = tag.find('a', class_='stui-vodlist__thumb lazyload').get('title')
            url = fileUrl + tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('真不卡影院  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
        title = tag.find('a', class_='stui-vodlist__thumb lazyload').get('title')
        img = tag.find('a', class_='stui-vodlist__thumb lazyload').get('data-original')
        url = fileUrl + tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
        des = tag.find('div', class_='stui-vodlist__detail active').find('p').string
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (title + '   ' + img + '   ' + url + '   ' + des)


# 执行程序
def run():
    fileUrl = 'http://www.zhenbuka.com'
    page = 1
    source = 1
    file_handle = open('dev/真不卡影院.txt', mode='w')
    while page < 750:
        baseurl = 'http://www.zhenbuka.com/vodshow/1--------' + str(page) + '---/'
        soup = NetControl.sendRequest(baseurl)
        checkFilms(fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
