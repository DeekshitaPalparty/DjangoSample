
from rest_framework.request import Request
from django.db import connection
from django.http import JsonResponse
from django.core import serializers as ser
from django.views.decorators.csrf import csrf_exempt
import logging 
from datetime import datetime
import json
from time import time
from employee_project.postgresql import DBObjects as dob
from employee_project.postgresql.Login import LOGIN as lf
from employee_project.Utilities import Util as ut
from employee_project.services import Responses as Lg
# import uuid 
# import mysql.connector
 
logger = logging.getLogger(__name__)
 
# @csrf_exempt
#validates user 
def EMPLOYEE_LOGIN_VALIDATE(request):
    login=json.loads(request.body)
    logger.info(login)
    if( (login['data']['username'] == '') or (login['data']['password']== '') ):
        return JsonResponse("enter valid credentials", safe =False)
    else:
        user = lf.Validate_Login(login['data']['username'],login['data']['password'])
        res = Lg.LoginResponse()
        if(user.lastname != ''):
            token = ut.token_generate({"username":login['data']['username']})
            res.status = '1'
            res.token = token['token']
            res.firstname = user.firstname
            res.lastname = user.lastname
            # logger.info(res.status)
            # logger.info(res.token)
            # logger.info(res.firstname)
            # logger.info(res.lastname)
            now = datetime.now()
            logger.info("token inside login validate")
            logger.info(res.token)
            # return JsonResponse(ser.serialize('json', res), safe=False)
            lf.session_entries(login['data']['username'],res.token,now,now)
            return JsonResponse(json.dumps(res.__dict__), safe =False)
        else:
            res.status ='0'
            res.message ='Invalid Credentials'
            return JsonResponse(json.dumps(res.__dict__), safe =False)

# @csrf_exempt  
#Update user password
def Update_info(request):    
    reset = json.loads(request.body)
    logger.info(reset)
    daobj=dob.User_details()
    daobj.user_id= reset['username']
    daobj.pwd= reset['newpassword']
    hashed = ut.hash_method(daobj.pwd) 
    logger.info(hashed)               
    if(lf.Reset_password(daobj.user_id ,hashed)) :
        return JsonResponse("Password resetting successful", safe =False)
    else:
        return JsonResponse("unsuccessful", safe =False) 

# @csrf_exempt  
# validation of session      
def Validate_session(token):
    # val = json.loads(request)
    res = Lg.LoginResponse()
    res.token = token
    logger.info("token in validate session")
    logger.info(res.token)
    last = lf.get_last_access(res.token)
    logger.info(last)
    logger.info("time fetched in validate login")
    now = datetime.now()
    time_duration = ut.date_diff_in_Seconds(last,now)
    logger.info(time_duration)
    if(time_duration > 3600):
        res.status = '-1'
        res.message = 'session expired'
        lf.delete_token(token)
        # return json.dumps(res.__dict__)
        return res.status
    else:
        lf.update_last_access(token)
        res.status = '2'
        res.message = 'session updated'
        # return json.dumps(res.__dict__)
        return res.status