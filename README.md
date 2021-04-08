# kafka_simulator

Simple project to run simulation of sending messages to Kafka cluster.

Kafka on Azure HDInsight -> go to [kafka-setup-hdinsight.md](./kafka-setup-hdinsight.md)

## steps to run kafka cluster

### run kafka cluster & zookeeper

```sh
./run_kafka_server.sh
```

to stop server use:
```sh
../kafka_2.12-2.3.0/bin/kafka-server-stop.sh
```


### create topic
```sh
../kafka_2.12-2.3.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic testcdr
```

### check topics
```sh
../kafka_2.12-2.3.0/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

### delete topic
```sh
../kafka_2.12-2.3.0/bin/kafka-topics.sh -zookeeper localhost:2181 -delete -topic test
```

## Mirror Maker
../kafka_2.12-2.3.0/bin/kafka-mirror-maker.sh --consumer.config ../azure-event-hubs-for-kafka/tutorials/mirror-maker/source-kafka.config  --num.streams 1 --producer.config ../azure-event-hubs-for-kafka/tutorials/mirror-maker/mirror-eventhub.config --whitelist=".*"


### run simulator producer

help:
```sh
usage: kafka_sym_producer.py [-h] [--topic TOPIC] [--max MAX]
                             [--cycles CYCLES] [--debug]

Process some integers.

optional arguments:
  -h, --help       show this help message and exit
  --topic TOPIC    kafka topic to write
  --max MAX        max number of generated CDRs in one cycle
  --cycles CYCLES  max cycles
  --debug          debug mode only
```

example run:
```sh
python ./kafka_sym_producer.py --topic testcdr --max 20 --cycles 10 --debug
```


