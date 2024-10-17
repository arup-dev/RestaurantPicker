import requests
import json

#Importing my api key
with open('config.json', 'r') as file:
    config = json.load(file)
    API_KEY = config.get('api_key')

def get_top_restaurants(city, num_results=10):
        # Using Geocoding API to get the geocodes
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={API_KEY}"
        geocode_response = requests.get(geocode_url)
        if geocode_response.status_code != 200:
                print("Error with Geocoding API:", geocode_response.status_code)
                return []
        geocode_data = geocode_response.json()
        if not geocode_data['results']:
                print("No results found for the city.")
                return []
        location = geocode_data['results'][0]['geometry']['location']
        lat, lng = location['lat'], location['lng']
        # Using the Places API to search for restaurants near the city
        places_url = (
                f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
                f"?location={lat},{lng}&radius=1500&type=restaurant&key={API_KEY}&rankby=prominence"
        )
        places_response = requests.get(places_url)
        if places_response.status_code != 200:
                print("Error with Places API:", places_response.status_code)
                return []
        places_data = places_response.json()
        if not places_data['results']:
                print("No restaurants found.")
                return []
        # Gets the details of the top restaurants
        restaurants = []
        for place in places_data['results'][:num_results]:
                restaurant = {
                        'name': place.get('name'),
                        'rating': place.get('rating'),
                        'address': place.get('vicinity'),
                        'total reviews': place.get('user_ratings_total')
                }
                restaurants.append(restaurant)
        return restaurants

def save_to_json(data, filename):
        # Saves the details of the top restaurants to a json file
        with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
                print(f"Data saved to {filename}")

def main():
        city = input("Enter the city: ")
        # Gets the top restaurants
        restaurants = get_top_restaurants(city)
        if restaurants:
                # Save the top restaurants to the JSON file
                filename = f"top_10_restaurants_{city.lower().replace(' ', '_')}.json"
                save_to_json(restaurants, filename)
        else:
                print("No results found or an error occurred.")

if __name__ == "__main__":
        main()
