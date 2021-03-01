
from rest_framework.request import Request
from django.db import connection
from django.http import JsonResponse
from django.core import serializers as ser
from django.views.decorators.csrf import csrf_exempt
import logging 
from django.core import serializers as ser
import json
from employee_project.postgresql import DBObjects as dob
from employee_project.postgresql.Employee import EMPLOYEES as em
from employee_project.Utilities import Util as ut
from employee_project.services import Responses as Lg
from employee_project.services import login_service as service
logger = logging.getLogger(__name__)

# @csrf_exempt
#Adds employee through request data
def EMPLOYEE_ADD(request,id):
    emp=json.loads(request.body)
    logger.info(emp)
    # logger.info(emp['empid'])
    daobj=dob.User_details()
    daobj.user_id = emp['UserId']
    daobj.e_id = emp['EmployeeId']
    daobj.first_name =emp['Firstname']
    daobj.last_name= emp['Lastname']
    daobj.address=emp['Address']
    daobj.pwd = ut.hash_method(emp['Password'])
    # hashed = ut.hash_method(daobj.pwd) 
    
    if (em.EMPLOYEE_ADD_QUERY(daobj)) :
        return JsonResponse("employee added", safe =False)
    else:
        return JsonResponse("employee addition failed", safe =False) 

# @csrf_exempt
# displays employee details in the frontend
def  EMPLOYEE_FETCH(request):
    try:
        
        token = request.headers['token']
        logger.info(token)
        response = service.Validate_session(token)
        logger.info(response)
        # logger.info(response.status)
        # logger.info(response[0])
        logger.info("called validate session")
        if(response == '2' or response == ''):
            emp_list = em.SELECT_QUERY() 
            logger.info("fetched data")
            return JsonResponse(emp_list, safe =False)
        else:
            return JsonResponse(response, safe =False)
    except Exception as e :
        res = Lg.BaseResponse()
        res.status = '1'
        res.message = e
        logger.error(e)
        return JsonResponse(json.dumps(res.__dict__),safe =False)
        


  
       


                 

      
        
    
        