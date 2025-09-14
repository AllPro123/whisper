"""
Command Line Interface for the Real Estate Helper App
"""

import sys
from typing import List, Optional
from .models import Property, User, Agent, ServiceProvider, PropertyType, UserType, ServiceType
from .matcher import PropertyMatcher
from .services import ServiceProviderDirectory


class RealEstateApp:
    """Main application class for the Real Estate Helper"""
    
    def __init__(self):
        self.matcher = PropertyMatcher()
        self.directory = ServiceProviderDirectory()
        self._load_sample_data()
    
    def _load_sample_data(self):
        """Load some sample data for demonstration"""
        # Sample properties
        properties = [
            Property(
                id="prop1",
                address="123 Oak Street",
                city="Austin",
                state="TX",
                zip_code="78701",
                property_type=PropertyType.HOUSE,
                bedrooms=3,
                bathrooms=2.0,
                square_feet=1800,
                lot_size=0.25,
                price=450000,
                seller_id="seller1",
                description="Beautiful family home with updated kitchen",
                features=["granite counters", "hardwood floors", "two-car garage"]
            ),
            Property(
                id="prop2", 
                address="456 Pine Avenue",
                city="Austin",
                state="TX",
                zip_code="78702",
                property_type=PropertyType.CONDO,
                bedrooms=2,
                bathrooms=1.5,
                square_feet=1200,
                lot_size=0.0,
                price=320000,
                seller_id="seller2",
                description="Modern condo in downtown area",
                features=["city views", "pool", "gym access"]
            ),
            Property(
                id="prop3",
                address="789 Elm Drive",
                city="Dallas",
                state="TX", 
                zip_code="75201",
                property_type=PropertyType.HOUSE,
                bedrooms=4,
                bathrooms=3.0,
                square_feet=2400,
                lot_size=0.5,
                price=580000,
                seller_id="seller3",
                description="Spacious home in quiet neighborhood",
                features=["large yard", "master suite", "updated appliances"]
            )
        ]
        
        for prop in properties:
            self.matcher.add_property(prop)
        
        # Sample users
        users = [
            User(
                id="buyer1",
                name="John Smith",
                email="john@example.com",
                phone="555-0123",
                user_type=UserType.BUYER,
                budget_min=300000,
                budget_max=500000,
                preferred_cities=["Austin"],
                preferred_property_types=[PropertyType.HOUSE, PropertyType.CONDO],
                min_bedrooms=2
            ),
            User(
                id="seller1",
                name="Jane Doe",
                email="jane@example.com", 
                phone="555-0456",
                user_type=UserType.SELLER
            )
        ]
        
        for user in users:
            self.matcher.add_user(user)
        
        # Sample agents
        agents = [
            Agent(
                id="agent1",
                name="Bob Wilson",
                email="bob@realty.com",
                phone="555-0789",
                license_number="TX123456",
                agency="Premier Realty",
                specialties=[PropertyType.HOUSE, PropertyType.CONDO],
                areas_served=["Austin", "Dallas"],
                years_experience=8,
                rating=4.8
            )
        ]
        
        for agent in agents:
            self.directory.add_agent(agent)
        
        # Sample service providers
        providers = [
            ServiceProvider(
                id="sp1",
                name="Mike's Home Inspection",
                email="mike@inspection.com",
                phone="555-1111",
                service_type=ServiceType.HOME_INSPECTOR,
                company="Thorough Inspections LLC",
                description="Comprehensive home inspections",
                areas_served=["Austin", "Dallas"],
                price_range="$300-500",
                rating=4.9,
                certifications=["ASHI Certified"]
            ),
            ServiceProvider(
                id="sp2",
                name="Green Thumb Landscaping",
                email="info@greenthumb.com",
                phone="555-2222",
                service_type=ServiceType.LANDSCAPER,
                company="Green Thumb LLC",
                description="Professional landscaping services",
                areas_served=["Austin"],
                price_range="$500-2000",
                rating=4.7
            ),
            ServiceProvider(
                id="sp3",
                name="Perfect Staging Co",
                email="stage@perfect.com",
                phone="555-3333",
                service_type=ServiceType.STAGER,
                company="Perfect Staging",
                description="Home staging for quick sales",
                areas_served=["Austin", "Dallas"],
                price_range="$1000-3000",
                rating=4.6
            )
        ]
        
        for provider in providers:
            self.directory.add_service_provider(provider)
    
    def show_main_menu(self):
        """Display the main menu"""
        print("\n=== Real Estate Helper App ===")
        print("1. Find property matches for buyer")
        print("2. Get property value enhancement recommendations")
        print("3. Find service providers")
        print("4. Find real estate agents")
        print("5. View system statistics")
        print("6. Exit")
        print("================================")
    
    def find_property_matches(self):
        """Find property matches for a buyer"""
        print("\nAvailable buyers:")
        for user_id, user in self.matcher.users.items():
            if user.user_type in [UserType.BUYER, UserType.BOTH]:
                print(f"  {user_id}: {user.name}")
        
        user_id = input("\nEnter buyer ID: ").strip()
        if not user_id:
            return
        
        matches = self.matcher.find_matches(user_id)
        
        if not matches:
            print("No matching properties found.")
            return
        
        print(f"\nFound {len(matches)} matching properties:")
        for i, (property, score) in enumerate(matches, 1):
            print(f"\n{i}. {property.address}, {property.city}")
            print(f"   Price: ${property.price:,.0f}")
            print(f"   {property.bedrooms} bed, {property.bathrooms} bath")
            print(f"   {property.square_feet} sq ft")
            print(f"   Match Score: {score:.1%}")
            print(f"   Description: {property.description}")
    
    def get_enhancement_recommendations(self):
        """Get property value enhancement recommendations"""
        print("\nAvailable properties:")
        for prop_id, prop in self.matcher.properties.items():
            print(f"  {prop_id}: {prop.address}, {prop.city} - ${prop.price:,.0f}")
        
        prop_id = input("\nEnter property ID: ").strip()
        if prop_id not in self.matcher.properties:
            print("Property not found.")
            return
        
        property = self.matcher.properties[prop_id]
        
        # Get recommendations from matcher
        recommendations = self.matcher.get_property_recommendations(prop_id)
        
        # Get service recommendations
        service_recs = self.directory.get_service_recommendations(property.price)
        
        # Get value enhancement plan
        plan = self.directory.get_value_enhancement_plan(property.price, property.city)
        
        print(f"\nEnhancement recommendations for {property.address}:")
        print("\nGeneral Recommendations:")
        for rec in recommendations:
            print(f"  • {rec}")
        
        print("\nService Recommendations:")
        for rec in service_recs:
            print(f"  • {rec}")
        
        print("\nRecommended Service Providers:")
        for service_type, providers in plan.items():
            print(f"\n{service_type.replace('_', ' ').title()}:")
            for provider in providers:
                print(f"  • {provider.name} ({provider.company}) - Rating: {provider.rating}/5")
                print(f"    Phone: {provider.phone}, Price: {provider.price_range}")
    
    def find_service_providers(self):
        """Find service providers"""
        print("\nAvailable service types:")
        for service_type in ServiceType:
            print(f"  {service_type.value}")
        
        service_input = input("\nEnter service type: ").strip().lower()
        
        # Find matching service type
        service_type = None
        for st in ServiceType:
            if st.value == service_input:
                service_type = st
                break
        
        if not service_type:
            print("Service type not found.")
            return
        
        city = input("Enter city (optional): ").strip()
        if not city:
            city = None
        
        providers = self.directory.find_service_providers(service_type, city, min_rating=4.0)
        
        if not providers:
            print("No service providers found.")
            return
        
        print(f"\nFound {len(providers)} service providers:")
        for provider in providers:
            print(f"\n• {provider.name} ({provider.company})")
            print(f"  Phone: {provider.phone}")
            print(f"  Rating: {provider.rating}/5")
            print(f"  Price Range: {provider.price_range}")
            print(f"  Areas: {', '.join(provider.areas_served)}")
            if provider.description:
                print(f"  Description: {provider.description}")
    
    def find_agents(self):
        """Find real estate agents"""
        city = input("Enter city (optional): ").strip()
        if not city:
            city = None
        
        agents = self.directory.find_agents(city=city, min_experience=2)
        
        if not agents:
            print("No agents found.")
            return
        
        print(f"\nFound {len(agents)} agents:")
        for agent in agents:
            print(f"\n• {agent.name} ({agent.agency})")
            print(f"  Phone: {agent.phone}")
            print(f"  License: {agent.license_number}")
            print(f"  Experience: {agent.years_experience} years")
            print(f"  Rating: {agent.rating}/5")
            print(f"  Areas: {', '.join(agent.areas_served)}")
            specialties = [s.value for s in agent.specialties]
            print(f"  Specialties: {', '.join(specialties)}")
    
    def show_statistics(self):
        """Show system statistics"""
        buyer_stats = self.matcher.get_buyer_statistics()
        directory_stats = self.directory.get_directory_stats()
        
        print("\n=== System Statistics ===")
        print(f"Total Properties: {len(self.matcher.properties)}")
        print(f"Available Properties: {sum(1 for p in self.matcher.properties.values() if p.is_available)}")
        print(f"Total Users: {len(self.matcher.users)}")
        print(f"Total Buyers: {buyer_stats['total_buyers']}")
        print(f"Active Buyer Searches: {buyer_stats['active_searches']}")
        
        print(f"\nBuyer Budget Distribution:")
        for range_name, count in buyer_stats['budget_ranges'].items():
            print(f"  {range_name.replace('_', ' ').title()}: {count}")
        
        print(f"\nService Providers: {directory_stats['total_providers']}")
        print(f"Real Estate Agents: {directory_stats['total_agents']}")
        print(f"High-Rated Providers (4.5+): {directory_stats['high_rated_providers']}")
        
        print(f"\nProviders by Service Type:")
        for service_type, count in directory_stats['by_service_type'].items():
            print(f"  {service_type.replace('_', ' ').title()}: {count}")
    
    def run(self):
        """Run the main application loop"""
        while True:
            self.show_main_menu()
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.find_property_matches()
            elif choice == "2":
                self.get_enhancement_recommendations()
            elif choice == "3":
                self.find_service_providers()
            elif choice == "4":
                self.find_agents()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                print("Thank you for using Real Estate Helper App!")
                break
            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")


def main():
    """Main entry point for the CLI application"""
    try:
        app = RealEstateApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()