from config.journey_config import BUS_TO_STATION

def can_catch_train(bus_minutes, train_minutes):
    """Determines if the user can catch the train based on bus and train arrival times.
    
    Args:
        bus_minutes (int): Minutes until the bus arrives at the station.
        train_minutes (int): Minutes until the train arrives at the station.
    Returns:
        bool: True if the user can catch the train, False otherwise.
    """
    arrival_station = bus_minutes + BUS_TO_STATION

    if arrival_station < train_minutes:
        return True

    return False
