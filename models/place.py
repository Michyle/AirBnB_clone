#!/usr/bin/python3
"""Defines the p_lace class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Rep a place

    Attributes:
    city_id (str): city id
    user_id (str): user id
    name (str): name of place
    description (str): the description of thr place
    number_rooms (int): num rooms in place
    number_bathrooms (int): num bathrooms in the place
    max_guest (int): The maximum number of guests of the place.
    price_by_night (int): The price by night of the place.
    latitude (float): The latitude of the place.
    longitude (float): The longitude of the place.
    amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
