#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    key, value = line.strip().split('\t')
    counts[key] += int(value)

# Basic totals
total = counts.get("TOTAL", 0)
errors = counts.get("ERROR", 0)

print(f"Total Requests\t{total}")
print(f"Error Requests\t{errors}")
error_rate = (errors / total * 100) if total else 0
print(f"Error Rate\t{error_rate:.2f}%\n")

# Errors per Node
print("Errors per Node:")
node_keys = [k for k in counts.keys() if k.startswith("NODE_")]
for k in node_keys:
    print(f"{k[5:]}\t{counts[k]}")

# Requests per IP
print("\nTop 5 IPs by Requests:")
ip_keys = [k for k in counts.keys() if k.startswith("IP_")]
top_ips = sorted(
    [(k[3:], counts[k]) for k in ip_keys],
    key=lambda x: x[1], reverse=True
)[:5]
for ip, count in top_ips:
    print(f"{ip}\t{count}")

# Status code counts
print("\nHTTP Status Counts:")
status_keys = [k for k in counts.keys() if k.startswith("STATUS_")]
for k in status_keys:
    print(f"{k[7:]}\t{counts[k]}")

# Top 3 Nodes by Errors
print("\nTop 3 Nodes by Errors:")
top_error_nodes = sorted(
    [(k[5:], counts[k]) for k in node_keys],
    key=lambda x: x[1], reverse=True
)[:3]
for node, val in top_error_nodes:
    print(f"{node}\t{val}")

# Average requests per node
node_counts = [counts[k] for k in node_keys]
avg_per_node = sum(node_counts)/len(node_counts) if node_counts else 0
print(f"\nAverage Requests per Node\t{avg_per_node:.2f}")

# Percent of total errors per node
print("\nPercent of Total Errors per Node:")
for k in node_keys:
    pct = (counts[k]/total*100) if total else 0
    print(f"{k[5:]}\t{pct:.2f}%")

# Requests per Hour
hour_keys = [k for k in counts.keys() if k.startswith("HOUR_")]
if hour_keys:
    print("\nRequests per Hour:")
    for k in sorted(hour_keys):
        print(f"{k[5:]}\t{counts[k]}")

# Top 5 IPs by Errors
ip_error_keys = [k for k in counts.keys() if k.startswith("IP_ERROR_")]
if ip_error_keys:
    print("\nTop 5 IPs by Errors:")
    top_error_ips = sorted(
        [(k[9:], counts[k]) for k in ip_error_keys],
        key=lambda x: x[1], reverse=True
    )[:5]
    for ip, val in top_error_ips:
        print(f"{ip}\t{val}")
