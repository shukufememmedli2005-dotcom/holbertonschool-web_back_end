#!/usr/bin/env python3
"""
Function that returns a list of schools containing a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns all documents (schools) that have the given topic in their 'topics' field.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        List of matching documents, or empty list if none found.
    """
    # Query: look for documents where the 'topics' array contains the given topic
    result = mongo_collection.find({ "topics": topic })

    # Convert cursor to list and return
    return list(result)
