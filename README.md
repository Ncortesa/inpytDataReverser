# inpytDataReverser
Ethereum Input data reverser (python build)

The goal of this file is to be able to create a small python library that can transform input data sent to ethereum Smart Contract into human readable information based in the SC ABI;

`Version 0.0.1`

## 1. Full Description:

The EVM receives data in a normalized hexadecimal code. This concept allows the information to flow in an interoperable agnostic environment that can receive the input data from the multiple implementations of ethereum clients;

The standard procedure to deploy functions in smart contracts is translated by sending a transaction (henceforth Tx) with attached input data that will trigger functions in the EVM side; (Assembly injections into nodes can also be a solution but this is not in the scope of this library)

The possibility to reverse this data in a off chain script can be a crucial feature to take bydesign decision on the construction of real life assets certification software. Going into deep details in the Yellow Paper of the ethereum protocol one can relate the gas costs with the allocation of data inside a SC. This costs have no impact in standard users but can be highly punisher in high scale business that record Hundreds of tx’s per day. 
The ability to translate the information of the input data can be then a feature to have in mind. 

## 3. File Organization:

The main library functions will be defined by:
- 'InputReverser.py' 

The complementary files will feed the main library in following logic:

*JSON related functions:*
- 'abiModules.py' 

*Hex converter functions:*
- 'extraTools.py' 


*Some testing files are also added:*
-AbiExample.json
-decoderExample.sol // this sol. file can be runned against the rinkeby with no problem using remix to create Tx with input data;


## 4. RoadMap:

To be defined - This is for now only a sketch of a solution

## 5. Documentation

For thorough documentation on the ABI hex transformation, see:
- [Ethereum ocumentation](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI)
- [How to decipher SC](https://medium.com/@hayeah/how-to-decipher-a-smart-contract-method-call-8ee980311603)
