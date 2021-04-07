# bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

## USAGE: python ./kafka_sym_producer.py --topic testcdr --max 20 --cycles 10 --debug
## USAGE: python ./kafka_sym_producer.py --topic testme --max 10 --cycles 50
## USAGE: python ./kafka_sym_producer.py --topic testcdr --max 20 --cycles 10 --debug --brokers wn0-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092,wn1-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092
## USAGE: python ./kafka_sym_producer.py --topic test --max 5 --cycles 2 --brokers wn0-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092,wn1-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092



## USAGE: KAFKABROKERS="wn0-xtx-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092,wn1-xtx-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092"
## USAGE: python ./kafka_sym_producer.py --topic test --max 5 --cycles 2 --brokers $KAFKABROKERS


import os
from time import sleep
from json import dumps
from kafka import KafkaProducer
from faker import Factory
import random
import string
import numpy as np
import argparse
from types import *


def randCDR(num):
    # tmp = ""+str(fake.name())
    tmp = ""+str(fake.word())
    # tmp = ""+random.choice(["Tomas","Michal","Petr","Jirka"])
    # tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    return tmp


def randCDRXXXX(num):
    tmp = ""+str(num)
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(random.randint(1000000,20000000))
    tmp += ","+str(random.randint(1000000,20000000))
    tmp += ","+str(random.randint(1000000,20000000))
    tmp += ","+str(random.randint(1000000,20000000))
    tmp += ","+str(random.randint(1000000,20000000))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(fake.date_time())
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(100,900))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    tmp += ","+str(random.randint(1,9))
    return tmp


def genCDRs(topic, num, debug=False):

    ## bursts -> gen array 
    # data =[]
    # for x in range(num):
    #     data.append({'cdr' : randCDR(x)})
    # print(f"generated {len(data)} CDRs")
    # if (debug):
    #     print(dumps(data)[0:80])
    # else:
    #     producer.send(topic, value=data)

    ## produce as multiple messages 
    for x in range(num):
        data = randCDR(x)
        if (debug):
            print(dumps(data)[0:80])
        else:
            producer.send(topic, value=data)
            # producer.send('test', str.encode("sxxx"))
    print(f"generated {num} CDRs")
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--brokers', dest='brokers', type=str, default='localhost:9092',
                    help='kafka brokers, format: broker1:port,broker2:port,...')
    parser.add_argument('--topic', dest='topic', type=str, default='test',
                    help='kafka topic to write')
    parser.add_argument('--max', dest='max', type=str, default=10,
                    help='max number of generated CDRs in one cycle')
    parser.add_argument('--cycles', dest='cycles', type=str, default=2,
                    help='max cycles')
    parser.add_argument('--debug', action='store_true', help='debug mode only')

                   
    args = parser.parse_args()

    # # DBG LOCALLY
    # args.topic = "test"
    # args.max = 10
    # args.cycles = 2
    # # debug=True doesn't send any data
    # args.debug = False


    # if not(isinstance(args.max,int)):
    #     print("MAX is not an integer: %r" % args.max) 
    #     quit()

    # if not(isinstance(args.cycles,int)):
    #     print("cycles is not an integer: %r" % args.cycles)
    #     quit()


    # KAFKAZKHOSTS="zk0-xtv-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:2181,zk2-xtv-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:2181,zk5-xtv-ka.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:2181"
    # KAFKABROKERS="wn0-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092,wn1-xtvkaf.phpziwd1d3iedoucfn5brcnrrc.ax.internal.cloudapp.net:9092"
    KAFKABROKERS=args.brokers

    # KAFKABROKERS = os.environ["KAFKABROKERS"]
    # print (f"Kafka brokers: {KAFKABROKERS}")

    kafka_brokers = KAFKABROKERS.split(",")
    print (f"Kafka brokers: {kafka_brokers}")
    # # localhost usage - running on Kafka Cluster
    # kafka_brokers = ['localhost:9092']

    producer = KafkaProducer(bootstrap_servers=kafka_brokers,
                            value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))

    print(f"Running simulation with total of {args.cycles} cycles (each max {args.max} CDRs)")

    if (args.debug):
        print(f"INFO: debug mode only")

    fake = Factory.create()

    bursts = np.random.randint(int(args.max), size=int(args.cycles))
    for numcdrs in bursts:
        genCDRs(topic=args.topic, num=numcdrs, debug=args.debug)
        sleep(1)


