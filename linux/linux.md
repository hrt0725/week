# Linux操作系统

## 虚拟环境

* CentOS 7 Linux操作系统；
* 虚拟机：VMware 17
* 客户端：XShell
* 服务器：CentOS 7版本的Linux；
* 客户端：XShell，Putty，SecureCRT（SSH协议）

## Linux操作系统

* 源于Unix操作系统，开源免费的；版本：RedHat，Ubuntu，CentOS；
* Linux：一切皆命令，一切皆文件。

### 基础概念

普通用户

```
[lan@landev root]$
```

root用户

```
[root@landev ~]#
```

* 切换用户： `su lan`
* pwd：查看当前路径，返回当前的绝对路径
* cd：切换目录，`cd 路径`
* ls：查看路径下的内容;

路径：

* 根路径：`cd  / ` 系统根目录
* 绝对路径：`cd /var/log`
* 相对路径：
* 当前路径：`cd ./`
* 上级路径：`cd ../../`
* 家路径：`cd ~`普通用户家目录/home/harry,  root用户的家目录：/root

辅助：

* history：查看当前会话的历史操作命令
* clear：清空屏幕

## 文件管理

* 文件夹/目录
  * 新建文件夹 `mkdir newDir newDir2 newDir3`可以创建单个或多个目录；
  * 创建层级目录：`mkdir -p db/oracle`
  * 删除目录：`rmdir 目录`
  * 删除层级目录：`rmdir -p db/mongodb/data`删除单层级目录，要求目录下为空
  * 删除目录及文件：`rm -rf dirName`
  * 查看目录：`ls 目录`   `ls -a`   `ls -A`   `ls -l`
* 文本文件
  * 创建文件：`touch fileName`
  * 修改文件：`vim fileName` 非编辑模式 i/a 进入编辑模式，ESC键退出编辑模式；`:wq`保存退出   `:q!`强制退出
  * 删除文件：`rm -rf fielName`
  * 查看文件：`cat/more/less/head/tail fileName`

    * `cat  fileName` 一次性查看文本内容
    * `more fileName` 分屏查看文本内容
    * `less fileName` 关键字查找文本内容
    * `head -n 10 fileName` 查看文本前10行内容
    * `tail -100f fileName` 动态查看最新100行记录
  * 文件复制/剪切

    * 复制： `cp -R 源路径 目标路径` 复制文件夹以及里面的内容要加 -R 参数
    * 剪切：`mv 源路径 目标路径`
  * 文件压缩解压 zip/tar 格式

    * zip压缩：`zip 压缩后文件.zip  源文件1  源文件2`
    * zip解压缩：`unzip fileName.zip`
    * tar压缩：`tar -zcvf fielName.tar.gz 源文件1 源文件2 源文件3`
    * tar解压缩：`tar -zxvf fileName.tar.gz`
  * 文件内容截取 cut

    * 举例：`cut -d ":" -f 1 fileName`
      * -d ":" 内容分割符号为":"
      * -f n 显示分割后内容的列
  * 动态输入文本内容：tee -a fileName

    * 管道（|）:将多个命令进行组合,将前一个命令的输出，作为后一个命令的输入；
    * 和管道（|）一起使用；`cat fileName | tee -a fileName`
  * 根据关键字查找文本：grep

    * `grep "keyWord" fileName`
  * grep：文本查找

    * -i：忽略大小写
    * -n：显示行号
    * -v：反向查找内容，查找非关键词的内容
    * -E：查找多个关键词 `grep -E "DO|Mu"`
    * -A num：向后多显示num行
    * -B num：向前多显示num行
  * sed：批量文本替换

    * 模糊查找关键字： `sed -i 's/log/exe/g' user.log`
    * 以关键字开头：`sed -i 's/^log/.exe/g' user.log`
    * 以关键字结尾：`sed -i 's/.log$/.exe/g' user.log`
    * 查找并插入：`sed -i "/hi/i goodmorning" users.log`
    * 查找并追加内容
      * `sed -i "/^-/a hi" user.log`
      * `sed -i "/hello/a hi" user.log`
    * 查找并删除
      * `sed -i "/hello/d" users.log`
      * `sed -e "3d" user.log`
    * 查找指定行 `sed -n "1,5p" user.log`
    * 多命令执行 -e
      `sed -e 's/user/user1/g' -e 's/linux/linux1/g' user.log`
  * awk：数据格式处理

    * 按照分隔符进行数据分割，并打印：
      `awk -F ":" '{print $1,$3}' passwd`
    * 对数据进行数据运算 (+   -    *   /)，(且：&&，或：||),条件判断、循环
      `awk -F ":" '(NR>2&&NR<6){sum+=$3;print $3,sum}' passwd`
  * grep、sed、awk的区别

    * grep侧重关键词查找
    * sed侧重文本修改
    * awk侧重内容提取计算
  * vim

    | 操作             | 解释                                             |
    | ---------------- | ------------------------------------------------ |
    | h,j,k,l          | 分别代表光标向：左下上下移动一个字符             |
    | ^                | 去到光标所在行的行首(第一个非空字符)             |
    | $                | 去到光标所在行的行尾                             |
    | gg               | 去到第一行的行首                                 |
    | G                | 去到最后一行的行首                               |
    | #G               | 指定去到第#行的行首(#为具体的数字)               |
    | yy               | 复制光标所在的行                                 |
    | #yy或y#y         | 从光标所在行向下复制#行(#为具体的数字)           |
    | p                | 从光标所在行的下一行开始粘贴(如果按行复制的内容) |
    | dd               | 删除光标所在的行                                 |
    | #dd或d#d         | 从光标所在行向下删除#行(#为具体的数字)           |
    | dw               | 删除光标所在的单词                               |
    | x                | 删除光标所在的字符                               |
    | u                | 撤销操作                                         |
    | /关键字          | 从光标所在处向后查找关键字                       |
    | :set nu          | 显示行号                                         |
    | :set nonu        | 取消显示行号                                     |
    | :set ic          | 忽略大小写                                       |
    | :%s/test/linux/g | 查找替换，全文查找test并将其替换成linux          |
    | :wq              | 保存退出                                         |
    | :q!              | 强制退出                                         |
    | ESC              | 切换到命令模式                                   |

