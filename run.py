# -*-coding:GBK -*-

import unittest
from lib.htmlrunner import HTMLTestRunner
from config import Basedir,is_send
import os
import logging
import click
from lib.e_mail import send_email


@click.command()
@click.option("--send",default="false",help="�Ƿ����ʼ�")
def run_all(send):
    suite=unittest.defaultTestLoader.discover(os.path.join(Basedir,"test_case"))
    report_file=os.path.join(Basedir,"report","report.html")
    logging.info("==========���Կ�ʼ==========")

    with open(report_file,"wb") as f:

         HTMLTestRunner(stream=f,title="���Ա���",description="�ӿڲ��Ա���" ).run(suite)
    logging.info("========== ���Խ���==========")


    if is_send and send=="true":
            send_email(report_file)
if __name__=="__main__":
    run_all()