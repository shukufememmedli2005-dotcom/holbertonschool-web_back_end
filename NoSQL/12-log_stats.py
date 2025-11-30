#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # List of HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents with GET /status
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{get_status_count} status check")

if __name__ == "__main__":
    main()
