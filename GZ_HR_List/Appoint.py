# 广州天河人才入户服务预约中心

import requests
import json

# 请求地址
businessUrl = 'http://thzwb.thnet.gov.cn/thyy/api/zwyy/getBusiness'
appointUrl = 'http://thzwb.thnet.gov.cn/thyy/api/zwyy/getAppointment'
'4330E611EF0C70C0F60B12DDD5750180'

# sign
sign = '08a1512c0c17ee83988a7b2deeea92e1'
appointSign = '6e502f21324b3c3a9ed3124c9fa87b33'

# 请求参数
parm = {"fwdt_code":"GZTHRCDT","DeptName":"天河区人才服务管理办公室","_level":1,"_sign":sign}
appointParm = {"fwdt_code":"GZTHRCDT","ITEM_CODE":"440106-976-FW-001-02","BizID":"7007","_level":1,"_sign":appointSign}


# 开始请求预约接口
{
        "TimeConfig": [
            {
                "YYSTime": "08:30",
                "code": "2B96B96F1DA604B3061243BFF9EA6B1E",
                "leftYYCount": 0,
                "YYMax": 8,
                "YYETime": "09:30"
            }
        ],
        "Week": "1",
        "Date": "2019-07-01"
    }

appointRes = requests.post(appointUrl, data=appointParm)
parsed = json.loads(appointRes.text)

rows = parsed['rows']
for day in rows:
    # 解析每一天的预约时间段
    configs = day['TimeConfig']
    for conf in configs:
        leftCount = conf['leftYYCount']
        if leftCount > 0:
            print('可预约时间：',day['Date'],'周',day['Week'],'；','时间段：',conf['YYSTime'],'-',conf['YYETime'])

