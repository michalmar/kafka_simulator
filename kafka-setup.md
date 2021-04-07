# Setup for HDInsight Kafka

source: https://docs.microsoft.com/en-us/azure/hdinsight/kafka/apache-kafka-get-started


## login to Cluster (Head Node)
```
CLUSTERNAME="xtx-kafka"
ssh sshuser@$CLUSTERNAME-ssh.azurehdinsight.net
```

## Setup inside the Kafka cluser
```
sudo apt -y install jq

clusterName="xtx-kafka"
password="**********"
```

**Setup hosts & brokers**
```
KAFKAZKHOSTS=$(curl -sS -u admin:$password -G https://$clusterName.azurehdinsight.net/api/v1/clusters/$clusterName/services/ZOOKEEPER/components/ZOOKEEPER_SERVER | jq -r '["\(.host_components[].HostRoles.host_name):2181"] | join(",")' | cut -d',' -f1,2);

KAFKABROKERS=$(curl -sS -u admin:$password -G https://$clusterName.azurehdinsight.net/api/v1/clusters/$clusterName/services/KAFKA/components/KAFKA_BROKER | jq -r '["\(.host_components[].HostRoles.host_name):9092"] | join(",")' | cut -d',' -f1,2);

echo $KAFKABROKERS

wn0-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092,wn1-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092
```

### CREATE TOPIC
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 3 --partitions 8 --topic test --zookeeper $KAFKAZKHOSTS

/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 3 --partitions 8 --topic crimes_topic --zookeeper $KAFKAZKHOSTS

/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 3 --partitions 8 --topic pycontw2017-pykafka-topic --zookeeper $KAFKAZKHOSTS
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 3 --partitions 8 --topic pycontw2017-kafkapython-topic --zookeeper $KAFKAZKHOSTS
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 3 --partitions 8 --topic pycontw2017-confluent-kafka-topic --zookeeper $KAFKAZKHOSTS

### LIST TOPICS
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --list --zookeeper $KAFKAZKHOSTS

### DELETE TOPICS
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --delete --topic test --zookeeper $KAFKAZKHOSTS

/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --delete --topic pycontw2017-pykafka-topic --zookeeper $KAFKAZKHOSTS
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --delete --topic pycontw2017-kafkapython-topic --zookeeper $KAFKAZKHOSTS
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --delete --topic pycontw2017-confluent-kafka-topic --zookeeper $KAFKAZKHOSTS


### CONSUMER (run on the head node)
/usr/hdp/current/kafka-broker/bin/kafka-console-consumer.sh --bootstrap-server $KAFKABROKERS --topic test --from-beginning

###  Set a retention on the topic to expire in 10 minutes
/usr/hdp/current/kafka-broker/bin/kafka-configs.sh --zookeeper $KAFKAZKHOSTS --alter --entity-type topics --entity-name crimes_topic --add-config retention.ms=600000

#### List consumer groups - informational

#### Describe topic
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --zookeeper $KAFKAZKHOSTS --describe --topic crimes_topic



### PRODUCER
```
python ./kafka_sym_producer.py --topic test --max 5 --cycles 2 --brokers wn0-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092,wn1-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092
```



# MIRORRMAKER
/usr/hdp/current/kafka-broker/bin/kafka-mirror-maker.sh  --consumer.config ~/src_kafka.config --num.streams 1 --producer.config ~/dest_kafka.config --whitelist=".*"
