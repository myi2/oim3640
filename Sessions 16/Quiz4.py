import requests

#================================== Question 1
def get_town_names() -> list:
    """
    Returns a sorted list of town names from the provided API.
    """
    try:
        # Make a request to the API
        response = requests.get('http://107.173.19.148/mass')
        response.raise_for_status()  
        
        # Parse the JSON response and extract the 'data' list
        data = response.json()['data'] 
        
        # Extract town names and sort them
        town_names = [town['name'] for town in data]
        town_names.sort()
        
        return town_names
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

names = get_town_names()
print(type(names), len(names))
print(names)  

#================================== Question 2
def get_population_by_name(town_name: str) -> int:
    """
    Returns the population of the given town, 0 if the town's name is invalid
    """
    try:
        # Make a request to the API
        response = requests.get('http://107.173.19.148/mass')
        response.raise_for_status() 
        
        # Parse the JSON data
        towns_data = response.json()['data']  
        
        # Search for the town by name
        for town in towns_data:
            if town['name'].lower() == town_name.lower():  
                return town['population']  
        
        return 0  
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

print(get_population_by_name('Wellesley'))  
print(get_population_by_name('New York'))  

#================================== Question 3

def find_smallest_town() -> str:
    """
    Returns the town's name that has the smallest population.
    """
    try:
        # Make a request to the API
        response = requests.get('http://107.173.19.148/mass')
        response.raise_for_status()
        
        # Parse the JSON data
        towns_data = response.json()['data']
        
        # Initialize variables to track the smallest town
        smallest_population = float('inf')  
        smallest_town_name = ""
        
        # Iterate through the list of towns
        for town in towns_data:
            if town['population'] < smallest_population:
                smallest_population = town['population']
                smallest_town_name = town['name']
        
        return smallest_town_name
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return ""

smallest = find_smallest_town()
print(smallest)

#================================== Question 4

def get_mayors_dict() -> dict:
    """
    Returns a dictionary that maps mayors to their towns, {str: list}
    """
    try:
        # Make a request to the API
        response = requests.get('http://107.173.19.148/mass')
        response.raise_for_status()
        
        # Parse the JSON data
        towns_data = response.json()['data']
        
        # Initialize the dictionary
        mayors_dict = {}
        
        for town in towns_data:
            mayor = town['mayor']
            town_name = town['name']
            if mayor in mayors_dict:
                mayors_dict[mayor].append(town_name)
            else:
                mayors_dict[mayor] = [town_name]
        
        return mayors_dict
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {}

mayors_dict = get_mayors_dict()
print(mayors_dict['Marissa'])  

#================================== EXTRA Question 5
def sort_mayors_by_pop() -> list:
    """
    Returns a list that records the mayor names sorted by the total population
    they are managing from most to least.
    """
    try:
        # Make a request to the API
        response = requests.get('http://107.173.19.148/mass')
        response.raise_for_status()
        
        # Parse the JSON data
        towns_data = response.json()['data']
        
        # Initialize a dictionary to track total population for each mayor
        mayors_population = {}
        
        for town in towns_data:
            mayor = town['mayor']
            population = town['population']
            if mayor in mayors_population:
                mayors_population[mayor] += population
            else:
                mayors_population[mayor] = population
        
        # Sort mayors by total population in descending order
        sorted_mayors = sorted(mayors_population.items(), key=lambda x: x[1], reverse=True)
        
        # Extract sorted list of mayor names
        sorted_mayor_names = [mayor[0] for mayor in sorted_mayors]
        
        return sorted_mayor_names
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []


sorted_mayor_list = sort_mayors_by_pop()
print(sorted_mayor_list)




