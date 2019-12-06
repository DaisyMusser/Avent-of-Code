#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX_LINE_LENGTH       100
#define MAX_LINES_IN_FILE     30000

// should return an array of that contains only the input
char reader ( int *max_lenght, int *number_of_lines, char file_name[MAX_LINE_LENGTH] ) {
    FILE* fp;
    char buffer[MAX_LINE_LENGTH];   // fgets null-terminates
    char *qnull, (*temp)[MAX_LINE_LENGTH] = malloc( MAX_LINES_IN_FILE * sizeof( char ) * MAX_LINE_LENGTH );
    size_t maxtemp;

    fp = fopen( file_name, "r" );
    while ( fgets(buffer, MAX_LINE_LENGTH, fp) != NULL ) {
        strncpy( temp[*number_of_lines], buffer, MAX_LINE_LENGTH );
        qnull = strchr( buffer, '\0' );
        maxtemp = qnull - &buffer[0];
        if ( (int)maxtemp > *max_lenght ) {
            max_lenght = (int)maxtemp;
        }
        *number_of_lines ++;
    }
    
    fclose( fp );

    char input[number_of_lines][max_lenght+1];
    for( int i=0; i < number_of_lines; i++ ) {
        strncpy( input[i], temp[i], max_lenght+1 );
    }
    
    free( temp );

    return &input;
}


//  function to parse mass into fuel from input string
int fuel_parser ( const int mass ) {
    int fuel;
    
    fuel = floor( (double)mass / 3.0 ) - 2;

    return fuel;
}


//
// main program
//
int main ( void ) {
    char file_name[MAX_LINE_LENGTH] = "input.txt";
    int max_lenght = 0;
    int number_of_lines = 0;
    
    input = reader( &max_lenght, &number_of_lines, file_name );
    
    return 0;
}
