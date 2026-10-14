from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import os
from unittest import result
from venv import logger
from fastapi import FastAPI,HTTPException 
from unittest.mock import MagicMock, patch


app = FastAPI()


@app.get("/products")
def get_products():
    import pymysql
    conn = None

    try:
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            connect_timeout=5
        )
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM products;")
            result = cursor.fetchall()
    except pymysql.MySQLError as e:
        logger.exception("MySQL error occurred")
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        if conn is not None:
            conn.close()
    return result


print("server running")
key = os.getenv("OPENAI_API_KEY")
if key:
    print("API KEY loaded")
else:
    print("API KEY missing")

@app.get("/hello")
def hello():
    return {"message": "version 2"}

@app.get("/health")
def health():
    return {"status": "ok"}
