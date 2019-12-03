# kafka_simulator


## steps to run kafka cluster

### run kafka cluster & zookeeper

```sh
./run_kafka_server.sh
```

### create topic
```sh
../kafka_2.12-2.3.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```

### check topics
```sh
../kafka_2.12-2.3.0/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

### delete topic
```sh
../kafka_2.12-2.3.0/bin/kafka-topics.sh -zookeeper localhost:2181 -delete -topic test
```


### run simulator producer

help:
```sh
usage: kafka_sym_producer.py [-h] [--max MAX] [--cycles CYCLES]

Run simulator of events to kafka topic.

optional arguments:
  -h, --help       show this help message and exit
  --max MAX        max number of generated CDRs in one cycle
  --cycles CYCLES  max cycles
```

example run:
```sh
python ./kafka_sym_producer.py --max 20 --cycles 10
```