import requests
from datetime import datetime
from config.journey_config import HAYES_HARLINGTON_STATION_ID

def get_elizabeth_line_trains():
    """Fetches the next 5 Elizabeth Line train arrivals at Hayes & Harlington Station.
    """

    url = f"https://api.tfl.gov.uk/stopPoint/{HAYES_HARLINGTON_STATION_ID}/Arrivals"
    response = requests.get(url)
    elizabeth_line_trains = response.json()

    # Sort by expected arrival time
    elizabeth_line_trains = sorted(elizabeth_line_trains, key=lambda x: x["timeToStation"])

    results = []
    
    for train in elizabeth_line_trains[:5]:

        minutes = train["timeToStation"] // 60  # convert seconds to minutes
        
        arrival_time = datetime.fromisoformat(train["expectedArrival"].replace("Z", "+00:00")).strftime("%H:%M:%S")
        
        results.append({
            "destination": train["destinationName"],
            "arrival_time": arrival_time,
            "minutes": minutes
        })

    return results
