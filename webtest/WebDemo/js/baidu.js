function toSearch(str) {
    var aELE = document.createElement("a");
    aELE.href = "https://www.baidu.com/s?wd=" + str;
    aELE.target = "_blank";
    aELE.click();
}

function searchBtn() {
    var inputValue = document.getElementById("searchInput").value;
    if (inputValue === "" || inputValue === null) {
        alert("请输入搜索内容");
        return;
    }
    document.getElementById("searchInput").value = "";
    toSearch(inputValue);
}

var hotSearchLists = [
    "习近平发表重要讲话", "九三阅兵全程回顾", "东风5C核导弹打击范围覆盖全球", "三支兵种首次亮相天安门广场", "歼-20S将彻底改变未来战场", "在天坛拍到了中式绝美同框", "咱们有飞飞飞不完的飞机了", "机器狼登场“无人化”作战时代到来新", "九三阅兵高清大图合集来了", "老战士起身敬礼场面看哭了",
    "机长驾驶运油-20A飞过天安门", "“安徽黄山地铁连接杭州”系谣言", "新华社出图了", "F61导弹亮相阅兵场", "歼35A歼20S歼20A震撼登场", "南山佩戴“共和国勋章”观礼", "最帅变阵！不是电影特效是中国军人", "导天花板来了", "新型“陆战之王”首亮相专家解读新", "“东风-5C”液体洲际战略核导弹亮相",
    "阅兵车牌号是1945和2025", "雷军现身阅兵观礼台", "感受80面战旗出场带来的压迫感", "军迷变军盲又兴奋又迷茫", "未来感十足！海上无人作战方队受", "轰6N战略轰炸机来了", "白求恩后人与斯诺后人在北京相遇", "海军方队平均年龄不到21岁", "轰炸机梯队压迫感拉满", "外交天团体育天团都现场看阅兵了"
]
var currhotPage = 0;
var pageSize = 10;

window.onload = function () {
    var hotSearchList = document.getElementById("hotSearchList");
    for (let index = currhotPage; index < pageSize; index++) {
        var li = document.createElement("li");
        li.addEventListener("click", function () {
            toSearch(hotSearchLists[index]);
        });
        li.textContent = hotSearchLists[index];
        hotSearchList.appendChild(li);
    }
}

function hotSearchRef() {
    if ((currhotPage + 1) * pageSize >= hotSearchLists.length) currhotPage = 0;
    else currhotPage++;
    var hotSearchList = document.getElementById("hotSearchList");
    hotSearchList.start = currhotPage * 10 + 1;
    hotSearchList.innerHTML = "";

    
    var endIndex = 0;
    if (currhotPage * pageSize + pageSize > hotSearchLists.length) endIndex = hotSearchLists.length;
    else endIndex = currhotPage * pageSize + pageSize;

    for (let index = currhotPage * pageSize; index < endIndex; index++) {
        var li = document.createElement("li");
        li.addEventListener("click", function () {
            toSearch(hotSearchLists[index]);
        });
        li.textContent = hotSearchLists[index];
        hotSearchList.appendChild(li);
    }
}

