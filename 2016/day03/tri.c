int tricheck( int a, int b, int c ) {
   if ( a+b <= c ) { return 0; }
   if ( b+c <= a ) { return 0; }
   if ( c+a <= b ) { return 0; }
   return 1; 
}

// main program
int x = tricheck( 3, 3, 3 );

