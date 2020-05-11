from random import randint
import pymysql


def select_nom():
    # 打开数据库连接
    db = pymysql.connect(host="localhost",user="debian-sys-maint",password="mysql",database="random_name" )
    
    # 使用cursor方法创建一个游标对象
    cursor = db.cursor()

    # 使用execute()方法执行SQL语句
    cursor.execute("SELECT * FROM NOM")

    #使用fetall()获取全部数据
    data = cursor.fetchall()

    #关闭游标和数据库的连接
    cursor.close()
    db.close()

    return data


def select_prenom():
    return '坤'


def index_generator(i):
    if i == 1:
        # 查询姓
        data = select_nom()
        print(data)
    elif i == 2:
        # 查询名
        return select_prenom()
        


def main():
    """主程序"""
    nom_list = list()

    for i in range(1,3):
        a = index_generator(i)
        nom_list.append(a)

    print('您的姓名是：{}{}'.format(nom_list[0], nom_list[1]))
    # print(nom_list)
    

if __name__ == '__main__':
    main()
