import os
from urllib import parse

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f7bc1188-c115-4b4a-a6ac-8d246bb646c0'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image123567'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'gVuMcqqgo9VrkcY3pTfN6hOPVLhpuHgbBeFyOewi1X+MqnFVrg2VnlmrJJITkLO/elrDcgtN3jKp+ASt3I5PfA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'python-db.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'python-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'admin123'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'admin@123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_SERVER + '/' + SQL_DATABASE + '?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server'
    params = parse.quote_plus \
    (r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:python-db.database.windows.net,1433;Database=admin123;Uid=admin123;Pwd=admin@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

    SQLALCHEMY_DATABASE_URI="mssql+pyodbc:///?odbc_connect={}".format(params)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "BVt8Q~g..doze24CKKkM1qzeEH2hwS.pHTjGecFh"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "c1ac018d-7679-4cbc-832f-af688c7b8309"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session