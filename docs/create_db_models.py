# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Owner(Base):
    """description: Table to store dog owner's information, including their first and last names, email, and account balance."""
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    account_balance = Column(Float, nullable=False, default=0.0)

class Dog(Base):
    """description: Table to store individual dog information linked to their owner."""
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)

class Walker(Base):
    """description: Table to store dog walker details along with their service rating."""
    __tablename__ = 'walkers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    rating = Column(Float, nullable=True)

class Walk(Base):
    """description: Table to manage details of walk events."""
    __tablename__ = 'walks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'), nullable=False)
    walker_id = Column(Integer, ForeignKey('walkers.id'), nullable=False)
    date_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    duration_minutes = Column(Integer, nullable=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=True)

class Location(Base):
    """description: Table to define possible walk locations including their addresses."""
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)

class Schedule(Base):
    """description: Table to manage availability of walkers by date and time."""
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'), nullable=False)
    available_date = Column(DateTime, nullable=False)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)

class Service(Base):
    """description: Table to list the types of services provided by walkers."""
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

class WalkerService(Base):
    """description: Table to establish the connection between walkers and services they offer."""
    __tablename__ = 'walker_services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)

class Review(Base):
    """description: Table to capture reviews and ratings provided by owners for walkers."""
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)

class Package(Base):
    """description: Table to outline package options available for walks."""
    __tablename__ = 'packages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

class WalkerPackage(Base):
    """description: Table to associate walkers with specific service packages."""
    __tablename__ = 'walker_packages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'), nullable=False)
    package_id = Column(Integer, ForeignKey('packages.id'), nullable=False)

class Subscription(Base):
    """description: Table to record subscriptions of owners to specific packages."""
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    package_id = Column(Integer, ForeignKey('packages.id'), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    end_date = Column(DateTime, nullable=True)

# Set up the SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=False)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample Data Insertions
# Owners
owner1 = Owner(first_name="John", last_name="Doe", email="john.doe@example.com", account_balance=200.0)
owner2 = Owner(first_name="Jane", last_name="Smith", email="jane.smith@example.com", account_balance=150.0)

# Dogs
dog1 = Dog(name="Buddy", breed="Golden Retriever", owner_id=1)
dog2 = Dog(name="Max", breed="Labrador", owner_id=2)

# Walkers
walker1 = Walker(name="Alice Walker", rating=4.5)
walker2 = Walker(name="Bob Hiker", rating=4.7)

# Locations
location1 = Location(name="Central Park", address="Central Park, NYC")
location2 = Location(name="Riverside Park", address="Riverside Dr, NYC")

# Walks
walk1 = Walk(dog_id=1, walker_id=1, date_time=datetime.datetime.now(), duration_minutes=30, location_id=1)
walk2 = Walk(dog_id=2, walker_id=2, date_time=datetime.datetime.now(), duration_minutes=45, location_id=2)

# Schedules
schedule1 = Schedule(walker_id=1, available_date=datetime.datetime.now(), start_time=None, end_time=None)
schedule2 = Schedule(walker_id=2, available_date=datetime.datetime.now(), start_time=None, end_time=None)

# Services
service1 = Service(name="Basic Walk", description="30 minutes walk")
service2 = Service(name="Extended Walk", description="1 hour walk")

# Walker Services
walker_service1 = WalkerService(walker_id=1, service_id=1)
walker_service2 = WalkerService(walker_id=2, service_id=2)

# Reviews
review1 = Review(walker_id=1, owner_id=1, rating=5, comment="Excellent service!")
review2 = Review(walker_id=2, owner_id=2, rating=4, comment="Good but can improve")

# Packages
package1 = Package(name="Weekly Pack", price=50.0)
package2 = Package(name="Monthly Pack", price=180.0)

# Walker Packages
walker_package1 = WalkerPackage(walker_id=1, package_id=1)
walker_package2 = WalkerPackage(walker_id=2, package_id=2)

# Subscriptions
subscription1 = Subscription(owner_id=1, package_id=1, start_date=datetime.datetime.now(), end_date=None)
subscription2 = Subscription(owner_id=2, package_id=2, start_date=datetime.datetime.now(), end_date=None)

# Add and commit all records to the database
session.add_all([
    owner1, owner2, dog1, dog2, walker1, walker2, location1, location2,
    walk1, walk2, schedule1, schedule2, service1, service2, walker_service1,
    walker_service2, review1, review2, package1, package2, walker_package1,
    walker_package2, subscription1, subscription2
])
session.commit()
