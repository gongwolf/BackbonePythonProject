# %%
import urllib.request
import json
import os, errno

def getJsonResults(file_name,url,method):
    response = urllib.request.urlopen(url,timeout=60*60)
    content = response.read()
    data = json.loads(content)

    target_file ='json_results/{}/{}'.format(method, file_name)
    parent_folder = 'json_results/{}'.format(method)
    try:
        os.makedirs(parent_folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    if os.path.exists(target_file):
        os.remove(target_file)
        print("delete the file {}".format(target_file))
    
    with open(target_file, 'w') as outfile:
        json.dump(data, outfile)
    
    print("{} {}".format(url, len(data)))

# %%
url_result_mapping = {}
#%% Sheraton Fishmean's Wharf Hotel

url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.80698671424124_-122.41378784179688}_type_lodging_Range_500_busStops_10.json":
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.80698671424124/-122.41378784179688/500/lodging/10"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.80698671424124_-122.41378784179688}_type_lodging_Range_500_busStops_20.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.80698671424124/-122.41378784179688/500/lodging/20"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.80698671424124_-122.41378784179688}_type_lodging_Range_500_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.80698671424124/-122.41378784179688/500/lodging/"})
url_result_mapping.update({"SF_Method_approxRangeIndexedByLocation_ByLocation_{37.80698671424124_-122.41378784179688}_type_lodging_Range_500_busStops_0.json": 
"http://localhost:8080/csDemoWS/rest/query/approxRangeIndexedByLocation/SF/37.80698671424124/-122.41378784179688/500/lodging/"})
url_result_mapping.update({"SF_Method_ExactImprovedIndex_ByLocation_{37.80698671424124_-122.41378784179688}_type_lodging_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/ExactImprovedIndex/SF/37.80698671424124/-122.41378784179688/lodging/"})


#%% Taco Bell
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.778628_-122.392779}_type_food_Range_500_busStops_10.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.778628/-122.392779/500/food/10"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.778628_-122.392779}_type_food_Range_500_busStops_20.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.778628/-122.392779/500/food/20"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.778628_-122.392779}_type_food_Range_500_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.778628/-122.392779/500/food/"})
url_result_mapping.update({"SF_Method_approxRangeIndexedByLocation_ByLocation_{37.778628_-122.392779}_type_food_Range_500_busStops_0.json": 
"http://localhost:8080/csDemoWS/rest/query/approxRangeIndexedByLocation/SF/37.778628/-122.392779/500/food/"})
url_result_mapping.update({"SF_Method_ExactImprovedIndex_ByLocation_{37.778628_-122.392779}_type_food_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/ExactImprovedIndex/SF/37.778628/-122.392779/food/"})
# %% The Ramp

url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.764248_-122.386805}_type_food_Range_500_busStops_10.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.764248/-122.386805/500/food/10"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.764248_-122.386805}_type_food_Range_500_busStops_20.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.764248/-122.386805/500/food/20"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.764248_-122.386805}_type_food_Range_500_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.764248/-122.386805/500/food/"})
url_result_mapping.update({"SF_Method_approxRangeIndexedByLocation_ByLocation_{37.764248_-122.386805}_type_food_Range_500_busStops_0.json": 
"http://localhost:8080/csDemoWS/rest/query/approxRangeIndexedByLocation/SF/37.764248/-122.386805/500/food/"})
url_result_mapping.update({"SF_Method_ExactImprovedIndex_ByLocation_{37.764248_-122.386805}_type_food_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/ExactImprovedIndex/SF/37.764248/-122.386805/food/"})


# %% subway, 5 Embarcadero Center San Francisco, CA 94111
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_food_Range_500_busStops_10.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.794597/-122.395181/500/food/10"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_food_Range_500_busStops_20.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.794597/-122.395181/500/food/20"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_food_Range_500_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.794597/-122.395181/500/food/"})
url_result_mapping.update({"SF_Method_approxRangeIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_food_Range_500_busStops_0.json": 
"http://localhost:8080/csDemoWS/rest/query/approxRangeIndexedByLocation/SF/37.794597/-122.395181/500/food/"})
url_result_mapping.update({"SF_Method_ExactImprovedIndex_ByLocation_{37.794597_-122.395181}_type_food_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/ExactImprovedIndex/SF/37.794597/-122.395181/food/"})


# %% Hyatt Regency, 5 Embarcadero Center San Francisco, CA 94111
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_lodging_Range_500_busStops_10.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.794597/-122.395181/500/lodging/10"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_lodging_Range_500_busStops_20.json": 
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.794597/-122.395181/500/lodging/20"})
url_result_mapping.update({"SF_Method_approxMixedIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_lodging_Range_500_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/approxMixedIndexedByLocation/SF/37.794597/-122.395181/500/lodging/"})
url_result_mapping.update({"SF_Method_approxRangeIndexedByLocation_ByLocation_{37.794597_-122.395181}_type_lodging_Range_500_busStops_0.json": 
"http://localhost:8080/csDemoWS/rest/query/approxRangeIndexedByLocation/SF/37.794597/-122.395181/500/lodging/"})
url_result_mapping.update({"SF_Method_ExactImprovedIndex_ByLocation_{37.794597_-122.395181}_type_lodging_busStops_0.json":
"http://localhost:8080/csDemoWS/rest/query/ExactImprovedIndex/SF/37.794597/-122.395181/lodging/"})
#%%
for filename, url in url_result_mapping.items():
    method = filename.split("_")[2]
    getJsonResults(filename,url,method)


# %%
