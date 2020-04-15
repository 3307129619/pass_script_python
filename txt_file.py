# coding=UTF-8
import pymysql;
import glob
import os

def read_File(path):
    data = [];
    cate = [path + '/' + x for x in os.listdir(path)]
    for path_temp in glob.glob(path + '/*.txt'):#一级目录
        print(path_temp);
        f1 = open(path_temp, 'r', encoding='gbk',errors='ignore')
        for eachLine in f1:
            str = eachLine.replace('\n', '').replace('\r', '').replace(' ', '').replace('\\', '').replace("'", '');
            data.append({'pass':str,'len':len(str)});
            if(len(data)>1000):
                createDb(data);
                data = [];
        f1.close()
    for idx, folder in enumerate(cate):#下级目录
        for im in glob.glob(folder + '/*.txt'):
            print(im,idx);
            f1 = open(im, 'r', encoding='gbk',errors='ignore')
            for eachLine in f1:
                str = eachLine.replace('\n', '').replace('\r', '').replace(' ', '').replace('\\', '').replace("'", '')
                data.append({'pass': str, 'len': len(str)});
                if (len(data) > 1000):
                    createDb(data);
                    data = [];
            f1.close()
    if (len(data)>0):
        createDb(data);

def createDb(data):
    temp_str = "";
    for i in data:
        temp_str += ",('{}','{}')".format(i['pass'],i['len']);
    sql = "insert ignore into cs_pass(`pass`,`str_count`)values{}".format(temp_str[1:]);
    cursor =db.cursor();
    try:
        cursor.execute(sql);
        db.commit()
    except BaseException as e:
        print(sql);
        print(e);
        db.rollback()

if __name__ == "__main__":
    path = './text'#目录地址
    db = pymysql.connect("127.0.0.1", "root", "123456.", ' cs')
    read_File(path);
    # 表结构：
    """
    CREATE TABLE `cs_pass` (
       `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
       `pass` varchar(150) DEFAULT NULL COMMENT '密码',
       `str_count` int(5) DEFAULT NULL COMMENT '字符串长度',
       PRIMARY KEY (`id`),
       UNIQUE KEY `pass` (`pass`) USING BTREE,
       KEY `count` (`str_count`) USING BTREE
     ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 
    """