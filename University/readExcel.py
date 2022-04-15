# -*- encoding:  utf-8 -*-
'''
Description: 
Author: xuequan
Date: 2022-04-11 15:55:00
'''

'''
读取高校xls文件，转换成json数据
'''


import xlrd
import json
import re

subjects = [
    {id: "01", name: "哲学"}
]


url = 'http://www.moe.gov.cn/'
desc = '据统计，截至2011年，共有112所高校进入《211工程》，39所高校进入《985工程》。此后，这两项工程均不再新增学校加入。教育部称，国家先后实施了《211工程》、《985工程》、《优势学科创新平台》和《特色重点学科项目》等重点项目，有效推动了我国高等教育整体水平的提升。今后，我国将进一步加强顶层设计，坚持中国特色，强调战略引领，突出绩效原则，鼓励改革创新，避免重复交叉，提高集成效益，统筹推进世界一流大学和一流学科建设。'
u211 = '《211工程》，即面向21世纪重点建设100所左右的高等学校和一批重点学科的建设工程。《211工程》于1995年由国务院批准后正式启动。《211工程》是新中国成立以来由国家立项在高等教育领域进行的规模最大、层次最高的重点建设工作，是中国政府实施《科教兴国》战略的重大举措，是国家《九五》期间提出的高等教育发展工程，也是高等教育事业的系统改革工程。'
u985 = '1998年5月4日，在庆祝北京大学建校一百周年大会上，江泽民同志表示：《为了实现现代化，中国要有若干所具有世界先进水平的一流大学。》中国教育部决定在实施《面向21世纪教育振兴行动计划》中，重点支持北京大学、清华大学等部分高等学校创建世界一流大学和高水平大学，并以江泽民同志在北京大学100周年校庆的讲话时间（1998年5月）命名为：《985工程》。'
university985 = ['北京大学', '中国人民大学', '清华大学', '北京航空航天大学', '北京理工大学', '中国农业大学', '北京师范大学', '中央民族大学', '南开大学天津大学', '大连理工大学', '东北大学', '吉林大学', '哈尔滨工业大学', '复旦大学', '同济大学', '上海交通大学', '华东师范大学', '南京大学',
                 '东南大学', '浙江大学', '中国科学技术大学', '厦门大学', '山东大学', '中国海洋大学', '武汉大学', '华中科技大学', '湖南大学', '中南大学', '国防科学技术大学', '中山大学', '华南理工大学', '四川大学', '电子科技大学', '重庆大学', '西安交通大学', '西北工业大学', '西北农林科技大学', '兰州大学']
university211 = ['北京大学', '北京工业大学', '北京化工大学', '北京中医药大学', '中央财经大学', '中央民族大学', '天津大学', '内蒙古大学', '大连海事大学', '哈尔滨工业大学', '复旦大学', '东华大学', '上海大学', '东南大学', '河海大学', '南京师范大学', '合肥工业大学', '山东大学', '武汉大学', '华中农业大学', '中南大学', '暨南大学', '海南大学', '中国人民大学', '北京航空航天大学', '北京邮电大学', '北京师范大学', '对外经济贸易大学', '中国政法大学', '天津医科大学', '辽宁大学', '吉林大学', '哈尔滨工程大学', '同济大学', '华东师范大学', '第二军医大学', '南京航空航天大学', '江南大学', '浙江大学', '厦门大学', '中国海洋大学', '华中科技大学', '华中师范大学', '湖南师范大学', '华南理工大学', '四川大学', '清华大学', '北京理工大学', '中国农业大学', '北京外国语大学', '北京体育大学', '华北电力大学', '河北工业大学', '大连理工大学', '延边大学',
                 '东北农业大学', '上海交通大学', '上海外国语大学', '南京大学', '南京理工大学', '南京农业大学', '安徽大学', '福州大学', '中国石油大学', '中国地质大学', '中南财经政法大学', '国防科学技术大学', '华南师范大学', '西南交通大学', '北京交通大学', '北京科技大学', '北京林业大学', '中国传媒大学', '中央音乐学院', '南开大学', '太原理工大学', '东北大学', '东北师范大学', '东北林业大学', '华东理工大学', '上海财经大学', '苏州大学', '中国矿业大学', '中国药科大学', '中国科学技术大学', '南昌大学', '郑州大学', '武汉理工大学', '湖南大学', '中山大学', '广西大学', '电子科技大学', '四川农业大学', '贵州大学', '西安交通大学', '西北农林科技大学', '青海大学', '西南财经大学', '云南大学', '西北工业大学', '陕西师范大学', '宁夏大学', '重庆大学', '西藏大学', '西安电子科技大学', '第四军医大学', '新疆大学', '西南大学', '西北大学', '长安大学', '兰州大学', '石河子大学']


def convert(filename="./University/university_20210930.xls"):
    book = xlrd.open_workbook(filename)
    sheets = book.sheets()
    result = {
        'province': [],
        'city': [],
        'university': []
    }
    for sheet in sheets:
        province_id = None
        city_id = None
        cities = []
        for row in range(0, sheet.nrows):
            if row < 3:
                continue
            for col in range(0, sheet.ncols):
                cell = sheet.cell(row, col)
                if col == 0 and cell.ctype == 1:
                    # 省份格式如: 河北省（121所）
                    if re.search(r"^\w+（\d+所）$", cell.value):
                        province_name = re.sub(r"（\d+所）", u'', cell.value)
                        province_id = getProvinceCode(province_name)
                        if province_id is None:
                            province_id = ""

                        province_obj = {
                            'id': province_id,
                            'name': province_name
                        }
                        if province_obj not in result['province']:
                            result['province'].append(province_obj)

                if col == 4 and cell.ctype == 1:
                    cid = None
                    if cell.value not in cities:
                        city_id = getCityCode(cell.value)
                        cities.append(cell.value)
                        city_obj = {
                            'id': city_id,
                            'name': cell.value,
                            'pid': province_id
                        }
                        result['city'].append(city_obj)
                        cid = city_id
                    else:
                        cid = cities.index(cell.value) + 1

                    result['university'].append({
                        'id': sheet.cell(row, 2).value,
                        'name': sheet.cell(row, 1).value,
                        'level': sheet.cell(row, 5).value,
                        'type': sheet.cell(row, 6).value or u'公办',
                        'cid': cid,
                        '985': '',
                        '211': '',
                        'd': ''
                    })
    print(len(result['university']))
    return result


def getProvinceCode(name='北京'):
    with open('./University/provinces.json', 'r') as f:
        # data = f.read().decode(encoding='gbk').encode(encoding='utf-8')
        provinces = json.load(f)
        for p in provinces:
            print(p['name'], name)
            if (p['name'] == name or p['name'].startswith(name)):
                return p['code']


def getCityCode(name='北京'):
    with open('./University/cities.json', 'r') as f:
        # data = f.read().decode(encoding='gbk').encode(encoding='utf-8')
        cities = json.load(f)
        for p in cities:
            print(p['name'], name)
            if (p['name'] == name or p['name'].startswith(name)):
                return p['code']


def save_json(json_data={}):
    if json_data:
        with open('./data.json', 'w') as f:
            f.write(json.dumps(json_data, ensure_ascii=False))


def main():
    pro = getProvinceCode('北京')
    print(pro)
    json_data = convert()
    save_json(json_data)


if __name__ == '__main__':
    main()
