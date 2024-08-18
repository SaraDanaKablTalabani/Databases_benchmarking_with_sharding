Config Servers (mongo_config1, mongo_config2, mongo_config3): These are essential for the sharded cluster to manage metadata. They form a replica set named configReplSet.

Router (mongo_mongos): Acts as a query router for the sharded cluster, connecting to the config servers.

Shard Servers (mongo_db1 to mongo_db6): Each forms a replica set and is marked as a shard server.

Mongo Express (mongo_express): Provides a web-based MongoDB admin interface connected to the mongos router.

Lebels

sudo docker node update --label-add mongo.config=1 pc0

sudo docker node update --label-add mongo.config=2 pc1

sudo docker node update --label-add mongo.config=3 pc2

sudo docker node update --label-add mongo.shard=1 pc3

sudo docker node update --label-add mongo.shard=2 pc4

sudo docker node update --label-add mongo.shard=3 pc20

sudo docker node update --label-add mongo.shard=4 pc21

sudo docker node update --label-add mongo.shard=5 pc22

sudo docker node update --label-add mongo.shard=6 pc23


docker stack deploy -c docker-compose.yml mongo_cluster

Initialization

Initialize Config Servers:

Connect to one of the config servers and initiate the replica set:

docker exec -it <config_server_container> mongo --port 27019

In the Mongo shell:

rs.initiate({
  _id: "configReplSet",
  configsvr: true,
  members: [
    { _id: 0, host: "mongo_config1:27019" },
    { _id: 1, host: "mongo_config2:27020" },
    { _id: 2, host: "mongo_config3:27021" }
  ]
})

Initialize Shards:

Connect to each shard and initiate their replica sets:

docker exec -it <shard_container> mongo --port <shard_port>


In the Mongo shell:

rs.initiate({
  _id: "shardReplSet1",
  members: [{ _id: 0, host: "mongo_db1:27018" }]
})

rs.initiate({
  _id: "shardReplSet2",
  members: [{ _id: 0, host: "mongo_db2:27022" }]
})

rs.initiate({
  _id: "shardReplSet3",
  members: [{ _id: 0, host: "mongo_db3:27023" }]
})

rs.initiate({
  _id: "shardReplSet4",
  members: [{ _id: 0, host: "mongo_db4:27024" }]
})

rs.initiate({
  _id: "shardReplSet5",
  members: [{ _id: 0, host: "mongo_db5:27025" }]
})

rs.initiate({
  _id: "shardReplSet6",
  members: [{ _id: 0, host: "mongo_db6:27026" }]
})


Add Shards to the Cluster:

Connect to the mongos router:

docker exec -it <mongos_container> mongo

In the Mongo shell:

sh.addShard("shardReplSet1/mongo_db1:27018")

sh.addShard("shardReplSet2/mongo_db2:27022")

sh.addShard("shardReplSet3/mongo_db3:27023")

sh.addShard("shardReplSet4/mongo_db4:27024")

sh.addShard("shardReplSet5/mongo_db5:27025")

sh.addShard("shardReplSet6/mongo_db6:27026")

with this setup we have a MongoDB sharded cluster with 9 nodes, ready for benchmarking. we should load the database with high record counts to see the effect of the sharding.

loading

picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloada -threads 16 -p mongodb.url="mongodb://ycsbUser:ycsbPassword@10.0.13.240:27017/admin?w=1&readPreference=primary"

transaction

picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb run mongodb -s -P workloads/workloada -threads 16 -p mongodb.url="mongodb://ycsbUser:ycsbPassword@10.0.13.240:27017/admin?w=1&readPreference=primary"

sudo docker restart <mongos_container_id>

........................

mongos> sh.enableSharding("ycsb")

.......................

I used this method by creating the ycsb and then usertable and hashed shrd key then i targeted the ycsb database, not the admin database as before. so the benchmark results that is been saved in this repo since  16/08/2024 are following this way but make sure that you repeat the process of make a database with the name ycsb, usertable and making shard hashed key after deleting the ycsb database from the mongo express and then start new ycsb expeeriments and steps to do that are as the following: 

Shard Key: The shard key determines how documents are distributed across the shards. Using a hashed shard key (e.g., { _id: "hashed" }) ensures even distribution of documents across the shards by hashing the key values.

..............


index Requirement: MongoDB requires an index starting with the shard key for sharding. This ensures that queries can efficiently target the appropriate shard(s) and avoid scatter-gather queries.


commands to achieve that:


mongos> use ycsb

switched to db ycsb

mongos> db.createCollection("usertable")

db.usertable.createIndex({ _id: "hashed" });

sh.shardCollection("ycsb.usertable", { _id: "hashed" });

................

the loading phase:

picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloade -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/ycsb?w=1&readPreference=primary"


...........

the transaction phase:

picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb run mongodb -s -P workloads/workloade -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/ycsb?w=1&readPreference=primary"

............

use ycsb

db.usertable.deleteMany({})

db.usertable.drop()

show collections

db.getLastErrorObj()

use config

db.shards.find()

I modified all the data with the new method.

.........................

this is the command that with the last modification for 

the loading:

picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloada -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/ycsb"

for the transaction:

picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb run mongodb -s -P workloads/workloada -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/ycsb"

.................

how to list and make database in mongo shell?

show dbs
use myNewDatabase
db.myCollection.insert({ name: "MongoDB", type: "Database" })

show collections

use ycsb

..................

how to show the content of the usertable?

use ycsb

db.usertable.find().pretty()

db.usertable.find().limit(10).pretty()

db.usertable.find({}, { field1: 1, field2: 1 }).pretty()

....................

sh.status()

rs.status()

........................

to check the status of the replica set:

connect to one of the mongod shards and check the status as follows:

mongo --host mongo_db1 --port 27018

rs.status()

.................

Check Data Distribution: Use the db.getSiblingDB('ycsb').usertable.stats() command to confirm the distribution of data across shards.

..................

this is after loading 60000 record counts:

![image](https://github.com/user-attachments/assets/a51d1822-1b47-4e78-b870-ef39455d6b83)

...................

links:

https://www.mongodb.com/docs/manual/sharding/

https://www.youtube.com/watch?v=mjSNKjTzeao




