import pymysql


def main():
    no = int(input('要删除的部门编号：'))
    # 1.连接mysql数据库
    conn = pymysql.connect(host='47.96.6.227', port=13306, user='root', password='feifei.17', db='mysql-one', charset='utf8')
    try:
        # 2.获得游标对象
        with conn.cursor() as cursor:
            # 3.执行SQL得到结果
            result = cursor.execute(
                'delete from tb_dept where 编号=%s', (no, )
            )
            if result == 1:
                print('删除成功！')
            # 4.操作成功执行提交
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        # 5.操作失败执行回归
        conn.rollback()
    finally:
        # 6.关闭连接释放资源
        conn.close()
    #print(conn)

if __name__ == '__main__':
    main()

