# coding:utf-8

import NetControl


# VIP影院

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.vipyy666.com/index.php/vod/show/id/1/page/' + str(page) + '.html'
        fileUrl = 'https://www.vipyy666.com'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
            title = tag.find('a', class_='stui-vodlist__thumb lazyload').get('title')
            url = fileUrl + tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('VIP影院  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
        title = tag.find('a', class_='stui-vodlist__thumb lazyload').get('title')
        img = tag.find('a', class_='stui-vodlist__thumb lazyload').get('data-original')
        url = fileUrl + tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
        des = ''
        if None != tag.find('p',class_='text text-overflow text-muted hidden-xs').string:
            des = tag.find('p',class_='text text-overflow text-muted hidden-xs').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    source = 18
    maxPage = 683
    file_handle = open('dev/VIP影院.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.vipyy666.com/index.php/vod/show/id/1/page/' + str(page) + '.html'
        fileUrl = 'https://www.vipyy666.com'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
