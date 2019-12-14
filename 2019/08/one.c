#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAXCHARS 65536

// file-reader subroutine to determine dynamic lengths
// from https://gitlab.com/imhoffman/fa19b4-mat3006/blob/master/code/day15/single_line.c
void reader( FILE *f, int *n, char file_contents[] ) {
  char buffer[MAXCHARS] = { '\0' };
  int num_lines = 0;
  char *qnull;
  size_t file_length;

  while ( fgets( buffer, MAXCHARS, f ) != NULL ) {
    strncpy( file_contents, buffer, MAXCHARS );
    num_lines = num_lines + 1;
  }

  if ( num_lines > 1 ) {
	  printf( "\n PROBLEM: more than one line in file\n" );
	  *n = -1;
	  return;
  }

  qnull = strchr( file_contents, '\0' );
  file_length = qnull - &file_contents[0];   // difference of size_t's
  *n =(int) file_length;

  return;
}


int main( int argc, char *argv[] ) {
  // https://gitlab.com/imhoffman/fa19b4-mat3006/blob/master/code/day15/single_line.c
  //  file I/O
  FILE* fp;
  int nchars;
  char *temp;
  temp =(char *) malloc( MAXCHARS * sizeof( char ) );
  fp = fopen("input.txt","r");     // change file name here!
  reader( fp, &nchars, temp);
  fclose(fp);

  char *input = malloc( (nchars+1) * sizeof( char ) );
  strncpy( input, temp, nchars );
  free( temp );     // free the huge temporary file-read buffer
  input[nchars+1] = '\0';    // is this really needed ?
  printf( "\n read in %d characters from one line\n\n", nchars);
 
  return 0;
}
