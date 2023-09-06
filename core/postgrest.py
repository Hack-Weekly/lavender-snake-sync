import sys
import os
from psycopg2 import connect
from psycopg2.errors import OperationalError
from dotenv import load_dotenv
load_dotenv()

def is_available():
    try:
        connect(
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            dbname=os.environ.get("POSTGRES_DATABASE"),
        )
        return True
    except OperationalError:
        return False