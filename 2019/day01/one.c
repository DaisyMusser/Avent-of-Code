#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

// will find size of file and put contents of file into int array
//void file_reader ( ){


// takes a specific mod mass and returns fuel requiremnts 
int fuel_counter ( int mass ){
    int fuel;

    fuel = floor((double) mass / 3 ) - 2;

    return fuel;
}


int main ( void ){
    int example = 100756;
    int x;
    
    x = fuel_counter ( example );
    printf ( "\n\n%d  \n\n\n", x );

    return 0;
}
