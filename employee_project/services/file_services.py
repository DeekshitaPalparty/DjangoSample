import logging
from employee_project.services import Responses as Lg
import json
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage
import tempfile 
from employee_project.services import Responses as Lg
# import os
logger = logging.getLogger(__name__)
#uploads files from frontend
def File_handler(request) :
    parser_classes = (MultiPartParser, FormParser)
    folder = 'employee_project/media/'
    fs = request.FILES['fileContent']
    logger.info(fs)
    # my_file = FileSystemStorage(location=folder) #defaults to MEDIA_ROOT  
    file_name = default_storage.save(fs.name, fs)
    # fs = default_storage.open(file_name)
    file_url = default_storage.url(file_name)
    # file_stats = os.stat(fs)
    # size = file_stats.st_size / (1024 * 1024)
    # logger.info(size)
    # if(size > 30):
        #chuck code
    # fs.save()
    # destination = open('/Media/' + fs.name , 'wb+')
    # destination.close()
    res = Lg.FileResponse()
    res.url = file_url
    res.status = '3'
    res.message ='file uploaded'
    return JsonResponse(json.dumps(res.__dict__),safe = False)
# dividing files into chunks
def File_handler_chunks(request) :
    parser_classes = (MultiPartParser, FormParser)
    folder = 'employee_project/media/'
    if request.method =='POST':
        req = request.body
        logger.info(req)
        fs = request.FILES['file']
        # filename = str(request.FILES.getlist('file'))
        logger.info(fs)
        # logger.info(filename)
        fs.read()
        with open('employee_project/media/'+filename,'wb+') as destination:
            for chunk in fs.chunks():
                destination.write(chunk)

    
    res = Lg.FileResponse()
    res. upload_status = 'true'
    return JsonResponse(res.upload_status ,safe=False)
    