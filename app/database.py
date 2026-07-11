import mysql.connector
from config import Config


def get_connection():
    return mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        port=Config.DB_PORT,
        ssl_disabled=True
    )


def get_servers():

    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM servers
        ORDER BY created_at DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data


def add_server(server):

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO servers
        (server_name,environment,operating_system,ip_address,owner,status)

        VALUES(%s,%s,%s,%s,%s,%s)

    """,

    (

        server["server_name"],
        server["environment"],
        server["operating_system"],
        server["ip_address"],
        server["owner"],
        server["status"]

    ))

    db.commit()

    cursor.close()
    db.close()


def delete_server(server_id):

    db = get_connection()

    cursor = db.cursor()

    cursor.execute(

        "DELETE FROM servers WHERE id=%s",

        (server_id,)

    )

    db.commit()

    cursor.close()

    db.close()


def dashboard_stats():

    db = get_connection()

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) total FROM servers")
    total = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) running FROM servers WHERE status='Running'")
    running = cursor.fetchone()["running"]

    cursor.execute("SELECT COUNT(*) production FROM servers WHERE environment='Production'")
    production = cursor.fetchone()["production"]

    cursor.execute("SELECT COUNT(*) development FROM servers WHERE environment='Development'")
    development = cursor.fetchone()["development"]

    cursor.close()
    db.close()

    return {

        "total":total,
        "running":running,
        "production":production,
        "development":development

    }