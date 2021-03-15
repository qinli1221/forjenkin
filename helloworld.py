import unittest
import requests
from func.api_jiexi import get_Asc

'''
接口查询
excel读取
数据库读写删
邮件发送
测试报告
'''
class TestGoods(unittest.TestCase):
    url = "https://exmartapi.sdycsdyc.cn/api/goods/list"

    def test_orderby1(self):
        body = {"orderAsc": 2,"orderBy": 1,"cardFlag": 0}
        res = requests.post(url=self.url, json=body)
        (A,B) = get_Asc(res=res)
        # print(A,B)
        self.assertTrue(A>B)


    def test_orderAsc(self):
        body = {"orderAsc": 1,"orderBy": 1,"cardFlag": 0}
        res = requests.post(url=self.url, json=body)
        (A,B) = get_Asc(res=res)
        # print(A,B)
        self.assertTrue(A<B)

if __name__ == '__main__':
    unittest.main(verbosity=2)   # 运行所有用例