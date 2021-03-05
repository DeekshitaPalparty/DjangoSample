import unittest
import  psycopg2
from employee_project.postgresql.connectRoot import DBConnection as con
from employee_project.postgresql.CustomerConnect import CreateCustomerDB as DBMethod
from employee_project.postgresql import DBObjects as dob
from employee_project.postgresql.Customer import Customer_Info as cf
class Test: 
    def test_CustomerAdd(self):
        daobj = dob.Customer()
        daobj.custid =115
        daobj.custname ='customertest'
        daobj.custaddress ='india'
        daobj.dbserverid =1
        daobj.dbname='testcustdb'
        daobj.dbusername='custtest'
        daobj.dbpassword='india123'
        objcon=con.dbDetail()
        cur=objcon.cursor()
        # cur.execute("INSERT INTO customer(custname,custaddress,dbserverid,dbname,dbusername,dbpassword) VALUES(%s, %s,%s, %s, %s,%s)",(daobj.custname, daobj.custaddress,daobj.dbserverid,daobj.dbname,daobj.dbusername,daobj.dbpassword) )
        self.assertTrue(cf.CUSTOMER_ADD_QUERY(daobj))
        objcon.commit()
        if (objcon):

            objcon.close()
            print("\nThe connection is closed.")

    if __name__ == '__main__':
        unittest.main()