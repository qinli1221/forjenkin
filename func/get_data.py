import xlrd
import openpyxl


def excel_to_data(filename,index):
    # 读取sheet表内容存入data_list
    wd = xlrd.open_workbook(filename)
    sh= wd.sheet_by_index(index)
    tit = sh.row_values(0)
    data_list = []
    for i in range(1,sh.nrows):
        val = sh.row_values(i)
        dic = dict(zip(tit,val))
        data_list.append(dic)
    return data_list

def get_data(data_list,case_name):
    '''根据case_name查找对应用例行数据，没有数据返回None'''
    for case in data_list:
        if case_name == case["case_name"]:
            return case

def read_excel(data):
    excel = openpyxl.load_workbook("")