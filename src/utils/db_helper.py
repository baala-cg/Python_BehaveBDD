import pyodc as pyodc
from src.utils import config_reader

def connect_db():
    server = config_reader.read_config("DB Info","server")
    database = config_reader.read_config("DB Info","database")
    user = config_reader.read_config("DB Info","user")
    code = config_reader.read_config("DB Info","code")
    conn = pyodc.connect('DRIVER={SQL Server};SERVER=' +server+';DATABASE='+database+';ENCRYPT=yes;UID='+user+';PWD='+code)
    return conn

def get_dbdata_obdc(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor