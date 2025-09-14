"""
Tests for the Real Estate Helper App
"""

import pytest
from realestate.models import Property, User, Agent, ServiceProvider, PropertyType, UserType, ServiceType
from realestate.matcher import PropertyMatcher
from realestate.services import ServiceProviderDirectory


def test_property_creation():
    """Test creating a property"""
    prop = Property(
        id="test1",
        address="123 Test St",
        city="Austin",
        state="TX",
        zip_code="78701",
        property_type=PropertyType.HOUSE,
        bedrooms=3,
        bathrooms=2.0,
        square_feet=1800,
        lot_size=0.25,
        price=450000,
        seller_id="seller1"
    )
    
    assert prop.id == "test1"
    assert prop.address == "123 Test St"
    assert prop.property_type == PropertyType.HOUSE
    assert prop.bedrooms == 3
    assert prop.price == 450000


def test_user_creation():
    """Test creating a user"""
    user = User(
        id="buyer1",
        name="John Doe",
        email="john@example.com",
        phone="555-0123",
        user_type=UserType.BUYER,
        budget_min=300000,
        budget_max=500000
    )
    
    assert user.id == "buyer1"
    assert user.name == "John Doe"
    assert user.user_type == UserType.BUYER
    assert user.budget_max == 500000


def test_property_matcher():
    """Test property matching functionality"""
    matcher = PropertyMatcher()
    
    # Add a property
    prop = Property(
        id="prop1",
        address="123 Test St",
        city="Austin",
        state="TX",
        zip_code="78701",
        property_type=PropertyType.HOUSE,
        bedrooms=3,
        bathrooms=2.0,
        square_feet=1800,
        lot_size=0.25,
        price=450000,
        seller_id="seller1"
    )
    matcher.add_property(prop)
    
    # Add a buyer
    buyer = User(
        id="buyer1",
        name="John Doe",
        email="john@example.com",
        phone="555-0123",
        user_type=UserType.BUYER,
        budget_min=400000,
        budget_max=500000,
        preferred_cities=["Austin"],
        preferred_property_types=[PropertyType.HOUSE]
    )
    matcher.add_user(buyer)
    
    # Find matches
    matches = matcher.find_matches("buyer1")
    
    assert len(matches) == 1
    assert matches[0][0].id == "prop1"
    assert matches[0][1] > 0  # Should have a positive match score


def test_service_provider_directory():
    """Test service provider directory functionality"""
    directory = ServiceProviderDirectory()
    
    # Add a service provider
    provider = ServiceProvider(
        id="sp1",
        name="Test Cleaner",
        email="clean@test.com",
        phone="555-1111",
        service_type=ServiceType.CLEANER,
        company="Clean Co",
        areas_served=["Austin"],
        rating=4.5
    )
    directory.add_service_provider(provider)
    
    # Find providers
    providers = directory.find_service_providers(ServiceType.CLEANER, "Austin")
    
    assert len(providers) == 1
    assert providers[0].name == "Test Cleaner"
    assert providers[0].service_type == ServiceType.CLEANER


def test_property_recommendations():
    """Test property enhancement recommendations"""
    matcher = PropertyMatcher()
    
    # Add an older property
    prop = Property(
        id="old_prop",
        address="456 Old St",
        city="Austin",
        state="TX",
        zip_code="78701",
        property_type=PropertyType.HOUSE,
        bedrooms=2,
        bathrooms=1.0,
        square_feet=1200,
        lot_size=0.2,
        price=250000,
        seller_id="seller1",
        year_built=1980
    )
    matcher.add_property(prop)
    
    recommendations = matcher.get_property_recommendations("old_prop")
    
    assert len(recommendations) > 0
    assert any("electrical" in rec.lower() for rec in recommendations)
    assert any("kitchen" in rec.lower() for rec in recommendations)


def test_value_enhancement_plan():
    """Test value enhancement plan generation"""
    directory = ServiceProviderDirectory()
    
    # Add some service providers
    providers = [
        ServiceProvider("sp1", "Inspector", "i@test.com", "555-1", ServiceType.HOME_INSPECTOR, "Co", areas_served=["Austin"], rating=4.5),
        ServiceProvider("sp2", "Cleaner", "c@test.com", "555-2", ServiceType.CLEANER, "Co", areas_served=["Austin"], rating=4.7),
        ServiceProvider("sp3", "Photographer", "p@test.com", "555-3", ServiceType.PHOTOGRAPHER, "Co", areas_served=["Austin"], rating=4.9)
    ]
    
    for provider in providers:
        directory.add_service_provider(provider)
    
    plan = directory.get_value_enhancement_plan(400000, "Austin")
    
    assert len(plan) > 0
    assert ServiceType.HOME_INSPECTOR.value in plan
    assert ServiceType.CLEANER.value in plan


if __name__ == "__main__":
    # Run basic tests
    test_property_creation()
    test_user_creation()
    test_property_matcher()
    test_service_provider_directory()
    test_property_recommendations()
    test_value_enhancement_plan()
    print("All tests passed!")