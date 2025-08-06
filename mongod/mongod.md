# 数据库操作

## 数据库

### 创建数据库

```
use dbname 
db.createCollections('colName')
```

### 删除数据库

```
use dbname
db.dropDatabase()
```

### 使用数据库

```
use dbname;
show collections;
```

### 创建集合

集合：固定集合-限制集合的存储空间和大小、非固定集合-不限制集合空间大小；

```
db.createCollections('goods')
```

### 固定集合：

* size:代表存储空间的大小，
* max:代表存储文档的个数；
* size和max任意达标就从新开始覆盖；

```
db.createCollection('orders',{'capped':true,'size':1024,'max':100})
```

### 判断集合类型

```
db.colName.isCapped()  --返回true
```

### 删除集合

```
db.colName.drop()  -- 返回true，删除成功
```

## 文档操作

### 插入文档

```
db.colName.insertOne({'name':'张三'，'age',18})  --插入一个
db.colName.insertMany([{'name':'张三'，'age',18},{'name':'李四'，'age',18}])  --插入多个
```

### 查看文档

```
db.colName.find()
```

### 条件查询

```
db.colName.find({'name':'张三'}) -- 单个条件
db.colName.find({'name':'张三','age':18}) -- 多个条件
db.users.find({$or:[{'username':'张三'},{'age':17}]})    -- or 查询
db.colName.find({'age':{$gt:18}}) -- 大于18     大于等于   $gte
db.colName.find({'age':{$lt:18}}) -- 小于18     小于等于   $lte
db.colName.find({'age':{$ne:18}}) -- 不等于18
```

### 查询条件算术比较

* $gt: 大于 >
* $lt: 小于 <
* $gte: 大于等于  >=
* $lte: 小于等于  <=
* $ne: 不等于  !=

### 模糊查询

$regex:'中'  ：包含‘中’

```
db.users.find({'username':{$regex:'张'}})
```

$regex:'^中' ：以‘中’开头的

```
db.users.find({'username':{$regex:'^张'}})
```

$regex:'中\$' ：以‘中’结尾的

```
db.users.find({'username':{$regex:'张$'}})
```

### 文档更新

```
-- 更新单个
db.users.updateOne({'age':18},{$set:{'username':'new name',age:20}})
-- 更新多个
db.users.updateMany({'age':18},{$set:{'username':'new name',age:20}})
```

### 文档删除

```
-- 删除单个
db.users.deleteOne({'age':18})
-- 删除多个
db.users.deleteMany({'age':18})
```

### 高级查询

```
db.users.aggregate()
```

* 查询：$match

  ```
  db.users.aggregate([
             {$match:{username:'李四'}},
             {$project:{username:1}}
  ])
  ```
  * $project：字段投影，查询显示的结果字段;字段名：1

    ```
    db.users.aggregate（[{$match:{uname:'张三'}},{$project:{uname:1,address:1}}])
    ```
    练习
  * 查询商品集合中的价格在200-500之间的商品的名称，分类和价格；

    ```
    db.products.aggregate([
               {$match:{price:{$gte:200,$lte:500}}},
               {$project:{name:1,stock:1,category:1}}
    ])
    ```
  * 查询商品集合中库存小于100的商品的名称，库存；

    ```
    db.products.aggregate([
    {match:{"stock":{match:{"stock":{lt:100}}},
    {$project:{'name':1,'stock':1}}
    ])
    ```
  * 查询用户集合中姓张的用户的姓名，手机号；

    ```
    db.users.aggregate([
    {$match:{name:{$regex:'^张'}}},
    {$project:{name:1,phone:1}}
    ])
    ```
  * 查询订单集合中，订单金额大于1000的商品的ID和用户ID；

    ```
    db.orders.aggregate(
    {match:{'totalAmount':{match:{'totalAmount':{gt:1000}}},
    {$project:{'userId':1}}
    )
    ```
  * 查询订单集合中商品数量大于1的订单编号，订单数量，订单金额；

  ```
  db.orders.aggregate([
    {$match:{'items.quantity':{$gt:1}}},
    {$project:{totalAmount:1}}
    ])
  ```
* 分组：$group

  ```
  db.products.aggregate([
    {$match:{price:{$gt:10000}}},
    {$group:{_id:'$category'}}
  ])
  ```
* 排序：$sort；1：升序；-1：降序

  ```
  db.products.aggregate([
    {match:{stock:{match:{stock:{gt:150}}},
    {$sort:{price:-1}}
  ])
  ```
* limit：$limit

  ```
  db.products.aggregate([
    {$match:{stock:{$gt:150}}},
    {$limit:3}
  ])
  ```
* 聚合函数：max,min,avg,sum

  ```
  db.products.aggregate([
    {$group:{
      _id:"$category",
      maxPrice:{$max:'price'},
      minPrice:{$min:'price'},
      avgPrice:{$avg:'price'}，
      totalStock:{$sum:'stock'}
    }}
  ])
  ```
  * 统计

  ```
  db.products.aggregate([
    {$group:{
      _id:"$category",
      num:{$sum:1}
    }}
  ])
  ```
  练习：

  查询华为品牌商品的类别及其数量，并按数量进行降序排列；

  ```
  db.products.aggregate([
    {$match:{brand:'华为'}},
    {$project:{category:1,stock:1}},
    {$sort:{stock:-1}}
  ])
  ```
  查询价格在4500以上的商品的名称，类别，并按价格进行降序排列；

  ```
  db.products.aggregate([
  {$match:{price:{$gt:4500}}},
  {$project:{name:1,category:1}},
  {$sort:{price:-1}}
  ])
  ```
  查询库存数量小于100且商品名称包含手机的商品的名称，类别，价格

  ```
  db.products.aggregate([
  {match:{match:{or: [
  {stock:{$lt:100}],
  {name:{Sregex:'Pro'}}
  1y.
  {$project: {name:1,category:1,price:1}}
  1)
  db.products.aggregate([
  {match:{match:{and:[{stock:{lt:100}},{name:{lt:100}},{name:{regex:'Pro'}}]}},
  {$project:{name:1,category:1,price:1}}
  1)
  ```
* 关联查询：$lookup

  ```
  {$lookup:{
       from:"",
       localField:'',
       foreignField:'',
       as:''
    }
  }
  ```
  * 查询张三所有购买的定金金额

  ```
  {$match:{name:'张三'}},
  {$lookup:{
  from:'orders'
  localfield:'_id',
  foreignField: "userId"
  as:"orderInfo"
  }}
  ])
  ```
  查询编号为"order_002"订单所包含的商品名称，分类价格；

  ```
  db.orders.aggregate([
    {$match:{_id:'order_002'}},
    {$lookup:{
      from:'products',
      localField:'items.productId',
      foreignField:'_id',
      as:'productInfo'
    }}
  ])
  ```
  查询购买订单总金额大于1000，且总金额进行排序取排名前5的用户的姓名，手机号；

  ```
  db.orders.aggregate([
  {$group:
  _id:'$userId',
  userTotalAmount:{$sum:'$totalAmount'}
  }，
  {$match:{userTotalAmount:{$gt:10ooo}}},
  {$sort:{userTotalAmount:-1}},
  {$limit:5},
  {$lookup:{
      from:'users',
      localField:'userId',
      foreignField:'_id',
      as:'userInfo' 		 
   }}
  {$project:{userInfo.name:1,userInfo.phone:1}}
  ])
  ```
