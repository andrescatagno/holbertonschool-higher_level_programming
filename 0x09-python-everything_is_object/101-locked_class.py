#!/usr/bin/python3
"""A locked class that prevents the user from dinamically creating new instance attributes,
except if the new instance attribute is called 'first_name'"""

class LockedClass:
    """A locked class that prevents the user from dinamically creating new instance attributes,
    except if the new instance attribute is called 'first_name'"""
    __slots__ = 'first_name'
