
distances = {
    "Bethesda": 3.4,
    "Bloomingdale": 5.5,
    "Georgetown": 2.6,
    "Logan Circle": 4.1,
    "Foggy Bottom": 3.9
}
speed = 20

time_min = {location: (distance / speed) * 60 for location, distance in distances.items()}
time_min
