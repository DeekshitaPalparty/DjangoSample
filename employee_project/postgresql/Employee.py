from __future__ import unicode_literals
from employee_project.postgresql import DBObjects as dob
import collections
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.request import Request
from django.http import JsonResponse
import logging
from employee_project.postgresql.connectRoot import DBConnection as con
logger = logging.getLogger(__name__)

class EMPLOYEES:
    
    #Adds Employee to user_details table  
    def EMPLOYEE_ADD_QUERY(daobj):
        try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            
            cur.execute("INSERT INTO user_details(user_id,e_id,first_name,last_name,address,pwd) VALUES(%s, %s,%s, %s, %s,%s)",(daobj.user_id, daobj.e_id,daobj.first_name,daobj.last_name,daobj.address,daobj.pwd.decode('ascii')) )
            
            objcon.commit()
            print ( 'Data entered successfully.' )
            
            if (objcon):

                objcon.close()
                print("\nThe connection is closed.")
            
            return True
            
        except Exception as e :
            logger.error(e)
            return False
   
    #Fetches user details
    def SELECT_QUERY():
        
           
            objcon=con.dbDetail()
            cur=objcon.cursor()
            
            cur.execute("SELECT * from user_details ")
            
            print ( 'Data entered successfully.' )
            rows = cur.fetchall()

            rowarray_list = []
            for row in rows:
                t = (row[0], row[1], row[2], row[3], row[4],row[5])
                rowarray_list.append(t)
            # logger.info(rowarray_list)
            j = json.dumps(rowarray_list)
            # logger.info(j)

            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d['userid'] = row[0]
                d['employee_id'] = row[1]
                d['Firstname'] = row[2]
                d['Lastname'] = row[3]
                d['Address'] = row[4]
                objects_list.append(d)
            j = json.dumps(objects_list)
            logger.info("logged j value")
            if(objcon):
                objcon.close()
                print("\nThe connection is closed.")
        
            return j
            print ( 'Data displayed successfully.' )
         
    
            