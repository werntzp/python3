"""
property_address.py - Handle address properties and raise appropriate validation errors
"""
import re
import logging
from optparse import OptionParser
import configparser

# config info
config = configparser.RawConfigParser()
config.read('V:/workspace/Python3_Homework12/src/property_address.cfg')
zip_code_validator = config.get('validators', 'zip_code')
state_validator = config.get("validators", "state")
log_format = config.get("log", "format")
log_filename = config.get("log", "output")

# logging
#LOG_FILENAME = "property_address.log"
#LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "info" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(filename=log_filename, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=log_format)
    logging.info("Initialized log")
   
def validate_zip(value):
    # zip code must be no more than 5 digits
    regex = re.match(zip_code_validator, value)
    if regex:
        return  value    
    else:
        logging.error("ZIPCODE exception")
        raise ZipCodeError
            
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
        regex = re.match(state_validator, value)
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
        try:
            self._zip_code = validate_zip(value)
        except:
            raise ZipCodeError


if __name__ == '__main__':   
    
    # set parser options
    parser = OptionParser()
    parser.add_option('-l', '--level', dest="level", action="store", 
                            help="Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL")
    parser.add_option('-n', '--name', dest="name", 
                            action="store", help="Sets the name value of the Address object")    
    parser.add_option('-a', '--address', dest="address", 
                            action="store", help="Sets the street_address value of the Address object")    
    parser.add_option('-c', '--city', dest="city", 
                            action="store", help="Sets the city value of the Address object")    
    parser.add_option('-s', '--state', dest="state", 
                            action="store", help="Sets the state value of the Address object")    
    parser.add_option('-z', '--zip_code', dest="zip_code", 
                            action="store", help="Sets the zip_code value of the Address object")    
    (options, args) = parser.parse_args()

    # initiate the logging
    if not options.level:
        start_logging()
    else:
        start_logging(level=options.level.lower())

    # perform validation
    if not options.name and not options.address and not options.state and not options.state and not options.zip_code:
        parser.error("options -n, -a, -c, -s, -z are required")

    # check for valid zip before creating address
    if options.zip_code:
        try:
            zip = validate_zip(options.zip_code)
        except:
            parser.error("option -z requires a valid 5-digit US zip code")
    
    # create an address object
    a = Address( name=options.name, street_address=options.address, city=options.city, state=options.state, zip_code=options.zip_code)
    
     
