#!/usr/bin/env python3
"""
Function that updates the 'topics' field of a school document
based on its name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all documents with the given school name, setting the
    'topics' field to the provided list of topics.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list of str): list of topics to assign
    """
    # Use update_many to ensure all matching documents are updated
    mongo_collection.update_many(
        { "name": name },         # Filter: match documents with this name
        { "$set": { "topics": topics } }  # Update: set the 'topics' field
    )
