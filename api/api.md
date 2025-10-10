##### 接口测试

* 定义：脱离界面，模拟请求和响应，验证数据的传递交互
* 接口：API，GUI，CLI
* 接口测试的意义：
  * 前后端分离，系统架构的安全
  * 发现底层Bug，降低修复成本
  * 持续集成，提高测试效率
  * 覆盖边界异常等场景，提升系统稳定性；
  * 多重数据校验，保障接口安全

###### **接口分类：**

* 代码层面接口：系统模块内部，各个功能方法之间的逻辑相对独立的代码；
* 协议层面接口：各种协议，http，socket，webservice，telnet等进行通信交互的；
* 服务层面接口：不同应用程序之间的进行功能交互的接口；

##### 接口测试的流程：

* 接口需求分析
  * 分析接口文档中每个接口：功能、输入、输出、业务逻辑；
  * 输出接口测试场景（接口测试点）
* 接口测试用例设计
  * 按照接口用例模板格式，运用等价类、边界值等设计方法，依次完成每个接口场景的测试用例；
  * 输出，所有接口的测试用例；
* 环境及数据准备
  * 测试环境：集成测试环境；
  * 数据准备：验证单个接口测试场景的测试数据，接口自动化测试的批量数据；
* 脚本的编写
  * 借助接口工具（postman/jmeter/apifox）添加测试场景数据，生成脚本；
  * 使用python/java编写自动化测试脚本；
* 脚本执行
  * 对接口工具进行操作，单独执行每个接口用例；
  * 通过代码框架，一次性全面执行虽有接口用例；
* Bug跟踪回归
  * 发现的Bug提交到缺陷管理系统（禅道、jira）
  * 开发修复后对Bug再次回归验证；
* 接口测试报告
  * 对接口测试执行情况统计分析（接口用例：覆盖率、用例的执行率、用例通过率；Bug：数量、等级、修复率等）
  * 对接口测试情况进行评估和风险分析；

##### 接口测试用例

* 项目名称/模块名称
* 项目名称：会员注册接口 APP.User.Register
* 接口用例编号：
  * 由字母，数字，下划线、中横线构成；
  * 内容格式：项目名称_模块_接口_测试类型_编号
  * 举例：ECShop_Users_login_API_01
* 用例标题：描述当前的具体测试场景
  * 格式：验证登录接口_正常登录
  * 用例标题不能重复
* 请求方式：POST/GET/PUT/DELETE
  * 一个接口若支持多种请求方式，则用例中要分别验证；
* 请求URL：服务器地址+接口地址
  * 服务器地址：
    * 开发环境：dev开发环境
    * 集成环境：SIT 系统集成环境/sandBox 沙盒环境
    * 验收环境：PRE预发布环境、UAT验收环境
    * 生产环境：PRD线上环境
  * 接口地址：接口地址一般不变
    * 路径标识：/api/App/User/Register
  * 举例：http://192.168.1.2/ECS/api/App/User/Register
* 前置条件：测试当前接口所需要满足的要求；当前接口执行依赖其他接口；
* 请求参数：列出当前接口请求所需要的所有参数，包括必填，可选，默认值；
* 请求报文：将请求参数按照一定的报文格式进行组合；json/xml/text
* 返回报文：根据接口文档，**预期**应该返回的报文内容；注意报文的格式
* 结果验证：结果断言；从返回报文中选择一项或多项能够唯一证明接口请求成功；
  * 举例：ret=400,msg=客户端非法请求：缺少必要参数password
* 测试结果：实际结果；当前接口测试用例执行的结果；通过、失败；

##### 接口用例评审

* 评审方式：组内评审（测试组内部）、组外评审（产品、开发、测试）
* 评审内容：用例规范、用例覆盖率；

##### PostMan的使用

###### **使用**

* 工作区WorkSapce：用来创建不同的项目；
* 集合Collection：用来创建项目模块；
* 请求request：具体的接口
* 实例example：接口测试用例

###### **postman请求**

* get请求
  * 请求参数放在params
* post请求
  * 参数放在body-raw-json

**postman环境：便于接口测试用例在不同的服务器环境下进行测试用例**

###### **环境变量**

变量定义：global或environment环境中定义变量，在需要使用参数的位置使用{{var_name}}

* global全局变量：定义的变量在任何地方都能使用；
* Environment环境变量：在当前的测试环境下使用；
* collection变量；在当前集合中使用；
* 临时变量：在当前的请求中使用；

###### **PostMan请求结果断言**

* 获取请求响应结果

  * `pm.response.text()` 请求报文以字符串形式获取
  * `pm.response.json()` 请求报文以json格式获取
  * `pm.expect(pm.response.code).to.be.oneOf([201, 202]);`
* 请求应答码200

  ```javascript
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });
  ```
* 通过包含特定字符串

  ```javascript
  pm.test("包含字符串", function () {
      pm.expect(pm.response.text()).to.include('"err_code":0');
  });
  ```
* 通过具体字段取值判单

  ```javascript
  pm.test("json值判断", function () {
      var jsonData = pm.response.json();
      pm.expect(jsonData.data.err_code).to.eql(0);
  });
  ```
* 响应结果在指定列表中

  ```javascript
  pm.test("响应状态码在 [200,201, 202] 中", function () {
      pm.expect(pm.response.code).to.be.oneOf([200,201, 202]);
  });
  ```
* 验证响应头信息包含指定字段

  ```javascript
  pm.test("Content-Type is present", function () {
      pm.response.to.have.header("Content-Type");
  });
  ```
* 验证结构体是json格式

  ```javascript
  pm.test("验证结构体是json格式",function (){
       var jsondata = pm.response.json();
       pm.expect(jsondata).to.be.an("object")
  })
  ```
