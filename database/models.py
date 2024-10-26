# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 26, 2024 16:31:58
# Database: sqlite:////tmp/tmp.VvkxNl8L2Z/dog_iter_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Location(SAFRSBaseX, Base):
    """
    description: Table to define possible walk locations including their addresses.
    """
    __tablename__ = 'locations'
    _s_collection_name = 'Location'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="location")



class Owner(SAFRSBaseX, Base):
    """
    description: Table to store dog owner's information, including their first and last names, email, and account balance.
    """
    __tablename__ = 'owners'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String)
    account_balance = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    DogList : Mapped[List["Dog"]] = relationship(back_populates="owner")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="owner")
    SubscriptionList : Mapped[List["Subscription"]] = relationship(back_populates="owner")



class Package(SAFRSBaseX, Base):
    """
    description: Table to outline package options available for walks.
    """
    __tablename__ = 'packages'
    _s_collection_name = 'Package'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    SubscriptionList : Mapped[List["Subscription"]] = relationship(back_populates="package")
    WalkerPackageList : Mapped[List["WalkerPackage"]] = relationship(back_populates="package")



class Service(SAFRSBaseX, Base):
    """
    description: Table to list the types of services provided by walkers.
    """
    __tablename__ = 'services'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    WalkerServiceList : Mapped[List["WalkerService"]] = relationship(back_populates="service")



class Walker(SAFRSBaseX, Base):
    """
    description: Table to store dog walker details along with their service rating.
    """
    __tablename__ = 'walkers'
    _s_collection_name = 'Walker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="walker")
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="walker")
    WalkerPackageList : Mapped[List["WalkerPackage"]] = relationship(back_populates="walker")
    WalkerServiceList : Mapped[List["WalkerService"]] = relationship(back_populates="walker")
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="walker")



class Dog(SAFRSBaseX, Base):
    """
    description: Table to store individual dog information linked to their owner.
    """
    __tablename__ = 'dogs'
    _s_collection_name = 'Dog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    owner_id = Column(ForeignKey('owners.id'), nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("DogList"))

    # child relationships (access children)
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="dog")



class Review(SAFRSBaseX, Base):
    """
    description: Table to capture reviews and ratings provided by owners for walkers.
    """
    __tablename__ = 'reviews'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'), nullable=False)
    owner_id = Column(ForeignKey('owners.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("ReviewList"))
    walker : Mapped["Walker"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class Schedule(SAFRSBaseX, Base):
    """
    description: Table to manage availability of walkers by date and time.
    """
    __tablename__ = 'schedules'
    _s_collection_name = 'Schedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'), nullable=False)
    available_date = Column(DateTime, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("ScheduleList"))

    # child relationships (access children)



class Subscription(SAFRSBaseX, Base):
    """
    description: Table to record subscriptions of owners to specific packages.
    """
    __tablename__ = 'subscriptions'
    _s_collection_name = 'Subscription'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owners.id'), nullable=False)
    package_id = Column(ForeignKey('packages.id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("SubscriptionList"))
    package : Mapped["Package"] = relationship(back_populates=("SubscriptionList"))

    # child relationships (access children)



class WalkerPackage(SAFRSBaseX, Base):
    """
    description: Table to associate walkers with specific service packages.
    """
    __tablename__ = 'walker_packages'
    _s_collection_name = 'WalkerPackage'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'), nullable=False)
    package_id = Column(ForeignKey('packages.id'), nullable=False)

    # parent relationships (access parent)
    package : Mapped["Package"] = relationship(back_populates=("WalkerPackageList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerPackageList"))

    # child relationships (access children)



class WalkerService(SAFRSBaseX, Base):
    """
    description: Table to establish the connection between walkers and services they offer.
    """
    __tablename__ = 'walker_services'
    _s_collection_name = 'WalkerService'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'), nullable=False)
    service_id = Column(ForeignKey('services.id'), nullable=False)

    # parent relationships (access parent)
    service : Mapped["Service"] = relationship(back_populates=("WalkerServiceList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerServiceList"))

    # child relationships (access children)



class Walk(SAFRSBaseX, Base):
    """
    description: Table to manage details of walk events.
    """
    __tablename__ = 'walks'
    _s_collection_name = 'Walk'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dog_id = Column(ForeignKey('dogs.id'), nullable=False)
    walker_id = Column(ForeignKey('walkers.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer)
    location_id = Column(ForeignKey('locations.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("WalkList"))
    location : Mapped["Location"] = relationship(back_populates=("WalkList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkList"))

    # child relationships (access children)
