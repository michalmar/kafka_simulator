# -*- coding: utf-8 -*-
"""
    settings.py
    ~~~~~~~~~~~~
    Implements and sets the benchmarking related variables and functions for various benchmarking testing.

"""


# settings
msg_count = 1000
msg_counts = [10*1000,100*1000,150*1000,200*1000]
# msg_counts = [10,20]
msg_size = 1*1024 #1kB
msg_payload = ('a' * msg_size).encode()[:msg_size]
bootstrap_servers = 'wn0-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092' #'192.168.99.101:9092' # change if your brokers live else where


producer_timings = {}
consumer_timings = {}

#topic
topic_pk  = 'pycontw2017-pykafka-topic'
topic_kp  = 'pycontw2017-kafkapython-topic'
topic_ckp = 'pycontw2017-confluent-kafka-topic'
