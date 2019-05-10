# -*-coding:GBK -*-
import  unittest
import json
import requests
import logging
from ddt import ddt,data,unpack
from lib.excel import Excel
from  lib.db import DB
from lib.utils import json2dict

excel = Excel("接口测试用例.xls")
case_list = excel.get_sheet_data("绑定加油卡")


@ddt
class TestQueryFuelCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.db=DB()


    def test_query_fule_card_normal(self):
        #case_data=self.case_list[0]
        for case_data in self.case_list:
            method,url,data,expect=case_data[2],case_data[3],case_data[5],json2dict(case_data[7])

            res=requests.request(method,url)
            self.assertEqual(expect,res.json())

    @data(*case_list)
    def test_add_fuel_card(self,data):

        case_id,title=data[0],data[1]
        logging.info("执行第几条用例{}".format(case_id))
        method,url,header,data,expect=data[2],data[3],json2dict(data[4]),json2dict(data[5]),json2dict(data[7])
        print(url)
        logging.info("请求方法:{},url:{}".format(method,url))
        res=requests.request(method,url,headers=header,json=data)



    @classmethod
    def tearDownClass(cls) :
        cls.db.close()