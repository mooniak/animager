/**** cmd-line-tool ****/

#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main( int argc, char* argv[] ){
    
    int i = 1;
    string options = "python process.py -i /home/lahiru/Desktop/temp/temp";
    
    while( i < argc ){
        
        options = options + " " + argv[ i ];
        i++;
    }
    
    
    system( options.c_str() );
    
    return 0;
}