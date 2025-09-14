"""
Service provider directory and recommendation system
"""

from typing import List, Dict, Optional
from .models import ServiceProvider, ServiceType, Agent


class ServiceProviderDirectory:
    """Directory of service providers and agents"""
    
    def __init__(self):
        self.service_providers: Dict[str, ServiceProvider] = {}
        self.agents: Dict[str, Agent] = {}
    
    def add_service_provider(self, provider: ServiceProvider) -> None:
        """Add a service provider to the directory"""
        self.service_providers[provider.id] = provider
    
    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the directory"""
        self.agents[agent.id] = agent
    
    def find_service_providers(self, 
                             service_type: ServiceType, 
                             city: str = None, 
                             min_rating: float = 0.0) -> List[ServiceProvider]:
        """Find service providers by type, location, and rating"""
        providers = []
        
        for provider in self.service_providers.values():
            if provider.service_type != service_type:
                continue
            
            if provider.rating < min_rating:
                continue
            
            if city and city.lower() not in [area.lower() for area in provider.areas_served]:
                continue
            
            providers.append(provider)
        
        # Sort by rating (highest first)
        providers.sort(key=lambda p: p.rating, reverse=True)
        return providers
    
    def find_agents(self, 
                   city: str = None, 
                   property_type=None, 
                   min_experience: int = 0) -> List[Agent]:
        """Find agents by location, specialty, and experience"""
        agents = []
        
        for agent in self.agents.values():
            if min_experience > 0 and agent.years_experience < min_experience:
                continue
            
            if city and city.lower() not in [area.lower() for area in agent.areas_served]:
                continue
            
            if property_type and property_type not in agent.specialties:
                continue
            
            agents.append(agent)
        
        # Sort by rating and experience
        agents.sort(key=lambda a: (a.rating, a.years_experience), reverse=True)
        return agents
    
    def get_value_enhancement_plan(self, property_price: float, city: str) -> Dict[str, List[ServiceProvider]]:
        """Get a comprehensive value enhancement plan for a property"""
        plan = {}
        
        # Essential services for any property
        essential_services = [
            ServiceType.HOME_INSPECTOR,
            ServiceType.CLEANER,
            ServiceType.PHOTOGRAPHER
        ]
        
        # Enhancement services based on property value
        enhancement_services = []
        if property_price > 300000:
            enhancement_services.extend([
                ServiceType.STAGER,
                ServiceType.LANDSCAPER,
                ServiceType.CONTRACTOR
            ])
        else:
            enhancement_services.extend([
                ServiceType.CLEANER,
                ServiceType.LANDSCAPER
            ])
        
        # Find providers for each service type
        all_services = essential_services + enhancement_services
        for service_type in all_services:
            providers = self.find_service_providers(
                service_type=service_type,
                city=city,
                min_rating=4.0
            )
            if providers:
                plan[service_type.value] = providers[:3]  # Top 3 providers
        
        return plan
    
    def get_service_recommendations(self, property_price: float) -> List[str]:
        """Get service recommendations based on property value"""
        recommendations = []
        
        # Always recommended
        recommendations.extend([
            "Professional home inspection to identify issues",
            "Deep cleaning before photos and showings",
            "Professional photography for online listings"
        ])
        
        # Based on property value
        if property_price > 500000:
            recommendations.extend([
                "Professional staging to showcase the property",
                "Landscaping to enhance curb appeal", 
                "Consider minor renovations for high-impact improvements",
                "Professional appraisal to ensure optimal pricing"
            ])
        elif property_price > 200000:
            recommendations.extend([
                "Basic staging of key rooms",
                "Yard cleanup and basic landscaping",
                "Touch-up painting where needed"
            ])
        else:
            recommendations.extend([
                "Declutter and organize all spaces",
                "Basic yard maintenance",
                "Ensure all fixtures are working properly"
            ])
        
        return recommendations
    
    def get_directory_stats(self) -> Dict[str, int]:
        """Get statistics about the service provider directory"""
        stats = {
            'total_providers': len(self.service_providers),
            'total_agents': len(self.agents),
            'by_service_type': {},
            'high_rated_providers': 0
        }
        
        # Count by service type
        for provider in self.service_providers.values():
            service_type = provider.service_type.value
            stats['by_service_type'][service_type] = stats['by_service_type'].get(service_type, 0) + 1
            
            if provider.rating >= 4.5:
                stats['high_rated_providers'] += 1
        
        return stats