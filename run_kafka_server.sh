nohup ~/kafka_2.12-2.3.0/bin/zookeeper-server-start.sh ~/kafka_2.12-2.3.0/config/zookeeper.properties > zookeeper.out 2> zookeeper.err &
sleep 30
echo "zookeper started"
nohup ~/kafka_2.12-2.3.0/bin/kafka-server-start.sh ~/kafka_2.12-2.3.0/config/server.properties > kafka.out 2> kafka.err &
sleep 30
echo "kafka started"
