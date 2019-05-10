import xlrd
import os
from config import Basedir

class Excel(object):
    def __init__(self,file_name):
        file_path=os.path.join(Basedir,"data",file_name)

        self.wb=xlrd.open_workbook(file_path)

    def get_sheet_data(self,sheet_name):
        sh=self.wb.sheet_by_name(sheet_name)
        # case_list=[]
        # for i in range(1,sh.nrows):
        #     case_list.append(sh.row_values(i))
        return [sh.row_values(i) for i in range(1,sh.nrows)]