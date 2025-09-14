"""
Real Estate Helper App

A system that links sellers and buyers to properties, connects agents and 
service providers, and helps people build value in the property they are going to sell.
"""

from .models import Property, User, Agent, ServiceProvider
from .matcher import PropertyMatcher
from .services import ServiceProviderDirectory
from .cli import main

__version__ = "1.0.0"
__all__ = [
    "Property", 
    "User", 
    "Agent", 
    "ServiceProvider",
    "PropertyMatcher",
    "ServiceProviderDirectory",
    "main"
]