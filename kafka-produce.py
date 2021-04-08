from kafka import KafkaProducer


# KAFKAZKHOSTS="zk0-xtv-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:2181,zk2-xtv-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:2181,zk5-xtv-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:2181"
KAFKABROKERS="wn0-xtx-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092,wn1-xtx-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092"
# KAFKABROKERS="xtxkafka-int.azurehdinsight.net"
# KAFKABROKERS="10.3.1.12:9092"


kafka_brokers = KAFKABROKERS.split(",")

i=1
producer = KafkaProducer(bootstrap_servers=kafka_brokers)

for i in range(3):
    msg = f"abcdef{i}"
    producer.send('test', str.encode(msg))
print("all sent.")

