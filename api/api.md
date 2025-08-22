## 接口测试

* 定义：脱离界面，模拟请求和响应，验证数据的传递交互
* 接口：API，GUI，CLI
* 接口测试的意义：
  * 前后端分离，系统架构的安全
  * 发现底层Bug，降低修复成本
  * 持续集成，提高测试效率
  * 覆盖边界异常等场景，提升系统稳定性；
  * 多重数据校验，保障接口安全

**接口分类：**

* 代码层面接口：系统模块内部，各个功能方法之间的逻辑相对独立的代码；
* 协议层面接口：各种协议，http，socket，webservice，telnet等进行通信交互的；
* 服务层面接口：不同应用程序之间的进行功能交互的接口；

## 接口测试的流程：

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

## 接口测试用例

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

## 接口用例评审

* 评审方式：组内评审（测试组内部）、组外评审（产品、开发、测试）
* 评审内容：用例规范、用例覆盖率；

## PostMan的使用

**使用**

* 工作区WorkSapce：用来创建不同的项目；
* 集合Collection：用来创建项目模块；
* 请求request：具体的接口
* 实例example：接口测试用例

**postman请求**

* get请求
  * 请求参数放在params
* post请求
  * 参数放在body-raw-json

**postman环境：便于接口测试用例在不同的服务器环境下进行测试用例**

**环境变量**

变量定义：global或environment环境中定义变量，在需要使用参数的位置使用{{var_name}}

* global全局变量：定义的变量在任何地方都能使用；
* Environment环境变量：在当前的测试环境下使用；
* collection变量；在当前集合中使用；
* 临时变量：在当前的请求中使用；

**PostMan请求结果断言**

* 获取请求响应结果

  * `pm.response.test()` 请求报文以字符串形式获取
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

  ```javas
  pm.test("验证相应体中指定的字段存在",function (){
      pm.expect(pm.response.json().data).to.have.include.keys(["err_msg","err_code"])
  })
  ```
* postman接口关联pre-request

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

**HTTP请求应答码**

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
