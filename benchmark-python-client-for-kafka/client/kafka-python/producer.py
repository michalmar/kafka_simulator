from kafka import KafkaConsumer, KafkaProducer
# from settings import BOOTSTRAP_SERVERS, TOPICS, MSG
# producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
# producer.send(TOPICS, MSG.encode('utf-8'))

## MMA change -> to get rid of YML
sys.path.append("..")
from .settings import bootstrap_servers, msg_payload, msg_size, topic_kp

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer.send(topic_kp, msg_payload)