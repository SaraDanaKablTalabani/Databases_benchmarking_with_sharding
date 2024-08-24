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



  
