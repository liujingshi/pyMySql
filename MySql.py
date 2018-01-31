import pymysql

class MySql:

    def __init__(self, loalhost, dbUsername, dbPassword, dbName):  # 构造函数链接数据库设置游标
        self._db = pymysql.connect(loalhost, dbUsername, dbPassword, dbName)
        self._mysqli = self._db.cursor()

    def exec(self, sql):  # 执行sql语句
        try:
            self._mysqli.execute(sql)
            self._db.commit()
            return True
        except:
            self._db.rollback()
            return False

    def _rowToDic(self, rows): #原记录转换为字典
        rowDic = {}
        fields = self._mysqli.description
        for i in range(0, len(fields)):
            rowDic[fields[i][0]] = rows[i]
        return rowDic

    def query(self, sql):  # 查询一条记录
        if self.exec(sql):
            row = self._mysqli.fetchone()
            row = self._rowToDic(row)
            return row
        else:
            return False

    def queryAll(self, sql):  # 查询全部记录
        if self.exec(sql):
            rows = self._mysqli.fetchall()
            rowList = []
            for row in rows:
                rowList.append(self._rowToDic(row))
            return rowList
        else:
            return False

    def getRowCount(self): #得到查询的结果数量
        return self._mysqli.rowcount

