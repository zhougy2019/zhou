# -*-coding:GBK -*-
import os
import logging
#·������
Basedir=os.path.abspath(os.path.dirname(__file__))#��ǰ�ļ�����Ŀ¼�ľ���·��

#���ݿ�����

db_config='''{
    "host":"115.28.108.130",
    "port":"3306",
    "user":"test",
    "password":"123456",
    "db":"longtengserver"
}'''

#��־����:level����־����format:��־��ʽ��datefmt���ڸ�ʽ handers��־���������
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s  [%(filename)s:%(lineno)d]  %(funcName)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    handlers=[
                        logging.StreamHandler(),#�������Ļ
                        logging.FileHandler(os.path.join(Basedir,'log',"log.txt"),encoding="utf-8") #������ļ�

                    ]
                    )


email_config={
    "server":"smtp.qq.com",
    "user":"394973674@qq.com",
    "password":"pgwddpgocdafcagd",
    "body":"hi,���Ա���",
    "Subject":"���Ա���",
    "receiver":"394973674@qq.com"
}

#�Ƿ��ʼ�
is_send=True