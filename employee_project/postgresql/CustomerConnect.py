from employee_project.postgresql.connectRoot import DBConnection as con
import json
import  psycopg2
import logging
from employee_project.postgresql import DBObjects as dob
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
logger = logging.getLogger(__name__)

#Connects to customer Database
def GetCustomerConnect(cid):
    try:
        objcon=con.dbDetail()
        cur=objcon.cursor()
        logger.info("inside get customer connection details")
        cur.execute("Select  s.dbusername ,s.dbpassword ,s.dbname, d.dbserverip from customer s INNER JOIN dbservers d on s.dbserverid = d.dbserverid where s.custid = (%s)" ,[cid] )
        
        objcon.commit()
        print ( 'Data from joins fetched successfully.' )
        rows = cur.fetchall()
        
        dname = rows[0][2]
        logger.info(dname)
        uname = rows[0][0]
        pwd =rows[0][1]
        host= rows[0][3]
        
        return  psycopg2.connect(database= dname, user=uname, password=pwd, host=host, port="5432")
    except Exception as e:
        logger.error(e)
        return False
#Create a Customer Database           
def CreateCustomerDB (cid):
    try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            #fetch  db details of customer
            logger.info("inside get customer connection details")
            cur.execute("Select  s.dbusername ,s.dbpassword ,s.dbname, d.dbserverip from customer s INNER JOIN dbservers d on s.dbserverid = d.dbserverid where s.custid = (%s)" ,[cid] )
            
            objcon.commit()
            print ( 'Data from joins fetched successfully.' )
            rows = cur.fetchall()
            
            dname = rows[0][2]
            logger.info(dname)
            uname = rows[0][0]
            pwd =rows[0][1]
            host= rows[0][3]
            objcon.autocommit = True
            sqlCreateDatabase = "create database "+dname+";"
            query = " CREATE USER "+uname+" WITH ENCRYPTED PASSWORD '"+pwd+"' ; GRANT ALL PRIVILEGES ON DATABASE " +dname+ " TO " +uname+ ";"
            cur.execute(sqlCreateDatabase)
            cur.execute(query)
            conn = psycopg2.connect(database= dname, user=uname, password=pwd, host=host, port="5432")
            # objact = dob.Action()
            # objact.status= "processed"
            
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            conn.autocommit = True
            
            cursor.execute ("CREATE TABLE COMPANY( ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL)")
            logger.info("table created")
            if(rows.count == 0 ):
                return None
            
            
            if (objcon):

                objcon.close()
                print("\nThe connection is closed.")
            
            return 
            
    except Exception as e :
        logger.error(e)
        return None


