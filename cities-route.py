import numpy as np
import folium
import googlemaps
from sko.GA import GA_TSP
import matplotlib.pyplot as plt

# Initialize Google Maps API client
API_KEY = "AIzaSyB2ICaLs0Jq9U5OyEGzvVsryUI913KdlwE" # Replace with your API key
gmaps = googlemaps.Client(key=API_KEY)

# Get user input for cities
num_cities = int(input("Enter the number of cities: "))
cities = [input(f"Enter city {i+1} name: ") for i in range(num_cities)]

# Fetch city coordinates
city_coordinates = []
for city in cities:
    location = gmaps.geocode(city)
    if location:
        lat = location[0]['geometry']['location']['lat']
        lng = location[0]['geometry']['location']['lng']
        city_coordinates.append((lat, lng))
    else:
        print(f"Error: Could not find location for {city}")
        exit()

# Fetch road distances and routes using Google Directions API
distance_matrix = np.zeros((num_cities, num_cities))
road_routes = {}

for i, origin in enumerate(cities):
    for j, destination in enumerate(cities):
        if i != j:
            # Fetch route details from Google Directions API
            directions_result = gmaps.directions(origin, destination, mode="driving")
            distance = directions_result[0]['legs'][0]['distance']['value']  # Distance in meters
            route = [(step['end_location']['lat'], step['end_location']['lng']) for step in
                     directions_result[0]['legs'][0]['steps']]  # Extract route path
            distance_matrix[i, j] = distance / 1000  # Convert to kilometers
            road_routes[(i, j)] = route

# Objective function for the genetic algorithm
def cal_total_distance(routine):
    """
    Objective function for the genetic algorithm.
    Calculates the total road distance for a given routine (order of visiting cities).
    """
    num_cities, = routine.shape
    return sum([distance_matrix[routine[i % num_cities], routine[(i + 1) % num_cities]] for i in range(num_cities)])

# 1. Generate a Random Route
random_route = np.random.permutation(num_cities)
random_route_ = np.concatenate([random_route, [random_route[0]]])  # Close the loop
random_route_distance = cal_total_distance(random_route)

# Create a Folium map for the random route
m_random = folium.Map(location=city_coordinates[0], zoom_start=5)
for i, coord in enumerate(city_coordinates):
    folium.Marker(location=coord, popup=cities[i], icon=folium.Icon(color='blue')).add_to(m_random)
for i in range(len(random_route_) - 1):
    start = random_route_[i]
    end = random_route_[i + 1]
    folium.PolyLine(locations=road_routes[(start, end)], color='orange', weight=5, opacity=0.7).add_to(m_random)
m_random.save("random_route_map.html")
print(f"Random route map saved as 'random_route_map.html' with distance: {random_route_distance:.2f} km")

# 2. Optimize the Route using GA
ga_tsp = GA_TSP(func=cal_total_distance, n_dim=num_cities, size_pop=100, max_iter=1000, prob_mut=0.2)
best_points, best_distance = ga_tsp.run()

# Prepare the optimized route
best_points_ = np.concatenate([best_points, [best_points[0]]])  # Close the loop
optimized_route_coords = [city_coordinates[i] for i in best_points_]

# Create a Folium map for the optimized route
m_optimized = folium.Map(location=city_coordinates[0], zoom_start=5)
for i, coord in enumerate(city_coordinates):
    folium.Marker(location=coord, popup=cities[i], icon=folium.Icon(color='blue')).add_to(m_optimized)
for i in range(len(best_points_) - 1):
    start = best_points_[i]
    end = best_points_[i + 1]
    folium.PolyLine(locations=road_routes[(start, end)], color='red', weight=5, opacity=0.7).add_to(m_optimized)
m_optimized.save("optimized_route_map.html")
print(f"Optimized route map saved as 'optimized_route_map.html' with distance: {best_distance[0]:.2f} km")

# 3. Plot Improvement in Distance over Generations
plt.figure(figsize=(10, 6))
plt.plot(ga_tsp.generation_best_Y, label='GA Optimization Progress', color='green')
plt.axhline(y=random_route_distance, color='orange', linestyle='--', label='Random Route Distance')
plt.title("Distance Reduction Using Genetic Algorithm", fontsize=16)
plt.xlabel("Generation", fontsize=14)
plt.ylabel("Distance (km)", fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig("distance_reduction_plot.png")
plt.show()

# Print distances for comparison
print(f"Random Route Distance: {random_route_distance:.2f} km")
print(f"Optimized Route Distance: {best_distance[0]:.2f} km")