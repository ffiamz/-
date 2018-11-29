from django.db import connection as con
import uuid


def get_all_users():
    sql_order = 'select user_name,email,create_time from model_user'
    cursor = con.cursor()
    try:
        cursor.execute(sql_order)
        data = cursor.fetchall()
    except:
        data = None
    cursor.close()
    return data


def get_all_groups():
    sql_order = 'select * from model_group_user'
    cursor = con.cursor()
    try:
        cursor.execute(sql_order)
        data = cursor.fetchall()
    except:
        data = None
    cursor.close()
    return data

def create_group(info):
    sql_order = 'insert into model_group_user (group_id, name ,theme) values("%s", %s, %s)'
    print(sql_order % (str(uuid.uuid4()).replace('-',''), info[0], info[1]))
    cursor= con.cursor()
    try:
        ret = cursor.execute(sql_order % 
                (str(uuid.uuid4()).replace('-',''), info[0], info[1]))
        con.commit()
    except :
        ret = -1
    cursor.close()
    return ret


            

