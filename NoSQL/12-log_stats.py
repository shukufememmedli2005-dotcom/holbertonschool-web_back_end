#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def main():
    """
    Connects to the MongoDB 'logs' database, retrieves statistics from the
    'nginx' collection, and prints:
      - Total number of logs
      - Number of logs by HTTP method (GET, POST, PUT, PATCH, DELETE)
      - Number of GET requests to '/status'
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    nginx = db.nginx

    # Total number of logs
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET requests to /status
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()
