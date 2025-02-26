#!/usr/bin/env python3
"""
Document management script
"""
def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
