#!/usr/bin/python3
"""Defines a restricted class."""


class RestrictedClass:
    """
    Prevents the creation of new attributes in RestrictedClass
    except for an attribute named 'first_name'.
    """

    __slots__ = ["first_name"]
