import pymysql
import logging

class PyDB:
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host="101.37.123.138",
            db='sell_db',
            port=3306,
            user="test_user",
            passwd="L6aDIc2oHOF0v#NOri",
            charset="utf8"
            )
        # 设置游标
        self.cur = self.connect.cursor()

    def query_sql(self,sql):
        # sql = "SELECT mobile FROM user_order where user_order_no = 'S20210310104112967WwlWqT'"
        # 执行查询语句
        self.cur.execute(sql)
        logging.debug(sql)
        return  self.cur.fetchall()


    def update_sql(self,sql):
        result = self.cur.execute(sql)
        self.connect.commit()

    def check_user(self,mob):
        '''查询订单的下单手机号'''
        result = self.query_sql("SELECT name FROM sell_admin where mobile = '{mob}'".format(mob))
        logging.debug(result)
        return result

    def upadate_user(self,mob):
        try:
            self.update_sql("update sell_admin set name='nee' where mobile ='{mob}'".format(mob))
        except Exception as e:
            self.connect.rollback()
            logging.debug(str(e))

    def add_user(self,mob):
        try:
            self.update_sql("insert sell_admin set name='nee' where mobile ='{mob}'".format(mob))
        except Exception as e:
            self.connect.rollback()
            logging.debug(str(e))

    def __del__(self):
        '''关闭数据库游标和连接'''
        self.cur.close()
        self.connect.close()

# 编辑数据库
# 删除数据

sql="SELECT mobile FROM user_order where user_order_no = 'S20210310104112967WwlWqT'"

ll = PyDB()
ll.query_sql(sql)
