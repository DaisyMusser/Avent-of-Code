#include<stdio.h>

// should write layer with int from file_name
// https://stackoverflow.com/questions/4600797/read-int-values-from-a-text-file-in-c
void read_ints ( const char* file_name, int* layer[6][25] ) {
  FILE* file = fopen (file_name, "r");
  int temp = 0;

  while ( fscanf ( file, "%d", &temp ) != "EOF" ) {    
    for ( int i = 0; i++; i < 6 ) {
      for ( int ii = 0; ii++; i < 25 ) {
        layer[i][ii] = temp;
      }
    }
  }

  fclose (file);
  return;        
}


int main( void ) {
  int layer[6][25]; 
  char file_name[20] = "input.txt";

  read_ints ( file_name, layer );
  printf ( "%d", %layer[0][0] )

  return 1;
}
