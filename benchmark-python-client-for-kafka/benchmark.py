# -*- coding: utf-8 -*-
"""
    benchmark.py
    ~~~~~~~~~~~~
    Execute various benchmarking testing

"""

import time
import client.pykafka as pykafka
import client.kafka_python as kpython
# import client.confluent_kafka_python as ckpython

from client.settings import bootstrap_servers, msg_count, msg_payload, topic_kp, msg_size

print(f"Config:")
print(f"bootstrap_servers: {bootstrap_servers}")
print(f"msg_count: {msg_count}")
print(f"msg_payload: {msg_payload}")
print(f"topic_kp: {topic_kp}")
print(f"msg_size: {msg_size/1024}kB")

producer_timings = {}
consumer_timings = {}

def calculate_thoughput(timing, n_messages=1000000, msg_size=100):
    print("Processed {0} messsages in {1:.2f} seconds".format(n_messages, timing))
    print("{0:.2f} MB/s".format((msg_size * n_messages) / timing / (1024*1024)))
    print("{0:.2f} Msgs/s".format(n_messages / timing))



# produce message via pykafka
# print("Pushing to Kafka via PyKafka:")
producer_timings['pykafka_producer'] = pykafka.pykafka_producer_performance()
calculate_thoughput(producer_timings['pykafka_producer'], msg_count, msg_size)

# Run again with librdkafka
#producer_timings['pykafka_producer_rdkafka'] = pykafka.pykafka_producer_performance(use_rdkafka=True)
#calculate_thoughput(producer_timings['pykafka_producer_rdkafka'])
#
#
#_ = pykafka_consumer_performance(use_rdkafka=False)
# consumer_timings['pykafka_consumer'] = pykafka.pykafka_consumer_performance()
# calculate_thoughput(consumer_timings['pykafka_consumer'])


# Run it once thorough to warm the cache
## Run again with librdkafka
#_ = pykafka_consumer_performance(use_rdkafka=True)
#consumer_timings['pykafka_consumer_rdkafka'] = #pykafka.pykafka_consumer_performance(use_rdkafka=True)
#calculate_thoughput(consumer_timings['pykafka_consumer_rdkafka'])
# print("Pushing to Kafka via Kafka-Python:")
producer_timings['python_kafka_producer'] = kpython.python_kafka_producer_performance()
calculate_thoughput(producer_timings['python_kafka_producer'], msg_count, msg_size)

# _ = kpython.python_kafka_consumer_performance()
# consumer_timings['python_kafka_consumer'] = kpython.python_kafka_consumer_performance()
# calculate_thoughput(consumer_timings['python_kafka_consumer'])

if (False):
    # confluent-kafka-python
    producer_timings['confluent_kafka_producer'] = ckpython.confluent_kafka_producer_performance()
    calculate_thoughput(producer_timings['confluent_kafka_producer'], msg_count, msg_size)

    _ = confluent_kafka_consumer_performance() # Warm cache
    consumer_timings['confluent_kafka_consumer'] = ckpython.confluent_kafka_consumer_performance()
    calculate_thoughput(consumer_timings['confluent_kafka_consumer'], msg_count, msg_size)
