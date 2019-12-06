// this file is almost all copied from https://github.com/imhoffman/advent/blob/master/2019/01/one.c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX_LINE_LENGTH       100
#define MAX_LINES_IN_FILE     30000

// should return an array of that contains only the input
void reader ( int *max_lenght, int *number_of_lines, const char file_name[MAX_LINE_LENGTH], char temp[][MAX_LINE_LENGTH] ){
    FILE* fp;
    char buffer[MAX_LINE_LENGTH];   // fgets null-terminates
    char *qnull;
    size_t temp_max;
    
    *number_of_lines = 0;
    *max_lenght = 0;

    fp = fopen( file_name, "r" );
    while ( fgets(buffer, MAX_LINE_LENGTH, fp) != NULL ) {
        strncpy( temp[*number_of_lines], buffer, MAX_LINE_LENGTH );
        qnull = strchr( buffer, '\0' );
        temp_max = qnull - &buffer[0];
        if ( (int)temp_max > *max_lenght ) {   // make temp_max max_lenght if its > than max_length
            *max_lenght = (int)temp_max;
        }
        *number_of_lines ++;     // gives me an expression unused warning on compile? dont know why??
    }
    
    fclose( fp );        // need to manually close file

    return;
}


//  function returns fuel needed to carry inputed mass
int fuel_counter ( const int mass ) {
    int fuel = floor( (double)mass / 3.0 ) - 2;
    return fuel;
}


//
// main program
//
int main ( void ) {
    char file_name[MAX_LINE_LENGTH] = "input.txt";     // change file name here!
    int max_lenght, number_of_lines, total_fuel;
    char (*temp)[MAX_LINE_LENGTH] = malloc( MAX_LINES_IN_FILE * sizeof( char ) * MAX_LINE_LENGTH );
    // above the memory for temp is being manually allocated
    
    reader( &max_lenght, &number_of_lines, file_name, temp );
    //
    
    char input[number_of_lines][max_lenght+1];
    for( int i=0; i < number_of_lines; i++ ) {
        strncpy( input[i], temp[i], max_lenght+1 );
    }
    
    free( temp );
    // bc temp was manually allocted, it can now be released
    
    for ( int i=0; i < number_of_lines; i++ ) {
        total_fuel += fuel_counter( (int)input[i]);
    }
    
    printf("\n%d\n\n", total_fuel);
    return 0;
}
