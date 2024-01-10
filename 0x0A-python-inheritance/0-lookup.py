#!/bin/bash

"""description"""
def lookup(obj):
    """description"""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
