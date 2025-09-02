**Web前端开发测试**

**Web基础**

**Web系统架构**

* B/S：浏览器服务器；通过浏览器访问Web应用服务器；
* C/S：客户端服务器；通过安装在PC/移动端的应用程序访问服务器：

常见Web应用平台：

* JAVA平台：Java + Linux/Unix + Oracle + Tomcat /JBoos;
* LAMP平台：PHP + Linux + MariaDB + Apache/Nginx;
* ASP.NET平台: ASP(C#/.NET) + Windows + SQLServer + IIS;

Web工作原理

* 工作过程：域名解析--> 发起TCP的3次握手--> 建立TCP连接后发起http请求--> 服务器响应
  http 请求，浏览器得到html代码--> 浏览器解析html代码，并请求html代码中的资源
  （如js、css、图片等）--> 浏览器对页面进行渲染呈现给用户
* HTTP请求建立连接：
  * TCP三次握手建立连接
  * TCP四次挥手关闭连接
* HTTP请求(post与get的区别)
  * |              | POST                  | GET                 |
    | ------------ | --------------------- | ------------------- |
    | 数据传递方式 | body中传输            | URL地址中传输       |
    | 数据传递大小 | 数据大小无限制        | 数据大小有限制      |
    | 数据传输安全 | body体中更安全        | URL中不安全         |
    | 业务本质     | 提交数据 (增删改业务) | 获取数据 (查询业务) |
* Cookie，Session、Token的区别
  * Cookie浏览器客户端缓存，通常用于缓存HTML，js,css,图片音视频等资源文件到本地，便于本地用户下次访问能够更快的获取响应；通过sessionid与服务器进行进行关联，判断是否过期失效；
  * Session服务器缓存，通常用于缓存高并发请求的数据信息，减少大量请求对数据库服务器的压力；
  * ken通信会话过程中用于身份认证识别；
* URL构成
  * 协议+ip/域名+端口+资源地址；
  * https://www.baidu.com:443/s?wd=python&name=harry.
  * DNS域名解析协议：用于域名和IP地址的映射；
  * 域名：三级域名
    * 顶级域名：.com商业公司.edu 教育高校.net网络机构，.org 非盈利机构组织.cn 中国
    * 二级域名：baiu.com   jd.com  企业机构等全网的唯一标识；
    * 三级域名：map.baidu.com   news.baidu.com 企业内部进行业务区分；

**Web服务和应用服务**

* Web服务：用于处理服务器的静态资源包括（HTML，CSS，JS）；比如Nginx服务器；
* 应用服务：用来处理业务逻辑数据交互；比如数据库服务器，订单服务器；

**服务器架构**

* 单体服务器
  * 项目的所有业务逻辑，数据存储，应用解析等服务全部部署在同一台服务上；
  * 适用于业务比较单一、服务用户群体较小；
* 分布式服务器
  * 把项目业务进行拆分，设置为若干独立的业务板块，应对用户的请求；
* 分布式集群服务器
  * 相同业务拆分后增加若干服务器，同时应对相同的业务请求；
* 微服务
  * 按照业务需要，把所有业务进行粒度更小的拆分，

**数据库服务**

* 数据库读写分离，一主多从；
* 缓存数据，Redis缓存非结构化的数据，Session少量的临时数据；

**Web前端开发基础**

**HTML基础**

* 概念：超文本标记语言；用结构化标签定义页面的架构；
* 常用标签
  * 结构标签
    * `<html>`定义页面主题结构，所有内容必须放在里面；
    * `<body>`定义页面正文主体，具体页面效果展示的内容标签；
    * `<head>`定义页面头信息，用来加载资源文件；
    * `<title>`页面的标题
  * 内容标签
    * `<p></p>`段落标签
    * `<img>`图片标签
    * `<a></a>` 超链接标签
    * `<button></button>`按钮
  * 文本表单类标签
    * form表单
      * 用于提交内容到服务器，
      * 必填属性：name：用于唯一标识表单；methed：post/get；action：后台服务器接收数据的地址
    * input输入框
      * 用来接收数据，必填属性：name，type，value
      * type：
        * text：普通文本
        * password：密码输入框
        * radio：单选项，默认选中checked
        * checkbox：复选框，默认选中checked
        * file：文件上传
        * submit：提交表单
        * reset：重置表单
        * date.datetime-local：日期时间
        * email：邮箱格式
        * tel：电话格式
    * select下拉菜单 `<select name='name'>`
      * 选项 ：`<option value=''>cd</option>`
      * 选项组：`<optgroup lable='group name'></optgroup>`
    * textarea文本域 `<textarea>`
      * 用来输入多行内容
        `<textarea name='nave'></textarea>`

**CSS基础**

**JavaScript基础**
