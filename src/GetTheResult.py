#%% 
# Initialize the script
import urllib.request
import json

# Url = "http://128.123.63.83:8080/csDemoWS/rest/query/approxMixedIndexedById/LA/1000/2000/lodging/20"

Types_IDs={'all':1233, 'food':1233,'lodging':100,'restaurant':100}
cities = ["NY","SF","LA"]
# distance_threshold = [200,300,400,500,800,1000,1500,2000]
distance_threshold = [200,500,1000]
method="approxRangeIndexedById"
# method="approxMixedIndexedById"

def getJsonResults(file_name,url,method):
    print(url)
    response = urllib.request.urlopen(url,timeout=60*60)

    content = response.read()

    data = json.loads(content)

    with open('json_results/{}/{}'.format(method, file_name), 'w') as outfile:
        json.dump(data, outfile)

#%% 
""" Get the results from approximate method """
for c in cities:
    for t, ids in Types_IDs.items():
        for busStop in range(0,40,10):
            #do not run the query approxRangeIndexedById with no busStop limitation in LA with any type
            #The running will be timeout
            if method=='approxRangeIndexedById' and busStop==0 and c=="LA":
                continue
            
            for dist_threshold in distance_threshold:
                if t=='all':
                    file_name="{}_Method_{}_ByID_{}_type_all_Range_{}_busStops_{}.json".format(c,method,ids,dist_threshold,busStop)
                    if  busStop==0:
                        url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}/{}//".format(method,c,ids,dist_threshold)
                        getJsonResults(file_name, url,method)
                    else:
                        url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}/{}//{}".format(method,c,ids,dist_threshold,busStop)
                        getJsonResults(file_name, url,method)
                else:
                    file_name="{}_Method_{}_ByID_{}_type_{}_Range_{}_busStops_{}.json".format(c,method,ids,t,dist_threshold,busStop)
                    if  busStop==0:
                        url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}/{}/{}/".format(method,c,ids,dist_threshold,t)
                        getJsonResults(file_name, url,method)
                    else:
                        url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}/{}/{}/{}".format(method,c,ids,dist_threshold,t,busStop)
                        getJsonResults(file_name, url,method)


#%% Get the results from improved exact index method
Types_IDs={'food':1233,'lodging':100,'restaurant':100,'all':1233}
cities = ["NY","SF"]
method="ExactImprovedIndex"
busStop_Range = range(0,40,10)

#%%
#Just for LA query, no all type, no non-limitation on bus stop
Types_IDs={'lodging':100,'restaurant':100,'all':1233} # used for LA, no all type 
cities = ["LA"]
method="ExactImprovedIndex"
busStop_Range = range(10,30,10)


#%%
for c in cities:
    for t, ids in Types_IDs.items():
        for b in busStop_Range:
            if t=='all':
                file_name="{}_Method_{}_ByID_{}_type_all_busStops_{}.json".format(c,method,ids,b)
                if  b==0:
                    url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}//".format(method,c,ids)
                    getJsonResults(file_name, url,method)
                else:
                    url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}//{}".format(method,c,ids,b)
                    getJsonResults(file_name, url,method)
            else:
                file_name="{}_Method_approxMixedIndexedById_ByID_{}_type_{}_busStops_{}.json".format(c,ids,t,b)
                if  b==0:
                    url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}/{}/".format(method,c,ids,t)
                    getJsonResults(file_name, url,method)
                else:
                    url = "http://128.123.63.83:8080/csDemoWS/rest/query/{}/{}/{}/{}/{}".format(method,c,ids,t,b)
                    getJsonResults(file_name, url,method)




#%%
