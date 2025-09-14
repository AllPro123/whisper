"""
Property matching system that connects buyers with suitable properties
"""

from typing import List, Dict, Optional, Tuple
from .models import Property, User, UserType, PropertyType


class PropertyMatcher:
    """Matches buyers with properties based on their preferences and budget"""
    
    def __init__(self):
        self.properties: Dict[str, Property] = {}
        self.users: Dict[str, User] = {}
    
    def add_property(self, property: Property) -> None:
        """Add a property to the system"""
        self.properties[property.id] = property
    
    def add_user(self, user: User) -> None:
        """Add a user to the system"""
        self.users[user.id] = user
    
    def find_matches(self, user_id: str, limit: int = 10) -> List[Tuple[Property, float]]:
        """
        Find properties that match a user's preferences
        Returns list of (property, match_score) tuples sorted by score
        """
        if user_id not in self.users:
            return []
        
        user = self.users[user_id]
        if user.user_type not in [UserType.BUYER, UserType.BOTH]:
            return []
        
        matches = []
        for property in self.properties.values():
            if not property.is_available:
                continue
                
            score = self._calculate_match_score(user, property)
            if score > 0:
                matches.append((property, score))
        
        # Sort by score (highest first) and return top matches
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[:limit]
    
    def _calculate_match_score(self, user: User, property: Property) -> float:
        """Calculate how well a property matches a user's preferences (0-1 scale)"""
        score = 0.0
        total_factors = 0
        
        # Budget check (most important factor)
        if user.budget_min is not None and user.budget_max is not None:
            if user.budget_min <= property.price <= user.budget_max:
                score += 0.4  # 40% weight for budget
            else:
                return 0.0  # Property outside budget gets 0 score
            total_factors += 0.4
        
        # City preference
        if user.preferred_cities:
            if property.city.lower() in [city.lower() for city in user.preferred_cities]:
                score += 0.2  # 20% weight for city
            total_factors += 0.2
        
        # Property type preference
        if user.preferred_property_types:
            if property.property_type in user.preferred_property_types:
                score += 0.2  # 20% weight for property type
            total_factors += 0.2
        
        # Bedroom requirement
        if user.min_bedrooms is not None:
            if property.bedrooms >= user.min_bedrooms:
                score += 0.1  # 10% weight for bedrooms
            total_factors += 0.1
        
        # Bathroom requirement
        if user.min_bathrooms is not None:
            if property.bathrooms >= user.min_bathrooms:
                score += 0.1  # 10% weight for bathrooms
            total_factors += 0.1
        
        # Normalize score
        if total_factors > 0:
            return score / total_factors
        return 0.0
    
    def get_property_recommendations(self, property_id: str) -> List[str]:
        """Get recommendations for improving property value"""
        if property_id not in self.properties:
            return []
        
        property = self.properties[property_id]
        recommendations = []
        
        # Age-based recommendations
        if property.year_built and property.year_built < 1990:
            recommendations.extend([
                "Consider updating electrical and plumbing systems",
                "Modernize kitchen and bathrooms",
                "Add energy-efficient windows"
            ])
        
        # Property type specific recommendations
        if property.property_type == PropertyType.HOUSE:
            recommendations.extend([
                "Enhance curb appeal with landscaping",
                "Consider adding a deck or patio",
                "Update interior paint and flooring"
            ])
        elif property.property_type == PropertyType.APARTMENT:
            recommendations.extend([
                "Modernize appliances",
                "Improve lighting fixtures",
                "Add storage solutions"
            ])
        
        # Size-based recommendations
        if property.square_feet < 1500:
            recommendations.append("Use light colors and mirrors to create illusion of space")
        
        # General recommendations
        recommendations.extend([
            "Professional staging before showing",
            "High-quality photography for listings",
            "Pre-listing home inspection"
        ])
        
        return recommendations
    
    def get_buyer_statistics(self) -> Dict[str, int]:
        """Get statistics about buyers in the system"""
        stats = {
            'total_buyers': 0,
            'active_searches': 0,
            'budget_ranges': {
                'under_200k': 0,
                '200k_400k': 0,
                '400k_600k': 0,
                'over_600k': 0
            }
        }
        
        for user in self.users.values():
            if user.user_type in [UserType.BUYER, UserType.BOTH]:
                stats['total_buyers'] += 1
                
                if user.budget_max:
                    stats['active_searches'] += 1
                    if user.budget_max < 200000:
                        stats['budget_ranges']['under_200k'] += 1
                    elif user.budget_max < 400000:
                        stats['budget_ranges']['200k_400k'] += 1
                    elif user.budget_max < 600000:
                        stats['budget_ranges']['400k_600k'] += 1
                    else:
                        stats['budget_ranges']['over_600k'] += 1
        
        return stats