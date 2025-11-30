#!/usr/bin/env python3
"""
Function that lists all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Returns a list of all documents in the given collection.
    
    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents, or an empty list if the collection is empty.
    """
    # Perform a find() query to get all documents.
    # find() returns a cursor, so we convert it to a list.
    documents = list(mongo_collection.find())

    # If the cursor is empty, list() will return an empty list — perfect behavior.
    return documents
