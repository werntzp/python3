"""
property_address.py - Handle address properties and raise appropriate validation errors
"""
import re
import logging

LOG_FILENAME = "property_address.log"
#LOG_FORMAT = "%(asctime)s %(name)s:%(levelname)s:%(filename)s function:%(funcName)s line:%(lineno)d %(message)s"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "info" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    logging.info("Initialized log")
    
class ZipCodeError(Exception):
    pass

class StateError(Exception):
    pass

class Address():
    
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name # set directly in __init__
        # everything else goes through regular setters
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        logging.info("Creating a new address")
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # since was set in __init__, don't let it get set again
        logging.error("Tried to set name")
        raise AttributeError
        
    @property
    def street_address(self):
        return self._street_address

    @street_address.setter
    def street_address(self, value):
        self._street_address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
         
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        # state must be two-letter, all uppercase
        regex = re.match(r"\A[A-Z][A-Z]\Z", value)
        if regex:
            self._state = value
        else:
            logging.error("STATE exception")
            raise StateError
        
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        # zip code must be no more than 5 digits
        regex = re.match(r"\A\d{5}\Z", value)
        if regex:
            self._zip_code = value    
        else:
            logging.error("ZIPCODE exception")
            raise ZipCodeError
        
