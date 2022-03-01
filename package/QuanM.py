# coding:utf-8

import NetControl


# 全民电影网

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.qmdy.me/vodshow/id/20/page/' + str(page) + '.html'
        fileUrl = 'https://www.qmdy.me'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
            title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
            url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('全民电影网  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
        title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
        img = tag.find('a', class_='myui-vodlist__thumb lazyload').get('data-original')
        url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
        des = tag.find('p', class_='text text-overflow text-muted hidden-xs').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    source = 13
    # 分多个模块，每个都需要单独查询出来
    # key分别为电影，连续剧，综艺，动漫
    moreType = {'20': 526, '21': 134, '22': 27, '23': 75}
    file_handle = open('dev/全民电影网.txt', mode='w')
    for type in moreType.keys():
        while page <= moreType.get(type):
            url = 'https://www.qmdy.me/vodshow/id/' + type + '/page/' + str(page) + '.html'
            fileUrl = 'https://www.qmdy.me'
            soup = NetControl.sendRequest(url)
            checkFilms(page, fileUrl, soup, file_handle, source)
            page += 1


if __name__ == '__main__':
    run()
