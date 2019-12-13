// https://stackoverflow.com/questions/4600797/read-int-values-from-a-text-file-in-c
void read_ints ( const char* file_name ) {
  FILE* file = fopen (file_name, "r");
  int i = 0;

  fscanf (file, "%d", &i);    
  while (!feof (file))
    {  
      printf ("%d ", i);
      fscanf (file, "%d", &i);      
    }
  fclose (file);        
}


int main( void ) {
  FILE* file_pointer;  
  int layer[6][25]; 

  file_pointer = fopen("input.txt", "r");

  // https://www.cs.swarthmore.edu/~newhall/unixhelp/C_files.html  
  if ( file_pointer == NULL ) {  // error checking with fopen call
    printf("Unable to open file."); 
    exit(1);
  } 

  fclose( file_pointer );

  return 1
}
