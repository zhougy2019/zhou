# -*-coding:GBK -*-
import json
import logging

def json2dict(json_string):
    if json_string:
        try:
            return json.loads(json_string)
        except json.decoder.JSONDecodeError :
             logging.error("json格式错误：{}".format(json_string))