/**** animager cmd-line-tool ****/

#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main( int argc, char* argv[] ){
    
    int i = 1;
    string options = "python /opt/animager/process.py ";
    
    if( argc < 3 ){

        cout << "Invalid input. \n" << "usage : animager -p [video profile] -i [input file] -o [video output folder]\n";
        cout << "usage : animager -pname [profile name] -h [height] -w [width] -f [frame rate]\n";
        exit(EXIT_FAILURE);
    }

    if( argc % 2 == 0  ){

        cout << "Invalid input. \n" << "usage : animager -i [input file] -p [video profile] -o [video output folder]\n";
        cout << "usage : animager -pnew [profile name] -h [height] -w [width] -f [frame rate]\n";
        exit(EXIT_FAILURE);
    }

    while( i < argc ){
        
        options = options + " " + argv[ i ];
        i++;
    }
    
    
    system( options.c_str() );
    
    return 0;
}
