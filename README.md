# Distributed Log Analyzer

A distributed log analysis project using Apache Kafka for log streaming and Hadoop MapReduce for batch processing.

## Overview

This project simulates multiple servers generating log data in real time.  
Log messages are streamed through Kafka, stored in Hadoop HDFS, and analyzed using Hadoop Streaming with Python-based MapReduce scripts.

The project demonstrates a complete big data pipeline from ingestion to analysis.

## Repository Contents

- documentation.pdf  
  Full project documentation

- presentation.pptx  
  Project presentation slides

- implementation  
  Contains all Python source files  
  - producer.py  
  - consumer.py  
  - mapper.py  
  - reducer.py  

## Technologies Used

- Apache Kafka  
- Apache Zookeeper  
- Hadoop HDFS  
- Hadoop Streaming (MapReduce)  
- Python  
- Ubuntu Linux

## System Flow

Log producers send data to Kafka.  
Kafka consumers read the data and store it in HDFS.  
Hadoop MapReduce processes the stored logs and generates analytics.

## Execution Workflow

1. Start Zookeeper  
2. Start Kafka broker  
3. Run log producers  
4. Run Kafka consumer to store logs in HDFS  
5. Execute Hadoop MapReduce job  
6. View analysis results

## Output

The MapReduce job produces aggregated log analysis results such as:

- Log count per server  
- Number of error logs  
- Most frequent IP addresses  

## Purpose

- Demonstrate a distributed log processing system  
- Practice Kafka and Hadoop integration  
- Understand real-time ingestion with batch analytics

## Future Improvements

- Use Apache Spark for faster processing  
- Add visualization dashboards  
- Implement anomaly detection  
- Automate execution using Airflow  
- Add system monitoring
