# %%
import json


# %% define the city list
LA_city_list = ["agoura hills", "alhambra", "arcadia", "artesia", "avalon", "azusa", "baldwin park", "bell", "bell gardens", "bellflower", "beverly hills", "bradbury", "burbank", "calabasas", "carson", "cerritos", "claremont", "commerce", "compton", "covina", "cudahy", "culver city", "diamond bar", "downey", "duarte", "el monte", "el segundo", "gardena", "glendale", "glendora", "hawaiian gardens", "hawthorne", "hermosa beach", "hidden hills", "huntington park", "industry", "inglewood", "irwindale", "la cañada flintridge", "la habra heights", "la mirada", "la puente", "la verne", "lakewood", "lancaster", "lawndale",
                "lomita", "long beach", "los angeles", "lynwood", "malibu", "manhattan beach", "maywood", "monrovia", "montebello", "monterey park", "norwalk", "palmdale", "palos verdes estates", "paramount", "pasadena", "pico rivera", "pomona", "rancho palos verdes", "redondo beach", "rolling hills", "rolling hills estates", "rosemead", "san dimas", "san fernando", "san gabriel", "san marino", "santa clarita", "santa fe springs", "santa monica", "sierra madre", "signal hill", "south el monte", "south gate", "south pasadena", "temple city", "torrance", "vernon", "walnut", "west covina", "west hollywood", "westlake village", "whittier"]


# %% Read the business data from the json file
business_json_file = "/home/gqxwolf/mydata/DemoProject/yelp_dataset/business.json"
# business_json_file = "/home/gqxwolf/mydata/DemoProject/yelp_dataset/example.json"

business_obj = []
with open(business_json_file) as json_file:
    for line in json_file:
        business_obj.append(json.loads(line))
business_obj[5000:5100]

# %%
city_list = []
state_list = []

for b_obj in business_obj:
    city_list.append(str.lower(b_obj['city']).strip())
    state_list.append(str.upper(b_obj['state']).strip())

cities = list(set(city_list))
states = list(set(state_list))
print(states)
len(cities), len(city_list), len(states)


# %%
LA_list = []
for c in city_list:
    if c in LA_city_list:
        LA_list.append(c)

len(LA_list), len(set(LA_list)),len(LA_city_list) 


#%%
review_json_file_name = "/home/gqxwolf/mydata/DemoProject/yelp_dataset/review.json"
review_obj = []
with open(review_json_file_name) as json_file:
    for line in json_file:
        review_obj.append(json.loads(line))
review_obj[9999]


#%%
