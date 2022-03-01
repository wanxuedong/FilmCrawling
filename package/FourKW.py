# coding:utf-8

import NetControl


# 4K屋

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'http://www.kkkkwu.com/list-select-id-1-type--area--year--star--state--order-addtime-p-' + str(
            page) + '.html'
        fileUrl = 'http://www.kkkkwu.com'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='list-unstyled vod-item-img ff-img-215').find_all('li'):
            title = tag.find('img', class_='img-responsive img-thumbnail ff-img').get('alt')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('4k屋  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    if None == soup.find('ul', class_='list-unstyled vod-item-img ff-img-215'):
        return
    for tag in soup.find('ul', class_='list-unstyled vod-item-img ff-img-215').find_all('li'):
        title = tag.find('h2', class_='text-ellipsis text-mr-1').find('a').get('title')
        img = tag.find('img', class_='img-responsive img-thumbnail ff-img').get('data-original')
        url = fileUrl + tag.find('a').get('href')
        des = ''
        if None != tag.find('h4', class_='text-nowrap text-mr-1'):
            for name in tag.find('h4', class_='text-nowrap text-mr-1').find_all('a'):
                if None != name.string:
                    des += name.string.encode('UTF-8')
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")


# 执行程序
def run():
    page = 1
    maxPage = 1044
    source = 9
    file_handle = open('dev/4k屋.txt', mode='w')
    while page <= maxPage:
        url = 'http://www.kkkkwu.com/list-select-id-1-type--area--year--star--state--order-addtime-p-' + str(
            page) + '.html'
        fileUrl = 'http://www.kkkkwu.com'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
