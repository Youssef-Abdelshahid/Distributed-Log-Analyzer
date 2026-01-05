from kafka import KafkaConsumer
import os, time

consumer = KafkaConsumer(
    'dis_logs_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='dis_logs_group'
)

local_file = "/home/hdoop/dis_logs/all_logs.txt"
hdfs_dir = "/user/hdoop/dis_logs/input"

with open(local_file, "w") as f:
    for i, msg in enumerate(consumer):
        f.write(msg.value.decode('utf-8') + "\n")

        if (i + 1) % 50 == 0:
            f.flush()
            os.system(f"hdfs dfs -mkdir -p {hdfs_dir}")
            os.system(f"hdfs dfs -put -f {local_file} {hdfs_dir}")
            print(f"[INFO] Uploaded batch {i+1} logs to HDFS.")
            time.sleep(2)

