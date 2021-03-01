import  psycopg2


class DBConnection:
    #Connects to Main Database
    @staticmethod
    def dbDetail():
            DB_NAME="postgres" 
            DB_USER="postgres"
            DB_PASS="Postgres123"
            DB_HOST="localhost"
            DB_PORT="5432"
            
            return psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
            print("Database mydb connected!!")

#     def dbAdminConnect(a,b,c,d,e):
#             DB_NAME=a
#             DB_USER="postgres"
#             DB_PASS="Postgres123"
#             DB_HOST="localhost"
#             DB_PORT="5432"
            
#             return psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
#             print("Database mydb connected!!")
    


            

