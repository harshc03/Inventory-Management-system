from pymysql import *
from pymysql import cursors

class DatabaseHelper():
    USER = 'root'
    PASSWORD = 'HARSH'
    HOST = 'localhost'
    database = 'project'

    @classmethod
    def get_columns(cls, description):
        # column names are present as the first element of the collection,
        # hence extract the first element[0], create tuple & return it.
        return tuple(map(lambda x: x[0], description))

    @classmethod
    def get_data(cls, query, parameters=None) -> dict:# select * wali query aur return mei sirf 1 row chahiye
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor(cursor=cursors.DictCursor)
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query,parameters)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    @classmethod
    # returns me multiple rows as tuple inside a tuple
    def get_all_data(cls, query, parameters=None):
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor()
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query, parameters)
        result = cur.fetchall()
        # get me the column names of the data
        headers = DatabaseHelper.get_columns(cur.description)
        cur.close()
        conn.close()
        # add the columns as the first row of my data
        return (headers,) + result

    @classmethod
    # insert, update, delete
    def execute_query(cls, query, parameters=None):
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor()
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query, parameters)
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    # in clause, select query
    def get_all_data_multiple_input(cls, query, params):
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor()
        format_strings = ','.join(['%s'] * len(params))
        cur.execute(query % format_strings, params)
        result = cur.fetchall()
        # get me the column names of the data
        headers = DatabaseHelper.get_columns(cur.description)
        cur.close()
        conn.close()
        # add the columns as the first row of my data
        return (headers,) + result

    @classmethod
    #update table ,set, where
    def execute_all_data_multiple_input(cls, query, params):
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor()
        format_strings = ','.join(['%s'] * len(params))
        cur.execute(query % format_strings, params)
        conn.commit()
        cur.close()
        conn.close()
#
# if __name__ == '__main__':
#     def get_data_test():
#         print("get_data test")
#         query = "Select * from world.admin where AdminName=%s and AdminPassword=%s"
#         parameters = ('Ritesh','SGT')
#         res = DatabaseHelper.get_data(query, parameters)
#         print(res)
#
#     def get_all_data_test():
#         print("get_all_data test")
#         query = "Select * from world.foodmenu where FoodType=%s"
#         parameters = ('Starters')
#         res = DatabaseHelper.get_all_data(query, parameters)
#         print(res)
#
#     def get_all_data_multiple_input_test():
#         print("get_all_data_multiple_input_test test")
#         query = "Select * from world.foodmenu where FoodType in (%s)"
#         parameters = ('Starters', 'Desserts')
#         res = DatabaseHelper.get_all_data_multiple_input(query, parameters)
#         print(res)
#
#     def execute_query_test():
#         print("execute_query_test test")
#         query = "Insert into world.customers(customer_name,customer_password) values (%s,%s)"
#         parameters = ('dummy123', 'dummy456')
#         res = DatabaseHelper.execute_query(query, parameters)
#         print(res)
#
#     def execute_all_data_multiple_input_test():
#         print("execute_all_data_multiple_input test")
#         query = "Update world.customers set customer_gender='M' where customer_name in (%s)"
#         parameters = ('dummy123', 'mohit', 'abcd')
#         res = DatabaseHelper.execute_all_data_multiple_input(query, parameters)
#         print(res)
#
#     execute_all_data_multiple_input_test()
#
#
