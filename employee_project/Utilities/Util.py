from __future__ import unicode_literals
import bcrypt 
import logging
import jwt

from employee_project.postgresql.Login import LOGIN as ab
logger = logging.getLogger(__name__)    
# import os       
# Declaring sizesize= 5  
# # Using os.urandom() 
# methodresult= os.urandom(size)       
# # Print the random bytes string# Output will be different everytimeprint(result) 

def hash_method(pwd) :
    passencode = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    # s = '$2b$10$3euPcmQFCiblsZeEu5s7p'
    # salt = Convert.ToBase64String(s)
    hashed = bcrypt.hashpw(passencode, salt) 
    return hashed

def compare_hash(user_pwd , hash_pwd):
    logger.info("entered hashing")
    if(bcrypt.checkpw(user_pwd.encode('utf-8'),hash_pwd.encode('ascii'))):
        logger.info("compare hashing")
        return True 
    return False
    # a = bcrypt.checkpw(user_pwd.encode('utf-8'),b'$2b$12$Bcd4ZI5mkQkB/M0n70pF1eg0RpURmkT620VdKjY5usk/ZXtCbe0Mm')
    # return a

def token_generate(payload):
    
    logger.info(payload['username'])
    secret_key = "9AE3DACD7F4F31680D3F5415C458548E438C75CED4B6EFB91035D7680E05FD74"
    token = jwt.encode(payload,secret_key, algorithm='HS256')
    return {'token':token ,'payload':payload}



def date_diff_in_Seconds(dt2, dt1): 
    date2 = dt2.replace(microsecond=0)
    date1 = dt1.replace(microsecond=0)
   
    timedelta = date1 - date2
    return timedelta.days * 24 * 3600 + timedelta.seconds