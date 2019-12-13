

int main( void ) {
  FILE* file_pointer;  
  int layer[6][25]; 

  file_pointer = fopen("input.txt", "r");

  // https://www.cs.swarthmore.edu/~newhall/unixhelp/C_files.html  
  if ( infile == NULL ) {  // error checking with fopen call
    printf("Unable to open file."); 
    exit(1);
  } 

  fclose( file_pointer );

  return 1
}
