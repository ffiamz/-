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

def uuid2str(uuidhex):
    return str(uuidhex).replace('-','')


def create_group(info):
    sql_order = 'insert into model_group_user (group_id, name ,theme) values("%s", "%s", "%s")'
    gid = uuid2str(uuid.uuid4())
    cursor= con.cursor()
    try:
        ret = cursor.execute(sql_order % (gid, info[0], info[1]))
        con.commit()
    except :
        ret = -1
    cursor.close()
    uid = uuid2str(info[2])
    add_user_into_group((gid, uid, 'c'))
    return ret

def add_user_into_group(info):
    sql_order = 'insert into model_user_group_relation (group_id, user_id, status)'
    sql_order += 'values((select group_id from model_group_user where group_id="%s"), '
    sql_order += '(select user_id from model_user where user_id = "%s"), "%s")'
    print(sql_order % info)
    cursor = con.cursor()
    try:
        ret = cursor.execute(sql_order % info)
        con.commit()
    except:
        ret = -1
    cursor.close()
    return ret

def is_in_group(info):
    sql_order = 'select * from model_user_group_relation where user_id = %s and group_id = %s'
    print(sql_order % info)
    cursor = con.cursor()
    try:
        ret = cursor.execute(sql % info)
        con.commit()
    except:
        ret = None 
    cursor.close()
    return ret


def delete_group():
    pass

def remove_user_from_group():
    pass

def insert_blog_into_collection():
    pass

def remove_blog_into_collection():
    pass


