import hashlib
import pymysql.cursors

con = pymysql.connect(host="sdm173965400.my3w.com", port=3306, user="sdm173965400", password="523545286",
                      db="sdm173965400_db", charset='utf8', cursorclass=pymysql.cursors.DictCursor)

cursor = con.cursor()


def insert():
    sql = 'select max(`ID`) as "max"  from `ip`'

    cursor.execute(sql)
    result = cursor.fetchone();
    max = str((int((result['max'])) + 1)).encode("utf-8")
    m = hashlib.md5();
    m.update((max));
    m1=m.hexdigest()
    m.update(str(m1).encode("utf-8"));
    m2 = m.hexdigest()
    print(max);
    sql = "insert `ip` (`ip`,`count`,`server`,`cookies`) values ('%s','%s','%s','%s')" % ( m1, m1, m2, m2);
    print(sql)
    cursor.execute(sql);
    result = cursor.fetchone();
    print('运行结果 %s'%(result))


for i in range(1, 100000000000):
    insert();

con.close();
