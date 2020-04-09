# 利用pyMySql模块封装的数据库操作类

Python3.x

pip install pyMySql //需要安装pyMySql模块

使用方法:

ljsmysql.py => 用法类似ThinkPHP

``` python
from ljsmysql import Ljsmysql

Ljsmysql.connect(localhost, username, password, dbname, encoding)  # 连接数据库

rst = Ljsmysql.table("user").select()

rst = Ljsmysql.table("user").where("id", 1).find()

rst = Ljsmysql.table("user").where("age", ">", 20).select()

rst = Ljsmysql.table("user").where({
    "name": "ljs",
    "age": 22
}).select()

rst = Ljsmysql.table("user").where([
    ["name", "Liushu"],
    ["age", ">", 20]
]).select()

rst = Ljsmysql.table("name", "like", "_s")

insert_id = Ljsmysql.table("user").insert({
    "name": "aaa",
    "age": 23
})

Ljsmysql.table("user").where("id", 1).update({
    "name": "ss",
    "age": 20
})

Ljsmysql.table("user").where("id", 1).delete()

rst = Ljsmysql.query("select * from user")

Ljsmysql.exec("delete from user")
Ljsmysql.db.commit()

```

MySql.py

``` python
import MySql

mysql = MySql.MySql('数据库地址', '数据库用户名', '数据库密码', '数据库名') #创建数据库操作对象

print(mysql.query('select * from test where id = 1')) #查询一条记录 返回一个字典 失败返回False

print(mysql.queryAll('select * from test)) #查询全部记录 返回一个列表 失败返回False

print(mysql.getRowCount()) #得到查询结果数量

print(mysql.md5('admin')) #md5加密(utf-8)

mysql.exec('insert into test values(1)') #执行一条SQL语句 成功返回True 失败返回False
```
