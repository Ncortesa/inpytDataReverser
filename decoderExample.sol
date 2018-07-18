pragma solidity ^0.4.18;



contract decoderTesting {


bool variavelBoolena1;
bool variavelBoolena2;

int256 variavelInteiro1;
int256 variavelInteiro2;


function set1Bool (bool _variavelBooleana1) public {
    variavelBoolena1= _variavelBooleana1;
}

function set2Bool (bool _variavelBooleana1,bool _variavelBooleana2) public {
     variavelBoolena1= _variavelBooleana1;
     variavelBoolena2= _variavelBooleana2;
}

function set1Int (int256 _variavelInteiro1) public {
    variavelInteiro1= _variavelInteiro1;

}

function set2Int (int256 _variavelInteiro1,int256 _variavelInteiro2) public {
    variavelInteiro1= _variavelInteiro1;
    variavelInteiro2= _variavelInteiro2;
}

function set1Int1Bool(int256 _variavelInteiro1, bool _variavelBoolena1){
    variavelInteiro1= _variavelInteiro1;
    variavelBoolena1= _variavelBoolena1;
}



}
    
