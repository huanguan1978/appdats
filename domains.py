#!/bin/env python3

import os
import json


domains = {
    'yhxq_gxzhenzhe_net':{
        'domain':'yhxq.gxzhenzhi.net',
        'homepage':'/front/',
        'loading':1,
        'expired':'2021-01-01 00:00:00',
        'buttoname':'探索星球',
        'siteicon':'/front/images/avatar.png',
        'sitename':'燕汇财富健康球',
        'sitedesc':'您养燕子一阵子燕子养您一辈子',
        'greeting':'作任务拿积分获云石建燕屋，欢迎探索国祥健康燕汇财富星球。',
        },
    }


filename = 'domains.json'
with open(filename, 'w') as f:
    json.dump(domains, f)


## https://raw.githubusercontent.com/hpu-spring87/ebooks/master/update.json
## https://raw.githubusercontent.com/huanguan1978/appdats/master/domains.json
