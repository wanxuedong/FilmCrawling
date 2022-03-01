# coding:utf-8

import NetControl


# 妮克动漫

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.nicotv.me/video/type3/------addtime-' + str(page) + '.html'
        fileUrl = 'http://www.nicotv.me'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
            title = tag.find('h2', class_='text-nowrap ff-text-right').find('a').get('title')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('妮克动漫  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='list-unstyled vod-item-img ff-img-215').find_all('li'):
        title = tag.find('h2', class_='text-nowrap ff-text-right').find('a').get('title')
        img = tag.find('img', class_='img-responsive img-thumbnail ff-img').get('data-original')
        url = fileUrl + tag.find('a').get('href')
        des = ''
        if None != tag.find('h4', class_='text-nowrap ff-text-right'):
            for list in tag.find('h4', class_='text-nowrap ff-text-right').find_all('a'):
                # 去掉换行符
                des += list.string.encode('UTF-8').replace("\r", "").replace("\n", "")
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    source = 19
    maxPage = 498
    file_handle = open('dev/妮克动漫.txt', mode='w')
    while page <= maxPage:
        url = 'http://www.nicotv.me/video/type3/------addtime-' + str(page) + '.html'
        fileUrl = 'http://www.nicotv.me'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
