import pymongo



#创建客户端
client = pymongo.MongoClient('localhost')
#建库
db = client['text1029']
# #建表
table = db['users']
#插入数据
# table.insert({'name':'老王'})
# table.insert({'name':'小华'})
#插入多条
# user1={'name':'小王','age':18}
# user2={'name':'大王','age':22}
# user3={'name':'老王','age':38}
# table.insert_many([user1,user2,user3])

#查询
user = table.find().limit(5).skip(5)
for i in user:
    print(i)