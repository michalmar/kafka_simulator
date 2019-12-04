nohup ~/kafka_2.12-2.3.0/bin/zookeeper-server-start.sh ~/kafka_2.12-2.3.0/config/zookeeper.properties > zookeeper.out 2> zookeeper.err &
sleep 20
echo "zookeper started"
nohup ~/kafka_2.12-2.3.0/bin/kafka-server-start.sh ~/kafka_2.12-2.3.0/config/server.properties > kafka.out 2> kafka.err &
sleep 20
echo "kafka started"
nohup ~/kafka_2.12-2.3.0/bin/kafka-mirror-maker.sh --consumer.config ~/azure-event-hubs-for-kafka/tutorials/mirror-maker/source-kafka.config  --num.streams 1 --producer.config ~/azure-event-hubs-for-kafka/tutorials/mirror-maker/mirror-eventhub.config --whitelist=".*"  > kafka-mirror.out 2> kafka-mirror.err &
sleep 5
echo "kafka mirror maker started"

