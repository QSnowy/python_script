
from bs4 import BeautifulSoup

# 解析人社局返回的HTML文件
def handleFromHTML(html):
    if (html is None):
        html='<html></html>'
    soup = BeautifulSoup(html)
    return soup


# 从handler中获取下次请求参数
def paramFrom(soup):
    param = {'__VIEWSTATE': '',
             '__VIEWSTATEGENERATOR': ''}

    # 找到HTML数据中的input标签,提取对应的value作为下次请求的参数
    for key in param.keys():
        el = soup.find(id=key);
        val = el.get('value')
        param[key] = val
    # 可以使用的参数：LinkButton1(跳转)，NextLBtn(下一页)
    param['__EVENTTARGET']='NextLBtn'
    return param

# 解析HTML中的人员信息
def publicListFrom(soup):

    # 人员信息数据key
    pepKeys = ['name', 'company', 'result', 'department', 'start', 'end']
    keyCount = len(pepKeys)
    sort = 0
    # 定义人员列表数组
    pepList = []
    # 遍历HTML数据list
    for tr in soup.find('table', class_='listtable'):
        for td in tr:
            if (td != '\n'):
                # 前六个是table的字段名，跳过。
                if (sort >= keyCount):
                    if (len(pepList) <= int(sort / 6) - 1):
                        pep = {}
                        pepList.append(pep)
                    pep = pepList[int(sort / 6) - 1]
                    key = pepKeys[sort % 6]
                    pep[key] = td.string
                sort += 1

    # 返回人员列表
    return  pepList


