'''
Description: 原神祈愿记录
Author: xuequan
Date: 2022-07-01 14:27:15
'''

'''
gacha_type: 祈愿类型 100 新手祈愿；200 常驻祈愿；301 角色活动祈愿； 302 武器活动祈愿
end_id: 上个列表最后一个元素id，没有的话为0
'''

import requests

url = "https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?authkey=cmZoEJDqfJ5OdWVMOLy5PgbP8WpSK73no8XqCxpvwI5tsCpACaDo386xpCkmLIEqapaU8CepSG2b2GGfHMb391e6x2c5DVTwsdWhkNJGBk%2bsMPI8sD9IZXC15b%2fu%2fBH774OME8kupF7mWJ2q4WCbqA2eva3qbusKeXEti3OT9g6fRwtsNahPEr4hmQ%2bVEc1q3w3GGfFcRNyukcDEm4cHn%2fUWVNnPtqSPiF6wZdT2tw8fiVO20jd6ap8wQ1uY3rqFa5vEic8EEpVmu9o%2bHFELMXEQ%2fkDbNVIDIrvLmi4%2bqYpw%2bZLViRZZOSK5yry2RrILVhHsbg9nTW649dB4xekKu6MDSeFObxyQ1Cc6WdQMoDgNoUo77wsTbJd42KW%2bvubu%2bg8%2b6z7D1wrGyrkU21uPOQJN72Vfy6Lg3AV72U%2baAbK5Qb4oYhoIx6XuTZnQyBNxr9wDoXEQpfAnLcxXkYULxdve9cjZHfS%2bXw73xQrJ6K%2bOe0VDZjmXEKVqT6i34cF3qw3p%2bsXxLRnO%2bZIxbLWvVq%2ftli04L8KwJ4kPzxFkFnPWOJYnU0iyb0EsyTkhm%2f9bxdwaFyPANkzEJZtCeAdyOPNvykeF7sTbvCqtuMVuJzoIqUI8MOz4%2bx8ZWFlLuDc3nPaXQeQp9hZPUkn1DEfBrIUS%2bcmC1NIx6Vq%2bXsigjHuR2AjQ%2fqvQfUd4MWXFt5yULr%2bQ0PK9%2bihHMuv8xwqSv80%2bYyTd7L8JQVySLTcdC5Qb4ST%2bDhMqG6tkQ63CVO1Yx6B1Jql0MqdzYiowl3xxhzFsf1Dd2IJPicnMIHqKTpJPBSvrUmcysSSXbdJSqCIF%2b7IYJbRzB%2f6L3zdOWeha9igwjTToquLZ%2btCraPAXMrtgHdMNhd%2fa15f3neC1Ig6E5x2nI1YQXf62UMwPeNh6Dy4H2kmh9JW%2f%2b8fv%2f5evkn0VWqQyYNOShtmq5qovI%2bYOifmcQ0p7FlZR1lHLdFstlOcNaDDUNFUHB129nBV6uzBWINtUL%2fFx5fPH9QMaBWDUsFFHq8yqt8kmoyAyh2aWfnqzuOCykpIXSeg0J1WFIjOH7DaHORKH4M7VdoGhNS2h%2bdTHeb8fduRVj5Cdh%2f967cJGKHCpvdTt4fZZNHseamJVGPTtLPOX5XMJ5N%2bUQrijiZRe7mBFS52B2RTySpnT%2bdqeB8%2bJ24V2%2f%2ftlqwKbiIr91UJAj7uHMGPFhtOZnI5OXmTMy1O9%2bAqbHf%2b3WkM14wQvdatpzOBPgcRz0GUsIX%2bboVdWCJZ0Rk16G77viDR5%2bmB%2bB0c0ndeW19KMtximg8eHs7yxoLcmpR9nzpEtXALhulgmmw7f7lvsw9jfX7K3tV%2f%2bv7pSC8THes9A24fULA%3d%3d"

