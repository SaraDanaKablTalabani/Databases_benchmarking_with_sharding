Config Servers (mongo_config1, mongo_config2, mongo_config3): These are essential for the sharded cluster to manage metadata. They form a replica set named configReplSet.
Router (mongo_mongos): Acts as a query router for the sharded cluster, connecting to the config servers.
Shard Servers (mongo_db1 to mongo_db6): Each forms a replica set and is marked as a shard server.
Mongo Express (mongo_express): Provides a web-based MongoDB admin interface connected to the mongos router.

Lebels

docker node update --label-add mongo.config=1 <node-id-1>
docker node update --label-add mongo.config=2 <node-id-2>
docker node update --label-add mongo.config=3 <node-id-3>
docker node update --label-add mongo.shard=1 <node-id-4>
docker node update --label-add mongo.shard=2 <node-id-5>
docker node update --label-add mongo.shard=3 <node-id-6>
docker node update --label-add mongo.shard=4 <node-id-7>
docker node update --label-add mongo.shard=5 <node-id-8>
docker node update --label-add mongo.shard=6 <node-id-9>


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
