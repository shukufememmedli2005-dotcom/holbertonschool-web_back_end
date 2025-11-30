#!/usr/bin/env python3
"""
Function that inserts a new document in a MongoDB collection.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the collection using keyword arguments.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs for the document fields

    Returns:
        The _id of the inserted document
    """
    # Insert the document and get the inserted_id
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
