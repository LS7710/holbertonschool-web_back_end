#!/usr/bin/env python3
"""Task 12"""

from pymongo import MongoClient


def log_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Get the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Get the count of each method type
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Get the number of logs where method is GET and path is /status
    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    log_stats()
