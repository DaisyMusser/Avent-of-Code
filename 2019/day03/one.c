#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX_LINE_LENGTH       30000



// determines longest line of file
// adapted from: https://github.com/imhoffman/advent/blob/master/2019/01/one.c
void reader ( FILE* f, int* maxlen, char lines[][MAX_LINE_LENGTH] ) {
  char buffer[MAX_LINE_LENGTH];   
  char *qnull;
  size_t maxtemp;

  *maxlen=0;
  int n = 0;

  while ( fgets(buffer, MAX_LINE_LENGTH, f) != NULL ) {
    strncpy( lines[n], buffer, MAX_LINE_LENGTH );
    qnull = strchr( buffer, '\0' );  // no need to memset buffer to all \0 every loop
    maxtemp = qnull - &buffer[0];    // finds file length w/ adress differnce
    if ( (int)maxtemp > *maxlen ) { *maxlen = (int)maxtemp; }
    n++;
  }
  return;
}


int main ( void ) {

}
