from __future__ import unicode_literals
from employee_project.postgresql import DBObjects as dob
import collections
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.request import Request
from django.http import JsonResponse
import logging
from employee_project.postgresql.connectRoot import DBConnection as con
from employee_project.Utilities import Util as ut
from datetime import datetime

logger = logging.getLogger(__name__)    
class LOGIN:
 
    #Validates user checks for matching password
    def Validate_Login(userid,password):
        try:
            user = dob.User()
            objcon=con.dbDetail()
            cur=objcon.cursor()
            # query_select = ("SELECT * from user_details where user_id = '"+str(userid)+"'")
            logger.info("entered validate_login")
            cur.execute("SELECT * from user_details where user_id = (%s)" , [userid])
            # cur.execute(query_select)
            rows = cur.fetchall()
            logger.info(rows)
            logger.info("data fetched")
            rowarray_list = []
            for row in rows:
                
                if (ut.compare_hash(password,row[5])):
                    user.firstname = row[2]
                    user.lastname = row[3]
                    
                
            if (objcon):
                objcon.close()
                print("\nThe connection is closed.")
            return user
            
        except Exception as e :
            logger.error(e)
            return False
    # Reset password using update query   
    def Reset_password (userid,password):
        try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            # Sql = "UPDATE login_credentials SET p_word= (%s)  WHERE username = (%s)"
            # data = (password , username)
            # cur.execute(Sql, data)
            cur.execute("UPDATE user_details SET pwd= (%s)  WHERE user_id = (%s)",(password.decode('ascii'), userid))
            # cur.execute("UPDATE login_credentials SET p_word= '"+str(password).replace("'","''")+"'  WHERE username = '"+str(username)+"'")
            objcon.commit()
            print ( 'Data updated successfully.' )
            
            if (objcon):
                objcon.close()
                print("\nThe connection is closed.")
            return True
            
        except Exception as e :
            logger.error(e)
            return False
    # Adding into session entries table
    def session_entries(userid,token,time,last_time):
        try :
            objcon=con.dbDetail()
            cur=objcon.cursor()
            
            cur.execute("INSERT INTO session_details(u_id,token_issued,issued_time,last_accessed_time) VALUES(%s, %s,%s,%s)",(userid, token,time,last_time ))
            
            objcon.commit()
            print ( 'Data entered successfully.' )
            
            if (objcon):

                objcon.close()
                print("\nThe connection is closed.")
            
            return True
            
        except Exception as e :
            logger.error(e)
            return False
    #Deletion of token
    def delete_token(token):
        try:
            objcon=con.dbDetail()
            cur=objcon.cursor()
            logger.info("entered delete token")
            objcon=con.dbDetail()
            cur=objcon.cursor()
            cur.execute("Delete from session_details where token_issued =  '"+str(token)+"'")
            objcon.commit()
            logger.info("deleted")
            if (objcon):
                objcon.close()
                print("\nThe connection is closed.")
            
        except Exception as e :
            logger.error(e)
            return False 
    # Retriving last access for session
    def get_last_access(token):
        try :
            logger.info("entered get last access time")
            objcon=con.dbDetail()
            cur=objcon.cursor()
            logger.info("get last accessed")
            logger.info(token)
            
            # cur.execute("Select last_accessed_time from session_details where token =(%s)",(str(token)))
            cur.execute("Select last_accessed_time from session_details where token_issued = '"+str(token)+"'")
            rows = cur.fetchall()
            logger.info("fetched time")
            for row in rows:
                logger.info(row[0])
            if(objcon):
                objcon.close()
                print("\nThe connection is closed.")
            
                logger.info("returning time")
            return row[0]
            
        except Exception as e :
            logger.error(e)
            return False
    #updating last access for session
    def update_last_access(token):
        try:
            objcon = con.dbDetail()
            cur = objcon.cursor()
            logger.info("entered update last access")
            
            
            last_access = datetime.now()
            cur.execute("Update session_details set last_accessed_time = '"+str(last_access)+"' where token_issued ='"+str(token)+"'")
            
            objcon.commit()
            logger.info("updated successfully")
        
            if (objcon):
                objcon.close()
                print("\nThe connection is closed.")
        except Exception as e :
            logger.error(e)
            return False