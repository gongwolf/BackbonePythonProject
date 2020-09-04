import json
import math

max_value = math.inf

json_file = "/home/gqxwolf/mydata/BackBone_Py_Project/src/json_results/backup/ExactImprovedIndex/SF_Method_ExactImprovedIndex_ByLocation_{37.794597_-122.395181}_type_food_busStops_0.json"

max_walking = 0
max_index = 0
index = 0 
dict_max_walking={}
with open(json_file) as json_file:
    data = json.load(json_file)
    for o in data:
        name = o['end_name']
        if name in dict_max_walking:
            if o['costs'][0] > max_walking:
                max_walking = o['costs'][0]
                dict_max_walking.update({name:o['costs'][0]})
        else:
            dict_max_walking.update({name:o['costs'][0]})
print(max_walking)
for key,value in dict_max_walking.items():
    print(key,"    ",value)
