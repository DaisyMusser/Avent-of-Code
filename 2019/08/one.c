#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAXCHARS 65536

//  file-reader subroutine to determine dynamic lengths
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


//
// main program
//
// takes cammand line args??
int main( int argc, char *argv[] ) {

  //  file I/O
  FILE* fp;
  int total_chars;
  char *temp;
  // temp is given memory for maxchar char
  temp =(char *) malloc( MAXCHARS * sizeof( char ) );
  fp = fopen("intput.txt","r");
  reader( fp, &total_chars, temp);
  fclose(fp);

  printf("through reader module");

  char *input = malloc( (total_chars+1) * sizeof( char ) );
  strncpy( input, temp, total_chars );
  free( temp );     // free the huge temporary file-read buffer
  input[total_chars+1] = '\0';    // is this really needed ?
  printf( "\n read in %d characters from one line\n\n", total_chars);
  //  end of file I/O


  return 0;
}

