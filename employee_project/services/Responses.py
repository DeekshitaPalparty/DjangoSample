#standard responses
class BaseResponse:
  status = ''
  message =''
  
class LoginResponse (BaseResponse):
    token = ''
    firstname =''
    lastname =''
    
class FileResponse (BaseResponse) :
  title =''
  url = ''
  filecontent =''
  upload_status =''

