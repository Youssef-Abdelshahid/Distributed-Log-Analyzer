from kafka import KafkaProducer
import random, time, sys
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python3 producer.py <node_name>")
    sys.exit(1)

node = sys.argv[1]
producer = KafkaProducer(bootstrap_servers='localhost:9092')

statuses = [200, 200, 404, 500]
ips = [
    "192.168.1.1",
    "10.0.0.5",
    "172.16.0.3",
    "192.168.2.10",
    "10.0.1.12",
    "172.16.1.7",
    "192.168.3.4",
    "10.0.2.8",
    "172.16.2.14",
    "192.168.4.9"
]

num_logs = random.randint(50, 150)

for i in range(num_logs):
    log = f"{datetime.now().isoformat()} {node} {random.choice(ips)} {random.choice(statuses)}"
    producer.send('dis_logs_topic', log.encode('utf-8'))
    time.sleep(0.1)

producer.flush()
producer.close()
print(f"[{node}] Finished sending {num_logs} logs.")

