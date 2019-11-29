#include <stdio.h>
#define MAXCHAR 9999999



// takes directions array and returns floor they send you too
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
   char directions[] = { ')', ')', ')','(','(','(' };
   
   printf( "\n\n %d\n\n", translator( directions ) );
}
