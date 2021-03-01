from employee_project.postgresql import DBObjects as dob
import collections
import logging
from employee_project.postgresql.connectRoot import DBConnection as con
import json
import psycopg2
from employee_project.postgresql import CustomerConnect as connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
logger = logging.getLogger(__name__)
class Customer_Info :
    #Fetches Data from dbservers
    def SELECT_DB():
            
                objcon=con.dbDetail()
                cur=objcon.cursor()
                
                cur.execute("SELECT dbserverid , dbserverip from dbservers ")
    
                rows = cur.fetchall()

                rowarray_list = []
                for row in rows:
                    t = (row[0],row[1])
                    rowarray_list.append(t)
                # logger.info(rowarray_list)
                j = json.dumps(rowarray_list)
                # logger.info(j)

                objects_list = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['dbseverid'] = row[0]
                    d['dbseverip'] = row[1]
                    # d[row[0]] =row[1]
                  
                    objects_list.append(d)
                j = json.dumps(objects_list)
                logger.info(j)
                # logger.info("logged j value")
                if(objcon):
                    objcon.close()
                    print("\nThe connection is closed.")
            
                return j
                print ( 'Data displayed successfully.' )
    #Adds Customer to Database
    def CUSTOMER_ADD_QUERY (daobj) :
        try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            
            cur.execute("INSERT INTO customer(custname,custaddress,dbserverid,dbname,dbusername,dbpassword) VALUES(%s, %s,%s, %s, %s,%s)",(daobj.custname, daobj.custaddress,daobj.dbserverid,daobj.dbname,daobj.dbusername,daobj.dbpassword) )
            
            
            objcon.commit()
            print ( 'Data entered successfully.' )
            cur.execute("SELECT custid from customer where custname = (%s)",[daobj.custname])
            rows =cur.fetchall()
            logger.info(rows)
            logger.info(str(rows))
            for row in rows:
                customer_id = row[0]
            if (objcon):

                objcon.close()
                print("\nThe connection is closed.")
            
            return customer_id
            
        except Exception as e :
            logger.error(e)
            return False
    # Adds Customer Id, Status to Actions Table
    def ACTION_ADD_QUERY (objact) :
        try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            
            logger.info("inside action add query method")
            cur.execute("INSERT INTO actions(customerid,status,remarks)VALUES(%s,%s, %s)",(objact.cid ,objact.status,objact.remarks) )
            
            objcon.commit()
            print ( 'Data entered successfully in actions.' )
            
            if (objcon):

                objcon.close()
                print("\nThe connection is closed.")
            
            return True
            
        except Exception as e :
            logger.error(e)
            return False
    #Update Status in dbservers
    def UPDATE_SERVER_QUERY(server_status,sid):
        try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            
            logger.info("inside update server info method")
            cur.execute("UPDATE dbservers set status = %s where dbserverid = (%s)",(server_status,sid) )
            
            objcon.commit()
            print ( 'Data Updated successfully in dbservers.' )
            
            if (objcon):

                objcon.close()
                print("\nThe connection is closed.")
            
            return True
            
        except Exception as e :
            logger.error(e)
            return False
    #Update status in Actions Table
    def UPDATE_ACTIONS_STATUS(status,cid):
        try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            
            logger.info("inside update actions status method")
            cur.execute("UPDATE actions set status = %s where customerid = (%s)",(status,cid) )
            
            objcon.commit()
            print ( 'Data Updated successfully in actions.' )
            
            if (objcon):

                objcon.close()
                print("\nThe connection is closed.")
            
            return True
            
        except Exception as e :
            logger.error(e)
            return False
    #Calls Database Creation and Updates Status
    def DBCreation(customer_id):
        #fetch
        #update
        #query for db creation
        try:
            logger.info("inside DBCreation")
            objcon= con.dbDetail()
            cur=objcon.cursor()
            objcon.autocommit = True
            objact = dob.Action()
            objact.status = "processing"
            Customer_Info.UPDATE_ACTIONS_STATUS(objact.status,customer_id)
            connect.CreateCustomerDB(customer_id)
            objact.status = "processed"
            Customer_Info.UPDATE_ACTIONS_STATUS(objact.status,customer_id)
            return True 
        except Exception as e :
            logger.error(e)
            return False

