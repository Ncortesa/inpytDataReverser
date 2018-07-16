# to incode or decode hex to string:
#Functions not robust and not prepared to receive info that is not aligned with the necessary

def stringToHex(s):
    EncodedeString='0x's.encode("hex") #Encode to hex/ Encode is a builtIn function
                                       #The Ox is a goodpractice normalization in the eth commun.
def hexToHex(s):
    if s[0:2] == '0x':
        EncodedeString=s[2:].decode("hex")
    else:
        print("\n Hex string not provided;")
