"""
NYC Transit Challenge! 
Use OOP and inheritance to design subway and bus stations.
"""

"""
DO NOT EDIT THE MetroStation CLASS
"""
class MetroStation:
    """The MetroStation class is a base/parent class for all types of metro stations
    (bus, rail, subway, etc), containing their shared traits and functionality (aka attributes and methods).

    All metro stations have a name, a location, and default to being open.
    All metro stations must be able to open, close, and show their info.
    """
    def __init__(self, station_name, location):
        self.station_name = station_name
        self.location = location

        self.is_open = True

    def open_station(self):
        """Open a closed station"""
        self.is_open = True

    def close_station(self):
        """Close an open station"""
        self.is_open = False
    
    def show_info(self):
        """Display the current info about the station"""
        # Fancy python syntax
        open_info = 'open' if self.is_open else 'closed'
        print(f'{self.station_name} station is located at {self.location}. It is currently {open_info}.')


# 1.1 TODO: Using the MetroStation class above as the parent, make a child class called `SubwayStation`
#   `SubwayStation` should:
#   - Have an additional attribute called `lines` that is user-defined as a list during initialization.
#       This will indicate which subway lines stop at the station (for example ['A', 'C'])
#   - Override the show_info() method from MetroStation to display which subway lines stop there, in addition to the station_name and location

class SubwayStation(MetroStation):
    def __init__(self, station_name, location, lines: list):
        super().__init__(station_name, location)
        self.lines = lines

    def show_info(self):
        """Display the current info about the station"""
        open_info = 'open' if self.is_open else 'closed'
        print(f'{self.station_name} station is located at {self.location}. Lines {self.lines} stop here. It is currently {open_info}.')
# 1.2 TODO: Using your `SubwayStation` class, instantiate a subway station with the info below. 
# Then run the show_info() method.
# Make sure it prints out the station_name, location, whether it's open, and lines printed out
#   (NOTE: This means that the code in `MetroStation.show_info()` should still run in the `SubwayStation` code)
# station_name: '14th street'
# location: '14th street and 7th avenue'
# lines: ['1', '2', '3', 'L']

subway_station = SubwayStation('14th street', '14th street and 7th avenue', ['1', '2', '3', 'L'])
subway_station.show_info()

# 2.1 TODO: Using the `MetroStation` class below as the parent, make a child class called `BusStation`
# `BusStation` should:
# - Have an additional attribute called 'routes' that is user-defined as a list during initialization. 
#     this will indicate where buses can go from this station. For example, ['DC', 'Philly', 'Pittsburgh']
# - Have two additional methods:
#   - add_route()
#   - remove_route()
#   ^ both should take in a route to either add or remove from the list of routes, respectively.
# - Override the show_info() method to display the bus routes in addition to the station name and location
#   (NOTE: This means that the code in `MetroStation.show_info()` should still run in the `SubwayStation` code)      

class BusStation(MetroStation):
    def __init__(self, station_name, location, routes: list):
        super().__init__(station_name, location)
        self.routes = routes
    
    def add_route(self, route: str):
        self.routes.append(route)

    def remove_route(self, route: str):
        self.routes.remove(route)

    def show_info(self):
        """Display the current info about the station"""
        open_info = 'open' if self.is_open else 'closed'
        print(f'{self.station_name} station is located at {self.location}. List of routes: {self.routes}. It is currently {open_info}.')
# 3.0 TODO: Using your `BusStation` class:
# 3.1 Instantiate a bus station with the info below. 
# 3.2 Then, run the show_info() method to make sure you get the station_name, location, routes, and whether the station is open printed out
# 3.3 Demonstrate that you can close and open the bus station
#     i.e. that the show_info() method reflects correctly when the station is open versus closed.
#     NOTE: This requires running the `.close_station()` method
# station_name: 'NYC Megabus Stop'
# location: '34th street and 12th avenue'
# routes: ['Boston', 'DC', 'Philly']

bus_station = BusStation('NYC Megabus Stop', '34th street and 12th avenue', ['Boston', 'DC', 'Philly'])
bus_station.close_station()
bus_station.show_info()
bus_station.open_station()
bus_station.show_info()