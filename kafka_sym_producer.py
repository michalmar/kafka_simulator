# bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

## USAGE: python ./kafka_sym_producer.py --topic testcdr --max 20 --cycles 10 --debug
## USAGE: python ./kafka_sym_producer.py --topic testme --max 10 --cycles 50

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

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))



def randCDR(num):
    tmp = ""+str(fake.name())
    tmp = ""+random.choice(["Tomas","Michal","Petr","Jirka"])
    # tmp += ","+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
    return tmp


def randCDRx(num):
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
    print(f"generated {num} CDRs")
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    
    parser.add_argument('--topic', dest='topic', type=str, default='test',
                    help='kafka topic to write')
    parser.add_argument('--max', dest='max', type=str, default=10,
                    help='max number of generated CDRs in one cycle')
    parser.add_argument('--cycles', dest='cycles', type=str, default=2,
                    help='max cycles')
    parser.add_argument('--debug', action='store_true', help='debug mode only')


                    
    args = parser.parse_args()

    # if not(isinstance(args.max,int)):
    #     print("MAX is not an integer: %r" % args.max) 
    #     quit()

    # if not(isinstance(args.cycles,int)):
    #     print("cycles is not an integer: %r" % args.cycles)
    #     quit()

    print(f"Running simulation with total of {args.cycles} cycles (each max {args.max} CDRs)")

    if (args.debug):
        print(f"INFO: debug mode only")

    fake = Factory.create()

    bursts = np.random.randint(int(args.max), size=int(args.cycles))
    for numcdrs in bursts:
        genCDRs(topic=args.topic, num=numcdrs, debug=args.debug)
        sleep(1)