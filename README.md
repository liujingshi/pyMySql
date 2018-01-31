# 利用pyMySql模块封装的数据库操作类

Python3.x

pip install pyMySql //需要安装pyMySql模块


使用方法:

improt MySql

mysql = MySql.MySql('数据库地址', '数据库用户名', '数据库密码', '数据库名') #创建数据库操作对象

print(mysql.query('select * from test where id = 1')) #查询一条记录 返回一个字典 失败返回False

print(mysql.queryAll('select * from test)) #查询全部记录 返回一个列表 失败返回False

print(mysql.getRowCount()) #得到查询结果数量

print(mysql.md5('admin')) #md5加密(utf-8)

mysql.exec('insert into test values(1)') #执行一条SQL语句 成功返回True 失败返回False
