# Real Estate Helper App

## Overview

The Real Estate Helper App is a comprehensive system that links sellers and buyers to properties, connects them with agents and service providers, and helps people build value in the property they are going to sell.

## Features

### 1. Property Matching System
- Matches buyers with suitable properties based on:
  - Budget constraints
  - Location preferences  
  - Property type preferences
  - Bedroom/bathroom requirements
- Calculates match scores to rank properties
- Supports multiple user types (buyers, sellers, both)

### 2. Service Provider Directory
- Directory of service providers including:
  - Home inspectors
  - Contractors
  - Landscapers
  - Cleaners
  - Photographers
  - Stagers
  - Appraisers
  - Mortgage brokers
- Search by service type, location, and rating
- Generate value enhancement plans

### 3. Real Estate Agent Network
- Database of licensed real estate agents
- Search by specialties, experience, and service areas
- Agent ratings and credentials

### 4. Property Value Enhancement
- Automated recommendations for improving property value
- Age-based and property-type-specific suggestions
- Service provider recommendations based on property value
- Comprehensive enhancement plans

## Usage

### Command Line Interface

Run the application:
```bash
python realestate_app.py
```

Or use the module:
```bash
python -m realestate.cli
```

### Menu Options

1. **Find property matches for buyer** - Search for properties matching a buyer's criteria
2. **Get property value enhancement recommendations** - Get suggestions for improving property value
3. **Find service providers** - Search for service providers by type and location
4. **Find real estate agents** - Search for agents by specialty and experience
5. **View system statistics** - See system overview and statistics
6. **Exit** - Exit the application

### Programmatic Usage

```python
from realestate.models import Property, User, PropertyType, UserType
from realestate.matcher import PropertyMatcher
from realestate.services import ServiceProviderDirectory

# Create a property matcher
matcher = PropertyMatcher()

# Add a property
property = Property(
    id="prop1",
    address="123 Main St",
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
matcher.add_property(property)

# Add a buyer
buyer = User(
    id="buyer1",
    name="John Doe",
    email="john@example.com",
    phone="555-0123",
    user_type=UserType.BUYER,
    budget_min=400000,
    budget_max=500000,
    preferred_cities=["Austin"]
)
matcher.add_user(buyer)

# Find matches
matches = matcher.find_matches("buyer1")
for property, score in matches:
    print(f"{property.address} - Match Score: {score:.1%}")
```

## Data Models

### Property
- Address, city, state, zip code
- Property type (house, condo, apartment, etc.)
- Bedrooms, bathrooms, square feet
- Price and lot size
- Features and amenities
- Availability status

### User  
- Contact information
- User type (buyer, seller, both)
- Budget constraints
- Location and property preferences
- Minimum bedroom/bathroom requirements

### Agent
- Contact and license information
- Agency affiliation
- Property type specialties
- Service areas
- Experience and ratings

### Service Provider
- Contact information
- Service type specialization
- Company information
- Service areas and pricing
- Ratings and certifications

## Sample Data

The application comes with sample data including:
- 3 properties in Austin and Dallas
- 2 users (1 buyer, 1 seller)
- 1 real estate agent
- 3 service providers (inspector, landscaper, stager)

## Testing

Run the basic tests:
```bash
python test_realestate.py
```

## Integration

The Real Estate Helper App is integrated into the Whisper repository while preserving all original Whisper functionality. Both systems can coexist and be used independently.