import requests

lat = 51.48074
lon = -0.43309

# Bus Stop ID 
stop_id = "490007811B"

# Get nearby bus stops using the TFL API
# url = f"https://api.tfl.gov.uk/StopPoint?lat={lat}&lon={lon}&stopTypes=NaptanPublicBusCoachTram&radius=300"

# TFL API to get bus stop information by stop ID
url = f"https://api.tfl.gov.uk/StopPoint/{stop_id}/Arrivals"

response = requests.get(url)
data = response.json()

# sort bus arrivals by expected arrival time
data = sorted(data, key=lambda x: x["expectedArrival"])

print(f"Bus arrivals at stop {stop_id}:\n")

for bus in data[:5]:
    line = bus["lineName"]
    destination = bus["destinationName"]
    time = bus["timeToStation"] // 60  # convert seconds to minutes

    print(f"Line {line} to {destination} arriving in {time} minutes")

# for stop in data["stopPoints"]:
#     print(stop["commonName"], stop["id"])