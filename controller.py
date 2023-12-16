import sys
from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME
from datetime import datetime

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

def get_API():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon, wind, pm25, hum
            FROM IQAir
            WHERE id BEWTWEEN 291 AND 294
        """)
        result = [models.API(*row) for row in cs.fetchall()]

        # Modify the "ts" format
        for item in result:
            item.ts = item.ts.strftime('%Y-%m-%dT%H:%M')

            # Convert wind to float without the unit
            item.wind = float(item.wind.split()[0])

            # Convert hum to float without the unit
            item.hum = float(item.hum.split('%')[0])

        return result

def get_Location():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon
            FROM Location
            WHERE id BETWEEN 22 AND 34
            ORDER BY ts
        """)
        result = [models.Location(*row) for row in cs.fetchall()]

        # Modify the "ts" format
        for item in result:
            item.ts = item.ts.strftime('%Y-%m-%dT%H:%M')

        return result

def get_LocalPM():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, pm25
            FROM PMlocal
            WHERE id BETWEEN 306 AND 503
            ORDER BY ts
        """)
        result = [models.PMlocal(*row) for row in cs.fetchall()]

        # Modify the "ts" format
        for item in result:
            item.ts = item.ts.strftime('%Y-%m-%dT%H:%M')

        return result

def get_PMtoLocation():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DISTINCT Location.id, Location.ts, Location.lat, Location.lon, PMlocal.pm25
            FROM Location
            JOIN PMlocal ON DATE_FORMAT(Location.ts, '%Y-%m-%dT%H:%M') = DATE_FORMAT(PMlocal.ts, '%Y-%m-%dT%H:%M')
            WHERE Location.id BETWEEN 22 AND 34
            ORDER BY ts
        """)
        result = [models.PMtoLocation(*row) for row in cs.fetchall()]

        return result
