# 密码脚本

#### 项目介绍
使用python request模块访问进行爆破


# 需要使用模块：
1. requests
2. json
3. pymysql
4. time
5. glob
6. os

# 使用说明

* ######text -- 目录为密码目录该目录存放密码的txt
<br>

* ######txt_file.py -- 查找txt文件，并写入数据库
* ######需要修改：连接数据库账户密码、库等。需要指定要索引的txt文件目录地址
* ######执行方法：
        python txt_file.py
* ######pass_script.py -- 进行post，匹配密码
* ######需要修改：连接数据库账户密码、库等。
* ######共有两个方法，bmxit446 -- 使用ajax进行匹配，kunlungr--使用post进行匹配
* ######执行方法：
        python pass_script.py

### linux后台执行：
	nohup python 文件名 &

