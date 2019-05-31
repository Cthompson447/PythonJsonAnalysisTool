import json
import io
import nested_lookup
from nested_lookup import get_all_keys
from nested_lookup import get_occurrence_of_key

with io.open('petitionz.json', encoding ='ISO-8859-1') as json_file:
	content = json_file.read()
	json_data = json.loads(content)
	
print (type(json_data))	

print (get_all_keys(json_data))
print (get_occurence_of_key(json_data, key='signature_count'))
#def find(key, dictionary):
    #for k, v in json_data.items():
        #if k == key:
         #   yield v
        #elif isinstance(v, dict):
        #    for result in find(key, v):
       #         yield result
      #  elif isinstance(v, list):
     #       for d in v:
    #            for result in find(key, d):
   #                 yield result
  
list(find('signatures_by_country', json_data))
print (list)
#jdata = json.load(json_data.decode("utf-8","ignore"))
#print(json.dumps(data, indent =4, sort_keys=True))