authkey = "cmZoEJDqfJ5OdWVMOLy5PgbP8WpSK73no8XqCxpvwI5tsCpACaDo386xpCkmLIEqapaU8CepSG2b2GGfHMb391e6x2c5DVTwsdWhkNJGBk%2bsMPI8sD9IZXC15b%2fu%2fBH774OME8kupF7mWJ2q4WCbqA2eva3qbusKeXEti3OT9g6fRwtsNahPEr4hmQ%2bVEc1q3w3GGfFcRNyukcDEm4cHn%2fUWVNnPtqSPiF6wZdT2tw8fiVO20jd6ap8wQ1uY3rqFa5vEic8EEpVmu9o%2bHFELMXEQ%2fkDbNVIDIrvLmi4%2bqYpw%2bZLViRZZOSK5yry2RrILVhHsbg9nTW649dB4xekKu6MDSeFObxyQ1Cc6WdQMoDgNoUo77wsTbJd42KW%2bvubu%2bg8%2b6z7D1wrGyrkU21uPOQJN72Vfy6Lg3AV72U%2baAbK5Qb4oYhoIx6XuTZnQyBNxr9wDoXEQpfAnLcxXkYULxdve9cjZHfS%2bXw73xQrJ6K%2bOe0VDZjmXEKVqT6i34cF3qw3p%2bsXxLRnO%2bZIxbLWvVq%2ftli04L8KwJ4kPzxFkFnPWOJYnU0iyb0EsyTkhm%2f9bxdwaFyPANkzEJZtCeAdyOPNvykeF7sTbvCqtuMVuJzoIqUI8MOz4%2bx8ZWFlLuDc3nPaXQeQp9hZPUkn1DEfBrIUS%2bcmC1NIx6Vq%2bXsigjHuR2AjQ%2fqvQfUd4MWXFt5yULr%2bQ0PK9%2bihHMuv8xwqSv80%2bYyTd7L8JQVySLTcdC5Qb4ST%2bDhMqG6tkQ63CVO1Yx6B1Jql0MqdzYiowl3xxhzFsf1Dd2IJPicnMIHqKTpJPBSvrUmcysSSXbdJSqCIF%2b7IYJbRzB%2f6L3zdOWeha9igwjTToquLZ%2btCraPAXMrtgHdMNhd%2fa15f3neC1Ig6E5x2nI1YQXf62UMwPeNh6Dy4H2kmh9JW%2f%2b8fv%2f5evkn0VWqQyYNOShtmq5qovI%2bYOifmcQ0p7FlZR1lHLdFstlOcNaDDUNFUHB129nBV6uzBWINtUL%2fFx5fPH9QMaBWDUsFFHq8yqt8kmoyAyh2aWfnqzuOCykpIXSeg0J1WFIjOH7DaHORKH4M7VdoGhNS2h%2bdTHeb8fduRVj5Cdh%2f967cJGKHCpvdTt4fZZNHseamJVGPTtLPOX5XMJ5N%2bUQrijiZRe7mBFS52B2RTySpnT%2bdqeB8%2bJ24V2%2f%2ftlqwKbiIr91UJAj7uHMGPFhtOZnI5OXmTMy1O9%2bAqbHf%2b3WkM14wQvdatpzOBPgcRz0GUsIX%2bboVdWCJZ0Rk16G77viDR5%2bmB%2bB0c0ndeW19KMtximg8eHs7yxoLcmpR9nzpEtXALhulgmmw7f7lvsw9jfX7K3tV%2f%2bv7pSC8THes9A24fULA%3d%3d"
def getWish(type, page, endId):
    params = {
        'authkey_ver': '1',
        'sign_type': '2',
        'auth_appid': 'webview_gacha',
        'init_type': '200',
        'gacha_id': 'ebbfa80fdbc30f7cdfed84670d87c018950878',
        'timestamp': '1653954735',
        'lang': 'zh-cn',
        'device_type': 'mobile',
        'game_version': 'CNRELAndroid2.7.0_R8029328_S8227893_D8227893',
        'plat_type': 'android',
        'region': 'cn_gf01',
        'game_biz': 'hk4e_cn',
        'gacha_type': type,
        'page': page,
        'size': '20',
        'end_id': endId,
    }


    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }
    resp = requests.get(url, params=params, headers=header)
    print(resp.text)

getWish()
