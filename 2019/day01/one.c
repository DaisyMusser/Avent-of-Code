#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX_LINE_LENGTH       100
#define MAX_LINES_IN_FILE     30000

//
//  subroutine for determining length of file and longest single line
//  the file read is held in a large temporary array that is free'ed
//  in main once an appropriately-sized array is allocated and populated
void reader ( FILE* f, int* n, int* maxlen, char lines[][MAX_LINE_LENGTH] ) {
  char buffer[MAX_LINE_LENGTH];   // fgets null-terminates
  char *qnull;
  size_t maxtemp;

  *maxlen=0;
  *n = 0;
  while ( fgets(buffer, MAX_LINE_LENGTH, f) != NULL ) {
    strncpy( lines[*n], buffer, MAX_LINE_LENGTH );
    qnull = strchr( buffer, '\0' );  // no need to memset buffer to all \0 every loop
    maxtemp = qnull - &buffer[0];    // arithmetic among memory addresses
    if ( (int)maxtemp > *maxlen ) { *maxlen =(int) maxtemp; }
    (*n)++;
  }
  return;
}


//  function to parse mass into fuel from input string
int fuel_parser ( const char input[] ) {
  int mass, fuel;

  sscanf( input, "%d", &mass );

  fuel =(int) floor( (double)mass / 3.0 );
  fuel = fuel - 2;

  return fuel;
}

//
// main program
//
int main( int argc, char *argv[] ) {
 FILE* fp;
 int number_of_lines, longest_line, total;
 char (*temp)[MAX_LINE_LENGTH]
     = malloc( MAX_LINES_IN_FILE * sizeof( char ) * MAX_LINE_LENGTH );
         //  do we need to cast from (void *) to (char *) ?

 //  file I/O and memory allocation of memory input
 fp = fopen("puzzle.txt","r");
 reader( fp, &number_of_lines, &longest_line, temp );  // n and longest_line are known upon return
 fclose(fp);        // done with file...only read the file once

 printf( "\n read %d lines from the input file\n", number_of_lines );
 printf( "\n the longest line is %d chars long\n\n", longest_line );

 // declare an array of appropriate length and width
 char input[number_of_lines][longest_line+1];

 //  populate `input` with puzzle data for use going forward
 for( int i=0; i < number_of_lines; i++ ) {
  strncpy( input[i], temp[i], longest_line+1 );
 }
 // `input` now has the data...free the big temp array from the file read
 free( temp );
 //  end of file I/O

 //  puzzle solution
 total = 0;
 for ( int i=0; i < number_of_lines; i++ ) {
   total += fuel_parser( input[i] );
 }
 printf( "\n total fuel needed: %d\n\n", total );

 return 0;
}
