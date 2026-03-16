import requests
from datetime import datetime
from config.journey_config import BUS_STOP_ID

def get_bus_arrivals():
    
    url = f"https://api.tfl.gov.uk/StopPoint/{BUS_STOP_ID}/Arrivals"

    response = requests.get(url)
    data = response.json()

    buses = sorted(data, key=lambda x: x["timeToStation"])
    bus_arrivals = []

    for bus in buses[:5]:  # Get the next 5 bus arrivals
        line = bus["lineName"]
        destination = bus["destinationName"]
        minutes = bus["timeToStation"] // 60  # convert seconds to minutes
        arrival_time = datetime.fromisoformat(bus["expectedArrival"].replace("Z", "+00:00")).strftime("%H:%M:%S")
        
        bus_arrivals.append({
            "line": line,
            "destination": destination,
            "arrival_time": arrival_time,
            "minutes": minutes
        })

    return bus_arrivals
