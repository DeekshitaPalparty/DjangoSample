from rest_framework.request import Request
from django.db import connection
from django.http import JsonResponse
from django.core import serializers as ser
from django.views.decorators.csrf import csrf_exempt
import logging 
from django.core import serializers as ser
import json
from employee_project.postgresql import DBObjects as dob
from employee_project.postgresql.Customer import Customer_Info as cus
from employee_project.Utilities import Util as ut
from employee_project.services import Responses as Lg
from employee_project.services import login_service as service
logger = logging.getLogger(__name__)

#Handles request and sends available databases in response
def  Database_fetch(request):
    try:
        
        req = request.body
        logger.info(req)
        db_list = cus.SELECT_DB() 
        logger.info(db_list)
        
        return JsonResponse(db_list, safe =False)
        
    except Exception as e :
        
        logger.error(e)
        return JsonResponse("error occured",safe =False)
# Adds Customer through request data        
def Customer_info(request):
    try:
        cust = json.loads(request.body)
        logger.info(cust)
        daobj=dob.Customer ()
        daobj.custname = cust['CustomerName']
        daobj.custaddress =cust['CustomerAddress']
        daobj.dbserverid =cust['sid']
        daobj.dbname = cust['DBname']
        daobj.dbusername =cust['DBUsername']
        daobj.dbpassword =cust['DBPassword']
        
    
         
        if(daobj.custname == '') :
            return JsonResponse("Enter Valid details")
        else:
            objact = dob.Action()
            objserver = dob.DatabaseInfo()
            customer_id = cus.CUSTOMER_ADD_QUERY(daobj)
            logger.info(customer_id)
            if(customer_id != ''):
                logger.info("Fetched customer id")
                # objserver.dbserverid = daobj.dbserverid
                # objserver.status = "to be processed"
                objact.cid = customer_id
                objact.status ='to be processed'
                objact.remarks = 'none'
                cus.ACTION_ADD_QUERY(objact)
                logger.info("first update ")
                # cus.UPDATE_SERVER_QUERY(objserver.status,objserver.dbserverid)
                cus.DBCreation(customer_id)
                
                 
                # objserver.status= "processing"
                # logger.info("second update")
                # cus.UPDATE_SERVER_QUERY(objserver.status,objserver.dbserverid)
                return JsonResponse("customer added", safe =False)
            else:
                # ob_act.remarks ='error'
                # cus.ACTION_ADD_QUERY(ob_act.status)
                return JsonResponse("customer addition failed", safe =False) 
        
    except Exception as e :
        
        logger.error(e)
        return JsonResponse("error occured",safe =False)