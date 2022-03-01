# coding:utf-8

import NetControl


# 美剧天堂

# 检查是否存在该电影,默认检查前10页
def checkTarget(filmName):
    page = 1
    targetUrl = ""
    maxPage = 10
    while page <= maxPage:
        baseUrl = 'https://www.meijutt.tv/' + str(page) + '_______.html'
        fileUrl = 'https://www.meijutt.tv'
        soup = NetControl.sendRequest(baseUrl)
        for tag in soup.find('div', class_='list3_cn_box ').find_all('div', class_='cn_box2'):
            title = tag.find('a').get('title')
            url = fileUrl + tag.find('a').get('href')
            if filmName == title:
                targetUrl = url
                break
        page += 1
    print ('美剧天堂  ' + '   地址: ' + str(targetUrl))


# 获取全部电影数据
def checkFilms(page, fileUrl, soup, file_handle, source):
    for tag in soup.find('div', class_='list3_cn_box').find_all('div', class_='cn_box2'):
        title = tag.find('a').get('title')
        img = tag.find('img', class_='list_pic').get('src')
        url = fileUrl + tag.find('a').get('href')
        des = ''
        file_handle.write(title + "---" + img + "---" + url + "---" + des + '---' + str(source) + '---0' + "\n")
        print (str(page) + '  ' + title + "   " + img + "  " + url + '   ' + des)


# 执行程序
def run():
    page = 1
    source = 21
    maxPage = 10
    file_handle = open('dev/美剧天堂.txt', mode='w')
    while page <= maxPage:
        url = 'https://www.meijutt.tv/' + str(page) + '_______.html'
        fileUrl = 'https://www.meijutt.tv'
        soup = NetControl.sendRequest(url)
        checkFilms(page, fileUrl, soup, file_handle, source)
        page += 1


if __name__ == '__main__':
    run()
