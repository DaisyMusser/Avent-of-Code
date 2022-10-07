// made this file as a class
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXMOVES 999999


void mover ( const char current_move, int *x, int *y ) {
  switch ( current_move ) {
    case '>': *x = *x+1; break;
    case '<': *x = *x-1; break;
    case '^': *y = *y+1; break;
    case 'v': *y = *y-1; break;
  }

  return;
}

int main ( void ) {
  char *end_of_list, buffer[MAXMOVES];
  FILE *fp;
  int number_of_moves;
  size_t differnce;

  fp = fopen( "input.txt", "r" );

  if (fgets ( buffer, MAXMOVES, fp ) != NULL ) {
    
    end_of_list = strchr( buffer, '\0' );
    differnce = end_of_list - &buffer[0];    
    number_of_moves = (int) differnce;  

  } else {   //error catching 
     
    printf( ":(\n" );
    return 1;
  
  }
  
  fclose( fp );
  
  int x=0, y=0;
  for ( int i = 0; i < number_of_moves; i++ ) {
    printf( "move: %c, x: %d, y: %d", buffer[i], x, y );
  }

  return 0;
}
