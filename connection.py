import pymysql

try:
    db_conn = pymysql.connect(
        host='172.203.219.73',
        user='bits',
        password='Bits@1234!',
        database='bits_stdu'
    )
except Exception as e:
    print(f"Exception: {e}")
