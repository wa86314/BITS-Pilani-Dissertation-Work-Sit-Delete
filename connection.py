import pymysql

try:
    db_conn = pymysql.connect(
        host='localhost',
        user='bits',
        password='Bits@1234!',
        database='bits_stdu'
    )
except Exception as e:
    print(f"Exception: {e}")
