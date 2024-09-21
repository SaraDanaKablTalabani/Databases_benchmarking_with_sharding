redis-cli --cluster create redis-node-0:6379 redis-node-1:6379 redis-node-2:6379 redis-node-3:6379 redis-node-4:6379 redis-node-5:6379 --cluster-replicas 1 --cluster-yes

redis-cli --cluster create 10.0.13.240:6379 10.0.13.244:6379 10.0.13.242:6379 10.0.13.241:6379 redis-node-4:6379 10.0.13.240:6379 --cluster-replicas 1 --cluster-yes


Links:
 https://github.com/bitnami/containers/blob/main/bitnami/redis-cluster/docker-compose.yml
