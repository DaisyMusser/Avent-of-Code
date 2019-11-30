#include <stdio.h>
#define MAXCHAR 9999999



// takes directions array of arbitrary length and returns the specified floor
// can loose the counter processing and just pass in size after measure mod is working
int translator ( char directions[] ) {
   int i, floor, counter;
   
   floor = 0;

   for ( i=0; i<1000; i++ ) {
      if ( directions[i] != '\0' ) { counter = counter + 1; }
      else break;
   }

   for ( i=0; i < counter; i++ ) {
      if ( directions[i] == '(' ) { floor = floor + 1; }
      if ( directions[i] == ')' ) { floor = floor - 1; }
   }

   return floor;
}



// main program
int main ( void ) {
   FILE* fp;
   char *buffer;

   buffer = (char *) malloc( MAXCHAR * sizeof( char ) );  

   fp = fopen( "input.txt", "r" );

   while ( fgets( buffer, MAXCHAR, fp ) ) {
      

   printf ( "ta-da: %d \n", translator( temp ) );

   return 0;
}
