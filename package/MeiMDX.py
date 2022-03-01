# coding:utf-8

import NetControl


# 蒙面大侠

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://mengmiandaxia.com/cate/2?page=' + str(page)
        fileUrl = 'https://mengmiandaxia.com'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
            title = tag.find('a', class_='stui-vodlist__thumb lazyload').get('title')
            url = tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('蒙面大侠  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('ul', class_='stui-vodlist clearfix').find_all('li'):
        title = tag.find('a', class_='stui-vodlist__thumb lazyload').get('title')
        img = tag.find('img', class_='cover-image').get('src')
        if img.startswith('//'):
            img = 'https:' + img
        url = tag.find('a', class_='stui-vodlist__thumb lazyload').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    maxPage = 186
    source = 11
    file_handle = open('dev/蒙面大侠.txt', mode='w')
    while page <= maxPage:
        url = 'https://mengmiandaxia.com/cate/2?page=' + str(page)
        fileUrl = 'https://mengmiandaxia.com'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
