import requests
import time
import json

categoryUrl = 'https://gaokao.chsi.com.cn/zyk/zybk/mlCategory/1050'
specialUrl = 'https://gaokao.chsi.com.cn/zyk/zybk/xkCategory'
specialityesByCategoryUrl = 'https://gaokao.chsi.com.cn/zyk/zybk/specialityesByCategory'

def fetchSubjects():
    # 获取学科门类
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
    r = requests.get(categoryUrl, headers=header)
    categoryRes = r.json()
    # 学科门类
    categorys = categoryRes['msg']
    allCategorys = []
    if len(categorys) <= 0:
        return
    for i, cate in enumerate(categorys):
        allCategorys.append({
            'code': cate['key'],
            'name': cate['name'],
            'children': []
        })
        id = cate['key']
        subSpecialUrl = specialUrl + '/' + id + '?_t=' + str(int(round(time.time() * 1000)))
        req = requests.get(subSpecialUrl, headers=header)
        # 二级学科
        specialList = req.json()['msg']
        time.sleep(0.5)
        # 请求二级学科下的所有专业
        for j, spec in enumerate(specialList):
            allCategorys[i]['children'].append({
                'code': spec['key'],
                'name': spec['name'],
                'children': []
            })
            allSpecialUrl = specialityesByCategoryUrl + '/' + spec['key'] + '?_t=' + str(int(round(time.time() * 1000)))
            req = requests.get(allSpecialUrl, headers=header)
            print(req.json())
            allCategorys[i]['children'][j]['children'].append(req.json()['msg'])
            time.sleep(0.4)
    save_json(allCategorys)
        
def save_json(json_data={}):
    if json_data:
        with open('./University/china_university_subjects.json', 'w') as f:
            f.write(json.dumps(json_data, ensure_ascii=False))


def main():
    fetchSubjects()

if __name__ == '__main__':
    main()