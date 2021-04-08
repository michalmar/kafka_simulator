from kafka import KafkaConsumer
# Replace the `ip_address` entries with the IP address of your worker nodes
# Again, you only need one or two, not the full list.
# Note: auto_offset_reset='earliest' resets the starting offset to the beginning
#       of the topic

KAFKABROKERS="10.3.1.12:9092"
kafka_brokers = KAFKABROKERS.split(",")

consumer = KafkaConsumer(bootstrap_servers=kafka_brokers,auto_offset_reset='earliest')
consumer.subscribe(['test'])
# i =  0
for msg in consumer:
  print (msg)
#   i=i+1

# print(f"messages: {i}")


