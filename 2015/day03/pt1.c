#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXMOVES 999999


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

  } else { 
    
    printf( ":(\n" );
    return 1;
  
  }
  
  fclose( fp );
  
  printf( "%d\n", number_of_moves );

  return 0;
}
