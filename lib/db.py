# -*-coding:GBK -*-
import pymysql
import logging
from config import db_config






class DB(object):
    def __init__(self):

        self.conn=pymysql.connect(host='115.28.108.130',
                                  port=3306,
                                  user='test',
                                  password='123456',
                                  db='longtengserver'
        )
        self.cur=self.conn.cursor()

    def execute(self,sql):
        logging.debug("ִ��sql:{}".format(sql))
        try:
            self.cur.execute(sql)

        except pymysql.err.ProgrammingError as ex:
            logging.error("sql�﷨����sql-{} ������Ϣ-����".format(sql,ex))

        except pymysql.err.InternalError as  ex:
            logging.error("sqlִ�д���sql-{} ������Ϣ-����".format(sql,ex))

        else:
            result=self.cur.fetchall()
            logging.debug("sql���ݽ����{}".format(result))


    def close(self):
        self.conn.close()



if __name__=='__main__':


    print(db_config)



