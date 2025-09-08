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
  * 结构标签
    * 表格类型：`<table> <tr> <th> <td>`
    * 列表类型：`<ul> <ol> <li>`
    * 内嵌类型：`<frame> <iframe> <frameset>`
    * 容器类型：`<div> <span>`

**CSS基础**

**常见样式**

* 轮廓界面：width，height，border，background
* 文字样式：color,font-size,font-weight,font-family,text-align
  * color:字体颜色，颜色英文单词，6位RGB的16进制颜色值；color：#89d6e2；
  * font-size:字体大小;font-size:16px
  * font-weight:字体粗细；font-weight:bold/22px;
  * font-family:字体类型：font-family：'宋体，仿宋，微软雅黑'
  * text-align:文字对其方式：text-align:right/left/center
* 布局样式：float，margin，padding，clear
  * float：实现改变元素的dom流顺序，让div容器左右浮动；float:left/right
  * margin:外间距
  * padding：内间距
  * clear：清除前面浮动的影响

**样式使用**

* 行内样式：在标签内添加属性 style
  * `style="width:100%; height:120px; border: 1px solid red";`
* 内嵌样式：在 `<head>`标签中添加 `<style>`标签，内部通过样式选择器来定义；
  * 样式选择器
    * ID选择器：#head{}
    * 类选择器：.btn{}
    * 标签选择器：input{}

**JavaScript基础**

**js的使用**

* html中任意位置，内部使用 `<script> code.... </script>`
* 外部使用 `<script src="....."></script>`

**基础语法规则**

* 变量声明
  * var name='harry'
  * let age=18   定义可变变量
  * const sex='男'   定义不可变变量
* 变量定义规则：
  * 变量名称：可以字母、下划线、数字组成，不能纯数字，不能以数字开头；
  * 命名规则：可以是单个英文单词，拼英；多个单词组合用下划线连接；驼峰命名(testUserName)；
  * 不能使用系统自带的关键字命名；(比如：let，const，for，while)
  * 变量命名区分大小写；
* 变量类型
  * string 字符串：`address='四川成都锦江区'`
  * 数字类型number：`price=12.99，num=5`
  * 数组类型array：`let hobby = [1,2,3,4]`
  * 布尔类型bool：`let isYoung=true`
  * 对象类型object：
    ```javascript
    const person={
           name:"jieni",
           age:18,
           address:"四川成都"
    }
    ```
* 变量赋值
  * 常规赋值：let num=111;
  * 运算赋值：a+=1；a-=1；a*=5
* 条件运算
  * 算术比较：>，<，==，===，!=，>=，<=，
* 逻辑运算
  * &&：逻辑与，两个条件同时满足；
  * ||：逻辑或，两个条件满足其一，结果为真(true)，否则为假(false)；
  * !：逻辑非，条件取相反结果；

**流程控制语句**

* if条件判断
  * if(){  } else {  }
  * if(){} else if(){}  esle{}
  * demo
    ```javascript
            // 根据分数判断分数的等级，分数的取值范围1-100，成绩60分以下不及格E，60分以上为合格；
            // 90-100为优秀等级A，80-90为良好等级B，70-80等级C，60-70等级D；
            let condition = 90;
            if (condition < 1 || condition > 100) {
                console.log("分数输入错误");
            } else if (condition < 60) {
                console.log(`分数为:${condition}-等级:E`);
            } else if (condition < 70) {
                console.log(`分数为:${condition}-等级:D`);
            } else if (condition < 80) {
                console.log(`分数为:${condition}-等级:C`);
            } else if (condition < 90) {
                console.log(`分数为:${condition}-等级:B`);
            } else {
                console.log(`分数为:${condition}-等级:A`);
            }
    ```
* for循环
  * for (let index = 0; index < 100; index++) {}
  * for (const item of hobby) {} 从数组，集合，对象中遍历数据
* while循环
  ```javascript
   let i = 0
          let sum = 0;
          while (i < 10) {
              sum += i;
              i++;
          }
          console.log(sum);
  ```
* switch....case选择
  ```javascript
  let level = "A";
          switch (level) {
              case "A":
                  console.log("----优秀----");
                  break;
              case 'B':
                  console.log("----中等----");
                  break;
              case 'C':
                  console.log("----差----");
                  break;
              default:
                  console.log('----未知等级----');
                  break;
          }
  ```
* break,contiune
  * break:结束所有语句的执行；
  * contiune：结束当前的循环，进入下一次循环；

**函数和事件**

* 函数 function fname(){}
  * 函数定义：function funName(paramName){}
  * 函数调用：funcName(paramValue)
  * return;
* 事件
  * 常用事件：input、click、dbclick、mouseenter，mousout，mousehover、keydown、keyup
  * 触发事件：on+事件名
    * HTML标签中 使用触发事件的属性：onclick(函数名称)
* DOM操作
  * 获取页面元素；
  * 获取单一元素对象
    * `document.getElementById("chat-textarea")`
    * `document.getElementsByClassName("mnav c-font-normal c-color-t")[2]`
  * 获取元素列表
    * document.getElementsByName("username")
    * document.getElementsByClassName("divBox")
    * document.getElementsByTagName("li")
  * document.querySelector通过元素选择器获取
  * 获取单个
    * `document.querySelector("#box")`
    * `document.querySelectorAll(".box")[0]`
  * 获取多个：document.querySelectorAll
    * `document.querySelectorAll(".hotsearch")`
    * `document.querySelectorAll("#hotsearch-content-wrapper > li:nth-child(1) > a > span.title-content-title")`
* DOM操作 - 元素对象操作
  * 元素赋值：element.textContent="value'
