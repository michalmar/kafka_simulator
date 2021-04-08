# -*- coding: utf-8 -*-
"""
    benchmark.py
    ~~~~~~~~~~~~
    Execute various benchmarking testing

"""

import time
import client.pykafka as pykafka
import client.kafka_python as kpython
import client.confluent_kafka_python as ckpython

from client.settings import bootstrap_servers, msg_payload, msg_size, msg_counts

# import argparse

print(f"-"*80)
print(f"Test init.")
print(f"Config:")
print(f"bootstrap_servers: {bootstrap_servers}")
print(f"msg_counts: {msg_counts}")
# print(f"msg_payload: {msg_payload}")
print(f"msg_size: {msg_size/1024}kB")
print(f"-"*80)

producer_timings = {}
consumer_timings = {}

def calculate_thoughput(timing, n_messages=1000000, msg_size=100):
    print("Processed {0} messsages in {1:.2f} seconds".format(n_messages, timing))
    throughput = (msg_size * n_messages) / timing / (1024*1024)
    freq = n_messages / timing
    print("{0:.2f} MB/s".format(throughput))
    print("{0:.2f} Msgs/s".format(freq))
    return [timing, throughput, freq]

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.0f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


print(f"Test start.")

# produce message via pykafka
for msg_count in msg_counts:
    time_in_seconds = pykafka.pykafka_producer_performance(msg_count=msg_count)
    producer_timings[f'pykafka_producer_{human_format(msg_count)}'] = calculate_thoughput(time_in_seconds, msg_count, msg_size)

# produce via Kafka-Python
for msg_count in msg_counts:
    time_in_seconds = kpython.python_kafka_producer_performance(msg_count=msg_count)
    producer_timings[f'python_kafka_producer_{human_format(msg_count)}'] = calculate_thoughput(time_in_seconds, msg_count, msg_size)

# produce via confluent-kafka-python
for msg_count in msg_counts:
    time_in_seconds = ckpython.confluent_kafka_producer_performance(msg_count=msg_count)
    producer_timings[f'confluent_kafka_producer_{human_format(msg_count)}'] = calculate_thoughput(time_in_seconds, msg_count, msg_size)


print(f"Test done.")
import pandas as pd


# producer_timings = {'confluent_kafka_producer': [0.1,123]}
# pd.DataFrame.from_dict(producer_timings, orient='index').rename(columns={0: 'time_in_seconds', 1:'MB/s',2:'Msg/s'})


# consumer_df = pd.DataFrame.from_dict(consumer_timings, orient='index').rename(columns={0: 'time_in_seconds'})
producer_df = pd.DataFrame.from_dict(producer_timings, orient='index').rename(columns={0: 'time_in_seconds', 1:'MB/s',2:'Msg/s'})

# # consumer_df['MBs/s'] = (len(msg_payload) * msg_count) / consumer_df.time_in_seconds / (1024*1024)
# producer_df['MBs/s'] = (len(msg_payload) * msg_count) / producer_df.time_in_seconds / (1024*1024)

# # consumer_df['Msgs/s'] = msg_count / consumer_df.time_in_seconds
# producer_df['Msgs/s'] = msg_count / producer_df.time_in_seconds

producer_df.sort_index(inplace=True)
producer_df

# consumer_df.sort_index(inplace=True)
# consumer_df


## Vizualization
# import seaborn as sns
# %pylab inline
# producer_df.plot(kind='bar', subplots=True, figsize=(10, 10), title="Producer Comparison")

producer_df.to_csv("producer.csv")