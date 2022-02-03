import json
import time
import requests as r


class DataRecord:
    """to record the data of bilibili"""
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.record = {}

    def get_follower(self):
        response = r.get(self.url)
        if response.status_code == 200:
            response_dict = response.json()
            response_dict = response_dict['data']['follower']
            return response_dict
        else:
            return 0

    def time_follower_dict(self):
        follower = DataRecord.get_follower(self)
        if len(self.record) != 0:
            self.record = {}
        self.record[time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())] = follower
        return self.record

bili_url = 'https://api.bilibili.com/x/relation/stat?vmid=401315430'
file_path = 'D:/BVideoFiles/22886883-星瞳_Official/record_fans_num.json'
'''get返回dict: {'code': 0, 'message': '0', 'ttl': 1,'data': {'mid': 401315430, 'following': 20, 'whisper': 0, 'black': 0,'follower': 160679}} '''

if __name__ == '__main__':
    count = 1
    Data = DataRecord(bili_url, file_path)
    while 1:
        if count:
            ctime = time.strftime("%S", time.localtime())
            if ctime == '00':
                count -= 1
        else:
            with open(file_path, 'r') as file:
                data_load = list(json.load(file))
                data_load.append(Data.time_follower_dict())
            with open(file_path, 'w') as f:
                json.dump(data_load, f, indent=4)
            time.sleep(600)