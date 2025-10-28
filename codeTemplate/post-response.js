var jsondata = pm.response.json();
pm.globals.set("uuid", jsondata.data.uuid);
pm.globals.set("token", jsondata.data.token);

pm.test("状态码为200", function () {
    pm.response.to.have.status(200);
});

pm.test("响应状态码在 [200,201, 202] 中", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 201, 202]);
});

pm.test("是否包含字符串\"err_code\":0", function () {
    pm.expect(pm.response.text()).to.include('"err_code":0');
});

pm.test("json值判断", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.data.err_code).to.eql(0);
});

pm.test("响应时间是否小于200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("是否包含响应头:Content-Type", function () {
    pm.response.to.have.header("Content-Type");
});

pm.test("验证相应体中指定的字段存在", function () {
    pm.expect(pm.response.json().data).to.have.include.keys(["err_msg", "err_code"])
})

pm.test("判断是否有uuid字段", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.data).to.have.property("uuid")
});

pm.test("判断是否有token字段", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.data).to.have.property("token")
});

pm.test("判断是否有role字段", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.data).to.have.property("role")
});

console.log(pm.variables.get("aa"));