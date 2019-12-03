#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX_LINE_LENGTH       30000


// determines longest line of file
// adapted from: https://github.com/imhoffman/advent/blob/master/2019/01/one.c
void reader ( FILE* f, int* maxlen, char lines[2][MAX_LINE_LENGTH] ) {
  char buffer[MAX_LINE_LENGTH];   
  char *qnull;
  size_t maxtemp;

  *maxlen = 0;
  int n = 0;

  while ( fgets(buffer, MAX_LINE_LENGTH, f) != NULL ) {
    strncpy( lines[n], buffer, MAX_LINE_LENGTH );
    qnull = strchr( buffer, '\0' );                           // finds end of file
    maxtemp = qnull - &buffer[0];                             // finds file length via adress -
    if ( (int)maxtemp > *maxlen ) { *maxlen = (int)maxtemp; }
    n++;
  }
  return;
}



int path_finder ( const int longest_line, const char directions[][], *red_path, *green_path ) {
  
  // writes green wire path
  for ( int i=0; i < longest_line ) {
   
   while ( directions[0][i] != "," ) {
    if     ( directions[0][i] == "R" ) {
    }

    elseif ( directions[0][i] == "L" ) {
    }

    elseif ( directions[0][i] == "U" ) {
    }

    elseif ( directions[0][i] == "D" ) {
    }
   } else { break }
  
  }

  // writes red wire path
  for ( int i=0; i < longest_line ) { 
   
    if     ( directions[1][i] == "R" ) {
    }

    elseif ( directions[1][i] == "L" ) {
    }

    elseif ( directions[1][i] == "U" ) {
    }

    elseif ( directions[1][i] == "D" ) {
    }

  }
 
  return:
}



// main function
int main ( void ) {
  //adapted from: https://github.com/imhoffman/advent/blob/master/2019/01/one.c
  FILE* fp;
  int longest_line, total;                  // might not need total?  
  char file_name [11] = "input.txt";        // change here for different file names

  char (*temp)[MAX_LINE_LENGTH]       
	 = malloc( 2 * sizeof( char ) * MAX_LINE_LENGTH );  // temp can now hold the whole file

  //  file I/O and memory allocation of memory input
  fp = fopen( file_name, "r" );
  reader( fp, &longest_line, temp );        // longest_line is known upon return
  fclose(fp);                               // done with file...only read the file once

  printf( "\n the longest line is %d chars long\n\n", longest_line );

  char directions[2][longest_line+1];

  for( int i=0; i < 2; i++ ) {
     strncpy( directions[i], temp[i], longest_line+1 );
  }

  // `directions` now has the data...free the big temp array from the file read
  free( temp );
  //  end of file I/O 
   
 return 0;
}
