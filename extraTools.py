# to incode or decode hex to string:
#Functions not robust and not prepared to receive info that is not aligned with the necessary
#Imports:

import sys
import hashlib
import sha3


##########33

def stringToHex(s):
    EncodedeString='0x'+s.encode("hex") #Encode to hex/ Encode is a builtIn function
    return EncodedeString               #The Ox is a goodpractice normalization in the eth commun.


def hexToStringPart(s,numberChars):   #Function that receives an hex string and n# chars and modifies that number of numberChars
    if s[0:2] == '0x':
        EncodedeString=s[2:numberChars].decode("hex")
        return EncodedeString
    else:
        print("\n Hex string not provided;")


def hexToStringAll(s):   #Function that receives an hex string and n# chars and modifies that number of numberChars
    if s[0:2] == '0x':
        EncodedeString=s[2:].decode("hex")
        return EncodedeString
    else:
        print("\n Hex string not provided;")

def sha3KecaakHex(stringData):  #function that receives a string and will apply the sha3 keccak256 hashing
    sha3Converter=sha3.keccak_256()
    sha3Converter.update(stringData)
    return sha3Converter.hexdigest()



def functionKeccaked(stringData):  #function that receives a function name andand will apply the sha3 keccak256 hashing on a 4 bytes scheme
    sha3Converter=sha3.keccak_256()
    sha3Converter.update(stringData)
    return sha3Converter.hexdigest()[0:8]


def AbijsonReader():
    #name='data.json'
    AbiName='AbiExample.json' ##Importing the ABI File into the engine
    with open(AbiName) as f:
        data = json.load(f)
    #Data will have a list of all the arguments inside the ABIJSON
    #Arguments are composed by dictionaries where type define if its a function, an event, a fallback or a constructor
    return data
