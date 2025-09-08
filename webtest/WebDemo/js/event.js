//分数计算
function judgeLevel(condition) {
    let result;
    if (condition < 0 || condition > 100 || isNaN(condition)) {
        result = "分数输入错误";
    } else if (condition < 60) {
        result = `分数为:${condition}-等级:E`;
    } else if (condition < 70) {
        result = `分数为:${condition}-等级:D`;
    } else if (condition < 80) {
        result = `分数为:${condition}-等级:C`;
    } else if (condition < 90) {
        result = `分数为:${condition}-等级:B`;
    } else {
        result = `分数为:${condition}-等级:A`;
    }
    console.log(result);
    return result;
}

function judge() {
    let inputELE = document.getElementById('inputCT');
    let divELE = document.getElementById('judgeResult');
    let condition = Number.parseInt(inputELE.value);
    let pELE = document.createElement('p');
    pELE.innerHTML = judgeLevel(condition);
    divELE.appendChild(pELE);
}

function clearResult() {
    let divELE = document.getElementById('judgeResult');
    divELE.innerHTML = "";
    document.getElementById('inputCT').value = "";
}

function inputChange() {
    let inputELE = document.getElementById('inputCT');
    let condition = Number.parseInt(inputELE.value);
    if (condition < 0 || condition > 100) {
        inputELE.value = Math.floor(condition / 10);
    }
}

window.onload = () => {
    let menuELEs = document.getElementsByClassName("menu");
    for (const menuItem of menuELEs) {
        menuItem.addEventListener("click", () => {
            for (const menuItem of menuELEs) {
                switchHideById(menuItem.getAttribute('name'));
            }
            switchShowById(menuItem.getAttribute('name'))

        })
    }
}
function switchHideById(id) {
    document.getElementById(id).style.display = "none";
}
function switchShowById(id) {
    let element = document.getElementById(id);
    if (element.style.display == "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}



//计算器
function jsqBtn() {
    let inputELE = document.getElementById("jsqInput");
    let result = undefined;
    try {
        result = eval(inputELE.value);
        if (isNaN(result) || !isFinite(result)) {
            result = "无效的计算结果";
        }
    } catch (error) {
        result = "输入格式错误";
        console.log(error);
    }

    let resultItemELE = document.createElement("p");
    resultItemELE.textContent = `${inputELE.value} = ${result}`;
    document.getElementById("jsqResult").appendChild(resultItemELE);
}


//登录
function loginBtn() {
    let userNmae = document.getElementById("usernameInput").value;
    let password = document.getElementById("passwordInput").value;
    if (userNmae != "" || password != "") {
        if (userNmae.length >= 6 && userNmae.length <= 18 && password.length >= 6 && password.length <= 18) {
            if (password.includes("@") || password.includes("!") || password.includes("%") || password.includes("_")) {
                alert("校验完成");
            } else {
                alert("密码必须包含“@、!、%、_");
            }
        } else {
            alert("用户名和密码长度需大于6小于18");
        }
    } else {
        alert("用户名或密码不能为空");
    }
}
//用户名输入校验
function userNameOnInput() {
    let userNmae = document.getElementById("usernameInput").value;
    let userNmaeTipELE = document.getElementById("userNameVaildTip");
    if (userNmae != "") {
        if (userNmae.length >= 6 && userNmae.length <= 18) {
            userNmaeTipELE.textContent = "";
        } else {
            userNmaeTipELE.textContent = "用户名长度需大于6小于18";
        }
    } else {
        userNmaeTipELE.textContent = "用户名不能为空";
    }
}
function passowrdOnInput() {
    let password = document.getElementById("passwordInput").value;
    let passwordTipELE = document.getElementById("passwordVaildTip");
    if (password != "") {
        if (password.length >= 6 && password.length <= 18) {
            if (password.includes("@") || password.includes("!") || password.includes("%") || password.includes("_")) {
                passwordTipELE.textContent = "";
            } else {
                passwordTipELE.textContent = "密码必须包含“@、!、%、_";
            }
        } else {
            passwordTipELE.textContent = "用户名和密码长度需大于6小于18";
        }
    } else {
        passwordTipELE.textContent = "用户名或密码不能为空";
    }
}

//头像放大
function imgAvatarEnter() {
    let imgAvatarELE = document.getElementById("imgAvatar");
    imgAvatarELE.style.scale = 1.5;
}
function imgAvatarLeave() {
    let imgAvatarELE = document.getElementById("imgAvatar");
    imgAvatarELE.parentElement.style.scale = 1;
    imgAvatarELE.style.scale = 1;

}


//runCode
function runBtn() {
    let runCodeInputELE = document.getElementById("runCodeInput");
    let runCodeResultELE = document.getElementById("runCodeResult");
    let result;
    try {
        result = eval(runCodeInputELE.value);
        runCodeResultELE.value += result + "\n";
    } catch (error) {
        console.log(error);
        runCodeResultELE.value += error + "\n";
    }


}