# coding:utf-8

import NetControl


# 暮光影视

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.muguangys.xyz/vodshow/' + type + '--------' + str(page) + '---.html'
        fileUrl = 'http://www.muguangys.xyz'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
            title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
            url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('暮光影视  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    if None == soup.find('ul', class_='myui-vodlist clearfix'):
        return
    for tag in soup.find('ul', class_='myui-vodlist clearfix').find_all('li'):
        title = tag.find('a', class_='myui-vodlist__thumb lazyload').get('title')
        img = tag.find('a', class_='myui-vodlist__thumb lazyload').get('data-original')
        if img.startswith('/upload/'):
            img = fileUrl + img
        url = fileUrl + tag.find('a', class_='myui-vodlist__thumb lazyload').get('href')
        des = tag.find('p', class_='text text-overflow text-muted hidden-xs').string.encode('UTF-8')
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    source = 15
    # 分多个模块，每个都需要单独查询出来
    # key分别为电影，连续剧，动漫
    moreType = {'1': 292, '2': 225, '4': 197}
    file_handle = open('dev/暮光影视.txt', mode='w')
    for type, maxPage in moreType.iteritems():
        page = 1
        while page <= maxPage:
            url = 'http://www.muguangys.xyz/vodshow/' + type + '--------' + str(page) + '---.html'
            fileUrl = 'http://www.muguangys.xyz'
            soup = NetControl.sendRequest(url)
            checkFilms(page, fileUrl, soup, file_handle, source)
            page += 1


if __name__ == '__main__':
    run()
