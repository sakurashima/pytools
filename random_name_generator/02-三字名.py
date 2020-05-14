from random import randint
import pymysql


def select(sql):

    # 打开数据库连接
    db = pymysql.connect(host="localhost",user="debian-sys-maint",password="mysql",database="random_name" )
    
    # 使用cursor方法创建一个游标对象
    cursor = db.cursor()

    # 使用execute()方法执行SQL语句
    cursor.execute(sql)

    #使用fetall()获取全部数据
    data = cursor.fetchall()

    #关闭游标和数据库的连接
    cursor.close()
    db.close()
    
    return data


def select_nom():

    return select('select * from NOM')


def select_prenom():
    
    return select('select * from PRENOM')


def select_behind_name():
    
    return select('select * from BEHIND_NAME')


def index_generator(i):

    if i == 1:
        nom_list = list()
        # 查询姓,查询的结果是一个大元组里面的小元祖
        datas = select_nom()
        for data in datas:
            for i in data:
                nom_list.append(i[0])

        length_nom_list = len(nom_list)
        random_num = randint(0, length_nom_list-1)
        return nom_list[random_num]

    elif i == 2:
        # 查询名
        nom_list = list()
        datas = select_prenom()
        for data in datas:
            for i in data:
                nom_list.append(i[0])

        length_nom_list = len(nom_list)
        random_num = randint(0, length_nom_list-1)
        return nom_list[random_num]

    elif i == 3:

        nom_list = list()
        datas = select_behind_name()
        for data in datas:
            for i in data:
                nom_list.append(i[0])

        length_nom_list = len(nom_list)
        random_num = randint(0, length_nom_list-1)
        return nom_list[random_num]


def main():
    """主程序"""
    nom_list = list()

    for i in range(1,4):
        a = index_generator(i)
        nom_list.append(a)

    print('您的姓名是：{}{}{}'.format(nom_list[0], nom_list[1], nom_list[2]))
    # print(nom_list)
    

if __name__ == '__main__':
    main()
