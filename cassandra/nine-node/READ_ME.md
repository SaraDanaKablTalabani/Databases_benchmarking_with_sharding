this .yml has been used for the set up: final-works-global-mode.yml 

...................

version: '3.7'

services:
  cassandra-seed1:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.seed == 1
    volumes:
      - cassandra-seed1-data:/var/lib/cassandra
    ports:
      - "9042:9042"
    command: "cassandra -f"

  cassandra-seed2:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack2
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.seed == 2
    volumes:
      - cassandra-seed2-data:/var/lib/cassandra
    command: "cassandra -f"

  cassandra-node1:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack1
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.node == 1
    volumes:
      - cassandra-node1-data:/var/lib/cassandra
    command: "cassandra -f"

  cassandra-node2:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack1
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.node == 2
    volumes:
      - cassandra-node2-data:/var/lib/cassandra
    command: "cassandra -f"

  cassandra-node3:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack2
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.node == 3
    volumes:
      - cassandra-node3-data:/var/lib/cassandra
    command: "cassandra -f"

  cassandra-node4:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack2
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.node == 4
    volumes:
      - cassandra-node4-data:/var/lib/cassandra
    command: "cassandra -f"
  cassandra-node5:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack2
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.node == 5
    volumes:
      - cassandra-node4-data:/var/lib/cassandra
    command: "cassandra -f"

  cassandra-node6:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack2
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.node == 6
    volumes:
      - cassandra-node4-data:/var/lib/cassandra
    command: "cassandra -f"
  cassandra-node7:
    image: cassandra:latest
    environment:
      - CASSANDRA_CLUSTER_NAME=MyCassandraCluster
      - CASSANDRA_DC=dc1
      - CASSANDRA_RACK=rack2
      - CASSANDRA_SEEDS=cassandra-seed1
      - CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch
    networks:
      - cassandra-net
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.labels.cassandra.node == 7
    volumes:
      - cassandra-node4-data:/var/lib/cassandra
    command: "cassandra -f"
networks:
  cassandra-net:
    driver: overlay

volumes:
  cassandra-seed1-data:
  cassandra-seed2-data:
  cassandra-node1-data:
  cassandra-node2-data:
  cassandra-node3-data:
  cassandra-node4-data:
  .................

Checking Cassandra Cluster Status:

# Run this inside one of the Cassandra containers:

nodetool status

...............

To check data distribution and replication, you can use:

nodetool ring

.............

Designing the Schema with a Proper Partition Key

CREATE TABLE ycsb.usertable (
  user_id UUID,
  region TEXT,
  data TEXT,
  PRIMARY KEY ((user_id, region))
);

.......................

![image](https://github.com/user-attachments/assets/90f9e09c-825d-47a4-8d82-add3b7a37026)

.......................

steps after the containers are up and running:

access the seed container which deployed in our case on the pc0 which the manger node
then execute this sudo docker exec -it <cassandra-container-id> cqlsh

 after that we make a keyspace like this:

 CREATE KEYSPACE ycsb WITH REPLICATION = {
  'class': 'NetworkTopologyStrategy',
  'my-datacenter-1': 6
};

Verify the Keyspace Creation

DESCRIBE KEYSPACE ycsb;

USE ycsb;

create table usertable (

y_id varchar primary key,

field0 varchar,

field1 varchar,

field2 varchar,

field3 varchar,

field4 varchar,

field5 varchar,

field6 varchar,

field7 varchar,

field8 varchar,

field9 varchar);

TRUNCATE usertable;

verify

SELECT * FROM usertable;

DESCRIBE TABLES;


....................

Primary Key (y_id): The y_id is the partition key. In Cassandra, the partition key determines how data is distributed across nodes. Data with the same partition key is stored together, while different partition keys are spread across the cluster.

Partitioning Strategy: By default, Cassandra uses a consistent hashing algorithm for partitioning data. This consistent hashing ensures that data is distributed evenly across all nodes in the cluster.

..................

then the commmand to load: picocluster64@pc24:~/fe5/ycsb-cassandra-binding-0.17.0 $ sudo ./bin/ycsb load cassandra-cql -s -P workloads/workloada -threads 16 -p hosts="10.0.13.234" -p port=9042 -p cassandra.username=admin -p cassandra.password=admin

transaction: picocluster64@pc24:~/fe5/ycsb-cassandra-binding-0.17.0 $ sudo ./bin/ycsb run cassandra-cql -s -P workloads/workloada -threads 16 -p hosts="10.0.13.234" -p port=9042 -p cassandra.username=admin -p cassandra.password=admin



.......................

links:

https://github.com/bioatlas/ala-docker/blob/master/swarm-cassandra-cluster.yml

https://github.com/sukolupo/cassandra-docker-swarm/blob/master/README.md

https://github.com/bioatlas/ala-docker/blob/master/swarm-cassandra-cluster.yml

https://github.com/digitalis-io/ccc/blob/master/docker-compose.yml

https://medium.com/@kayvan.sol2/deploying-apache-cassandra-cluster-3-nodes-with-docker-compose-3634ef8345e8

https://groups.google.com/g/kairosdb-group/c/DoNPB48tMZk

  
