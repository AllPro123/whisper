"""
Data models for the Real Estate Helper App
"""

from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import json


class PropertyType(Enum):
    HOUSE = "house"
    APARTMENT = "apartment"
    CONDO = "condo"
    TOWNHOUSE = "townhouse"
    COMMERCIAL = "commercial"
    LAND = "land"


class UserType(Enum):
    BUYER = "buyer"
    SELLER = "seller"
    BOTH = "both"


class ServiceType(Enum):
    HOME_INSPECTOR = "home_inspector"
    CONTRACTOR = "contractor"
    LANDSCAPER = "landscaper"
    CLEANER = "cleaner"
    PHOTOGRAPHER = "photographer"
    STAGER = "stager"
    APPRAISER = "appraiser"
    MORTGAGE_BROKER = "mortgage_broker"


@dataclass
class Property:
    """Represents a real estate property"""
    id: str
    address: str
    city: str
    state: str
    zip_code: str
    property_type: PropertyType
    bedrooms: int
    bathrooms: float
    square_feet: int
    lot_size: float
    price: float
    seller_id: str
    description: str = ""
    features: List[str] = field(default_factory=list)
    year_built: Optional[int] = None
    garage_spaces: int = 0
    is_available: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert property to dictionary"""
        return {
            'id': self.id,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'property_type': self.property_type.value,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'square_feet': self.square_feet,
            'lot_size': self.lot_size,
            'price': self.price,
            'seller_id': self.seller_id,
            'description': self.description,
            'features': self.features,
            'year_built': self.year_built,
            'garage_spaces': self.garage_spaces,
            'is_available': self.is_available
        }


@dataclass 
class User:
    """Represents a user (buyer or seller)"""
    id: str
    name: str
    email: str
    phone: str
    user_type: UserType
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    preferred_cities: List[str] = field(default_factory=list)
    preferred_property_types: List[PropertyType] = field(default_factory=list)
    min_bedrooms: Optional[int] = None
    min_bathrooms: Optional[float] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'user_type': self.user_type.value,
            'budget_min': self.budget_min,
            'budget_max': self.budget_max,
            'preferred_cities': self.preferred_cities,
            'preferred_property_types': [pt.value for pt in self.preferred_property_types],
            'min_bedrooms': self.min_bedrooms,
            'min_bathrooms': self.min_bathrooms
        }


@dataclass
class Agent:
    """Represents a real estate agent"""
    id: str
    name: str
    email: str
    phone: str
    license_number: str
    agency: str
    specialties: List[PropertyType] = field(default_factory=list)
    areas_served: List[str] = field(default_factory=list)
    years_experience: int = 0
    rating: float = 5.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert agent to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'license_number': self.license_number,
            'agency': self.agency,
            'specialties': [s.value for s in self.specialties],
            'areas_served': self.areas_served,
            'years_experience': self.years_experience,
            'rating': self.rating
        }


@dataclass
class ServiceProvider:
    """Represents a service provider that helps enhance property value"""
    id: str
    name: str
    email: str
    phone: str
    service_type: ServiceType
    company: str
    description: str = ""
    areas_served: List[str] = field(default_factory=list)
    price_range: str = ""
    rating: float = 5.0
    certifications: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert service provider to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'service_type': self.service_type.value,
            'company': self.company,
            'description': self.description,
            'areas_served': self.areas_served,
            'price_range': self.price_range,
            'rating': self.rating,
            'certifications': self.certifications
        }