## 用户管理

* 用户添加：`useradd username`
* 设置密码：`passwd username`
* 用户删除：`usedel -r username`
* 创建组：`groupadd gname`
* 设置组密码：`gpasswd gname`
* 删除组：`groupdel gname`
* 添加组成员：`gpasswd -a username gname`
* 重新设置多个组成员：`gpasswd -M user1,user2,gname`
* 删除组成员：`gpasswd -d username gname`
* 查看组成员：`getent group gname`
* 查看用户所属组：`id username`

## 权限管理

文件角色：

* 所有者：owner  u
* 组成员：group member  g
* 其他用户：others  o

文件权限：

* 读：read-r-4
* 写：write-w-2
* 执行：execute-x-1

赋予权限：chmod

* `chmod u|g|o+r|w|x fimename`
* `chmod ugo+rwx filename`
* `chmod 755 filename`
* `chmod -R 755 dirname`

改权限

* chown 更改文件所有者：`chown user filename`
* chgrp 更改文件所属组： `chgrp dev cpFile.sh`
* 同时更改用户及所属组：`chown -R ls:ls linux`
* sudo 临时使用root身份进行操作：
  * root进入visudo，把指定用户加入到sudoers
  * 普通用户加上sudo + 命令执行；

文件查找

* find -name：根据名字查找
  * 精确查找：`find /home -name "ab.log"`
  * 模糊查找：`find /home -name "ab*.log"`
* find -user：根据拥有者查找
  * `find /home -user username`
* find -type：根据文件类型查找 f - 普通文件  d - 目录文件
  * `find /home/harry -type f`
* find -size：根据文件大小查找 -10k 小于10k，+10M大于10M；
  * `find /home/harry -size +10M`
* find -mtime：根据文件修改时间查找 + 1：超过一天；-1：一天内
  * `find /home -mtime +1 -user ls`

系统管理

* 进程管理
  * 查看进程：
    * 查看当前系统进程：`ps -ef`
    * 查看所有用户执行的进程：`ps -aux`
  * 动态查看进程（实时查看）
    * top 实时更新查看进程
  * 结束进程：kill
    * `kill pid`
    * `kill -9 pid`：强制结束
  * 查看内存
    * free：当前查看
    * top：动态查看
* 服务管理：systemctl / service（centos 6.5以前版本）
  * 查看服务：`systemctl status network`
  * 启动服务：`systemctl start|restart network`
  * 关闭服务：`systemctl stop network`
  * `service network status|restart|stop`
  * 服务自启动：`enable|disable`
    * `statemctl enable network`：设置开机自启
    * `statemctl disable network`：关闭开机自启
    * `chkconfig network on|off`：系统命令设置服务自启动：on/off
* 网络管理
  * 查看ip：ifconfig  / ip addr
  * 查看网络连通：`ping ip|域名`
  * 查看端口：`netstat`
  * 查看路由：`route`
  * 防火墙关闭：
    * 查看防火墙：`systemctl status firewalld`
    * 关闭防火墙：`systemctl stop firewalld`
    * 启动防火墙：`systemctl start firewalld`
    * 重启防火墙：`systemctl restart firewalld`
  * 关机：`shutdown -h now`
  * 重启： `reboot`
* 磁盘管理
  * 查看系统信息：`uname -a`
  * 查看主机名：`hostname`
  * 查看当前路径每个文件大小：`du -h`
  * 查看整个系统磁盘使用情况：`df -h`
  * 硬盘挂载：`mount /dev/sad3 /data`
  * 写在硬盘：`umount /data`
  * 磁盘分区：`fdisk /dev/sda`
* 环境搭建
  * 安装器：yum；从系统镜像源下载并安装
    * 安装：`yum -y install`
    * 卸载：`yum -y remove`
    * 更新软件：`yum -y updata`
    * 换源：`wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo`
    * 清空所有缓存：`yum clean all`
    * 生成新的元数据缓存：`yum makecache`
    * 查看启用的yum源：`yum repolist enable`
  * 源码安装：make；从软件官网下载源码进行编译安装
    * 下载源码包：`wget http://.../..../abc.tar.gz`
    * 解压源码包：`tar -zxvf  abc.tar.gz`
    * 配置路径：`./configure --perfix=/user/local/abc`
    * 编译：`make`
    * 安装：`make install`
  * 二进制安装：rpm；从软件官网下载已经打包好的软件，进行安装
    * 下载rpm二进制包：curl http://..../....abc.rpm
    * 安装：`rpm -ivh abc.rpm`
    * 卸载：`rpm -e packageName`
    * 查看安装列表：`rpm -l`
    * 查看已安装软件：`rpm -qa packageName`
  * web服务安装（httpd）
    * httpd安装：
      * `yum install -y httpd httpd-devel php`
    * 查看并启动服务：
      * `systemctl status httpd`
      * `systemctl start httpd`
    * 验证：
      * 找到www的路径
      * 新建php文件
      * ip地址访问php文件
  * 防火墙放行80端口
    * 临时放行：`firewall-cmd --add-port=80/tcp`
    * 永久放行80端口：`firewall-cmd --zone=public --add-port=80/tcp --permanent`
    * 重新加载防火墙：`firewall-cmd --reload`
    * 验证端口是否已开放：`firewall-cmd --list-ports`
