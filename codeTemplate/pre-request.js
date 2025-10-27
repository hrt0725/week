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