* 验证响应体数据类型:number，string，boolean，array

  ```javascript
  pm.test("验证结构体是json格式",function (){
       var jsondata = pm.response.json();
       pm.expect(jsondata.data.err_code).to.be.a("number")
  })
  ```
* 验证同一层级下的字段是否存在

  ```javascript
  pm.test("验证相应体中指定的字段存在",function (){
      pm.expect(pm.response.json().data).to.have.include.keys(["err_msg","err_code"])
  })
  ```
* postman接口关联pre-request

  * 对依赖的接口使用sendReqest()发送请求；
    * url
    * methed
    * body
      * mode：'raw'
      * raw：JSON.stringify()中填写以来接口的请求参数；
  * 对依赖接口返货的结果设置为环境变量
    * 获取需要关联的字段结果：pm. response.json().字段名
    * 设置环境变量pm.environment.set()：设置环境变量时，变量名不要与已存在的变量名冲突。
    * 接口关联：在当前接口的请求参数中，使用{{}}把变量引用进来。

  ```javascript
  try {
      const response = await pm.sendRequest({
          url: pm.environment.get("base_url") + "/api/App/User/Login",
          method: "POST",
          body: {
              mode: 'raw',
              raw: JSON.stringify({
                  "app_key": pm.globals.get("app_key"),
                  "username": pm.globals.get("username"),
                  "password": pm.globals.get("password")
              })
          }
      });
      console.log(response.json());
      var jsondata = response.json();
      pm.globals.set("uuid",jsondata.data.uuid);
      pm.globals.set("token",jsondata.data.token);
  } catch (err) {
      console.error(err);
  }

  ```

###### **参数化：CSV参数化：**

* 接口用例所需要的参数在CSV文件中用逗号分割，
* Postman参数中使用{0}引l用CSV中第一行的变量名；
* 断言中，使用pm.iterationData.get("varName")

###### **newman接口测试报告**

* newman安装：
  * 安装node.js
  * 安装newman：`npm install -g newman`
  * 安装reporthtml：`npm install -g report-html-export`
  * 检查安装：`newman -v`
* newman使用：
  * 从postman中到处批量执行的用例集合和环境数据；
  * 在cmd命令执行：`newman run`
    * `-n 5`：迭代次数
    * `-e 环境数据.json`
    * `-d 请求参数数据文件.csv`
    * `--reporters html`导出生成报告的格式；
    * `--reporter-html-export filename`

###### **接口Mock**

* 概念：在对某个接口进行测试时，该接口尚未实现或无法使用，可以通过Mock模拟该接口的输入和输出，使用输出的结果进行后续接口的测试；
* Mock接口过程：创建接口Mock服务；->输入模拟的请求参数和响应结果报文；->接口调用

##### **Fiddle抓包**

* 作用：在UI或接口出现错误的情况下，抓取分析请求的参数和返回的报文是否与需求一致，分析和定位Bug；

###### 分析问题

* 请求类型：Post请求，Get请求
* 应答码：2xx成功，3xx重定向，4xx客户端错误，5xx服务器错误。
* 请求地址：Host + URL

###### **Insector解析：**

* request请求：
  * header请求头
    * 请求方式，请求地址，请求协议
    * 请求头信息：
  * 请求内容：TextView，WebForm，Row，Json
* response响应
  * 响应报文：TextView，WebForm，Row，Json

###### Composer发送请求

* 对请求地址、接口重新发送请求验证响应结果；

###### **Filters请求过滤**

* 使用Host过滤
  * 内网过滤：show intranet 显示内网，show internet 显示外网
  * 隐藏或显示指定的Host过滤：列出需要显示或者隐藏的Host的IP地址或者域名地址，多个以分号分隔；
* 使用响应内容过滤
  * 通过响应应答码过滤
  * 通过响应内容的类型和大小过滤

###### **AutoResponser响应拦截**

* 对满足规则的的请求进行拦截，并返回指定的内容；

###### **请求信息的筛选QuickExec**

* 关键词查找筛选：?keyword
* 内容大小的筛选：>1000     <400
* 响应应答码筛选：=200
* Host名称筛选：@hostname
* 文件类型筛选：select类型：select image|css|html
* 打断点：
  * bpafter：对请求响应内容的进行断点；
    * bpafter + 关键词 进行拦截；
    * bpafter 放行
  * bps：响应状态码进行断点；
    * bps+状态码    进行拦截
    * bps  放行
  * bpm/bpv：请求方式进行断点
    * bpm+请求方式进行拦截
    * bpm  放行
  * bpu：请求URL进行断点
    * bpu + 路径   进行拦截
    * bpu 放行
  * 其它命令
    * cls/clear 清除记录
    * help 查看帮助文档
    * g/go放行断点

###### **代理使用-移动端：**

* 移动端和Fiddle所在的电脑处于同一网络；
* Fiddle设置：Tool->options->勾选 "allow Remote Computes to connect"，设置端口号：8000以上；
* 设置代理：移动端连接同一WIFI，并设置代理：IP地址（Fiddle所在电脑的局域网ip地址），端口号；
* 下载并安装证书：移动端的浏览器访问：ip地址+端口号；下载Fiddle安全证书；
* 安装证书：移动端系统自带的“安装证书"/"CA证书安装"；
* 使用抓包：移动端浏览器或者app访问，Fiddle验证捕获数据；

##### **HTTP请求应答码**

* 200系列；代表请求成功；
* 300系列；重定向

  * 301：临时重定向；
  * 302：永久重定向；
* 400系列；客户端错误

  * 403：权限拒绝访问；
  * 404：找不到网页；
* 500系列；服务器错误

  * 502：网关失败，拒绝访问；
  * 503：服务器故障，不可用；
