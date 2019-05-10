# -*-coding:GBK -*-
import os
import logging
#路径配置
Basedir=os.path.abspath(os.path.dirname(__file__))#当前文件所在目录的绝对路径

#数据库配置

db_config='''{
    "host":"115.28.108.130",
    "port":"3306",
    "user":"test",
    "password":"123456",
    "db":"longtengserver"
}'''

#日志配置:level：日志级别，format:日志格式，datefmt日期格式 handers日志输出处理器
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s  [%(filename)s:%(lineno)d]  %(funcName)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    handlers=[
                        logging.StreamHandler(),#输出到屏幕
                        logging.FileHandler(os.path.join(Basedir,'log',"log.txt"),encoding="utf-8") #输出到文件

                    ]
                    )


email_config={
    "server":"smtp.qq.com",
    "user":"394973674@qq.com",
    "password":"pgwddpgocdafcagd",
    "body":"hi,测试报告",
    "Subject":"测试报告",
    "receiver":"394973674@qq.com"
}

#是否发邮件
is_send=True