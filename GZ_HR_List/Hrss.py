import requests
from GZ_HR_List import Parser
import time


# 广州人社局公布人员接口，返回html，获取返回的__VIEWSTATE value作为下次请求的参数
gz_pub_url = "http://gzrsj.hrssgz.gov.cn/vsgzpiapp01/GZPI/Gateway/PersonIntroducePublicity.aspx"

# 请求user-agent
userAgent = {'User-Agent':"Mozilla/5.0"}


# 请求参数
param = {}
page = 1
totalPage = 0;
# 人员序号
pepSort = 1

# 循环调用接口
def requestList(param):
    global page
    global totalPage
    global pepSort

    # 请求接口
    hrss = requests.post(gz_pub_url, data=param, headers=userAgent)
    # 解析HTMLhandler
    soup = Parser.handleFromHTML(hrss.text)
    # 拿到总共的页数
    if (totalPage == 0):
        totalPage = int(soup.find(id = 'PageCount').string)

    # 下次请求的参数获取
    nextParam = Parser.paramFrom(soup)
    page += 1
    nextParam['ToPage'] = page
    # 到最后一页，直接返回
    if (page > totalPage):
        return

    # 人员列表
    peps = Parser.publicListFrom(soup)
    for p in peps:
        print(pepSort,':',p['name'],p['company'],'||',p['department'],'||',p['start'],p['end'])
        pepSort = pepSort + 1

    time.sleep(1)
    requestList(nextParam);


# 首次调用接口
requestList(param);