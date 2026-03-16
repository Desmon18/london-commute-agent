from bus import get_bus_arrivals
from trains import get_elizabeth_line_trains
from routing import can_catch_train

buses = get_bus_arrivals()
trains = get_elizabeth_line_trains()

print("\nBuses from Harlington Corner:")

for bus in buses:
    print(f"Line {bus['line']} to {bus['destination']}")
    print(f"Arrives at {bus['arrival_time']} ({bus['minutes']} mins)\n")

print("\nElizabeth Line trains from Hayes & Harlington Station:")

for train in trains:
    print(f"Line {train['line']} to {train['destination']}")
    print(f"Arrives at {train['arrival_time']} ({train['minutes']} mins)\n")

bus_time = buses[0]['minutes']  # Time until the next bus arrives
train_time = trains[0]['minutes']  # Time until the next train arrives

if can_catch_train(bus_time, train_time):
    print("You can catch the train!")
else:
    print("You will miss the train.")
