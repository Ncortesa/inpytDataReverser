#All the Abi manipulation functions will be detailed here

#Imports:
import json

def AbijsonReader(s):
    #name='data.json'
    AbiName='AbiExample.json' ##Importing the ABI File into the engine
    #hardcoded now but going to Int mode should be replaced with the string input of the function
    with open(AbiName) as f:
        data = json.load(f)
    #Data will have a list of all the arguments inside the ABIJSON
    #Arguments are composed by dictionaries where type define if its a function, an event, a fallback or a constructor
    return data #list will be returned

def argumentNameRetriever(dic): #receives an ABI argument -> should be a dictionary
    if dic["type"].encode('ascii','ignore')=="function":
        nameFunction=dic["name"].encode('ascii','ignore') #information from the ABI comes in unicode so a Ascii modification is required
        #print(nameFunction)
        return(nameFunction)
